#!/usr/bin/env python3
"""Local HTTP proxy gateway that sends chosen domains through a pool of VLESS/Trojan configs.

The gateway listens on 127.0.0.1 and routes by domain: hosts listed in domains.txt
leave through the currently healthy tunnel config, everything else connects direct.
A supervisor (`serve`) keeps the tunnel alive by probing and rotating configs.

User data lives in the platform's config dir (override with PROXY_TUNNEL_HOME):
  ~/.config/proxy-tunnel          Linux
  ~/Library/Application Support/proxy-tunnel   macOS
  %APPDATA%\\proxy-tunnel        Windows

  pool.txt      one share link per line, top of file tried first
  domains.txt   one domain per line; subdomains match too
  state.json    last good config, dead cooldowns
  gateway.json  generated xray config (do not edit by hand)
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import io
import json
import os
import platform
import re
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlencode, urlparse

CANARY = os.environ.get("PROXY_TUNNEL_CANARY") or "https://www.youtube.com/"
SCAN_TIMEOUT = 6
GATEWAY_TIMEOUT = 10
DEAD_COOLDOWN = 60
IS_WIN = os.name == "nt"


def _default_home() -> Path:
    if IS_WIN:
        base = os.environ.get("APPDATA")
        return Path(base) / "proxy-tunnel" if base else Path.home() / "AppData/Roaming/proxy-tunnel"
    if sys.platform == "darwin":
        return Path.home() / "Library/Application Support/proxy-tunnel"
    return Path.home() / ".config/proxy-tunnel"


HOME = Path(os.environ.get("PROXY_TUNNEL_HOME") or _default_home())
POOL = HOME / "pool.txt"
DOMAINS = HOME / "domains.txt"
STATE = HOME / "state.json"
GATEWAY = HOME / "gateway.json"
GATEWAY_LOG = HOME / "gateway.log"
LOG_BACKUP = HOME / "gateway.log.1"
LOG_MAX_BYTES = int(os.environ.get("PROXY_TUNNEL_LOG_MAX") or 2_000_000)
LOG_KEEP_LINES = 200
PIDFILE = HOME / "gateway.pid"
BIN_DIR = HOME / "bin"
XRAY_VERSION = os.environ.get("XRAY_VERSION") or "26.10.31"

SEED_DOMAINS = [
    "youtube.com", "googlevideo.com", "ytimg.com", "youtu.be",
    "x.com", "twitter.com", "t.co", "twimg.com",
    "telegram.org", "t.me", "telegram.me",
    "chatgpt.com", "openai.com", "claude.ai", "anthropic.com",
    "gemini.google.com", "perplexity.ai", "huggingface.co",
    "instagram.com", "facebook.com", "fbcdn.net", "whatsapp.com", "whatsapp.net",
]


# ---------------------------------------------------------------- xray discovery

def _v2rayn_root() -> Path | None:
    """v2rayN's data directory, which differs per platform and install flavour."""
    if IS_WIN:
        for base in (os.environ.get("APPDATA"), os.environ.get("LOCALAPPDATA")):
            if base and (Path(base) / "v2rayN").is_dir():
                return Path(base) / "v2rayN"
        return None
    if sys.platform == "darwin":
        root = Path.home() / "Library/Application Support/v2rayN"
        return root if root.is_dir() else None
    root = Path.home() / ".local/share/v2rayN"
    return root if root.is_dir() else None


def v2rayn_xray() -> Path | None:
    root = _v2rayn_root()
    name = "xray.exe" if IS_WIN else "xray"
    if root:
        for candidate in (root / "bin/xray" / name, root / "bin" / name):
            if candidate.is_file():
                return candidate
    return None


def v2rayn_db() -> Path | None:
    root = _v2rayn_root()
    if root:
        db = root / "guiConfigs/guiNDB.db"
        if db.is_file():
            return db
    return None


def cached_xray() -> Path | None:
    if not BIN_DIR.is_dir():
        return None
    name = "xray.exe" if IS_WIN else "xray"
    for folder in sorted(BIN_DIR.glob("xray-*"), reverse=True):
        binary = folder / name
        if binary.is_file():
            return binary
    return None


def find_xray() -> str | None:
    for candidate in (os.environ.get("XRAY_BIN"), shutil.which("xray"),
                      v2rayn_xray(), cached_xray()):
        if candidate and Path(candidate).is_file():
            return str(candidate)
    return None


def _asset_name() -> str:
    osname = {"nt": "windows", "darwin": "macos"}.get(os.name, "linux")
    machine = platform.machine().lower()
    if machine in ("x86_64", "amd64"):
        arch = "64"
    elif machine in ("aarch64", "arm64"):
        arch = "arm64-v8a"
    elif machine in ("i386", "i686", "x86"):
        arch = "32"
    elif machine.startswith("armv7"):
        arch = "arm32-v7a"
    elif machine.startswith("armv6"):
        arch = "arm32-v6"
    else:
        sys.exit(f"no xray build for {os.name}/{machine}; set XRAY_BIN to an existing binary")
    return f"Xray-{osname}-{arch}.zip"


def _http_get(url: str, timeout: int = 180) -> bytes:
    request = urllib.request.Request(url, headers={"user-agent": "proxy-tunnel/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def _latest_release() -> str | None:
    """Newest published Xray tag, used only when the pinned one is gone."""
    try:
        meta = json.loads(_http_get(
            "https://api.github.com/repos/XTLS/Xray-core/releases/latest", timeout=30))
    except (OSError, ValueError, urllib.error.URLError):
        return None
    return str(meta.get("tag_name") or "").lstrip("v") or None


def _release_files(version: str, asset: str) -> tuple[str, bytes, str]:
    """Download the asset and its digest; fall back to the latest tag if 404.

    The pinned version is only a default, and GitHub keeps every release, so a
    404 means the tag itself is wrong or was withdrawn. That is the one failure
    `setup` cannot recover from on a fresh machine, so resolve it here rather
    than making every new user edit the source.
    """
    def fetch(tag: str) -> tuple[bytes, str]:
        url = f"https://github.com/XTLS/Xray-core/releases/download/v{tag}/{asset}"
        return _http_get(url), _http_get(url + ".dgst", timeout=30).decode("utf-8", "replace")

    print(f"xray not found; downloading {asset} (v{version})", file=sys.stderr)
    try:
        archive, digest = fetch(version)
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
        latest = _latest_release()
        if not latest or latest == version:
            raise
        print(f"v{version} is not published; retrying with latest v{latest}", file=sys.stderr)
        version = latest
        archive, digest = fetch(version)
    return version, archive, digest


def download_xray(version: str = XRAY_VERSION) -> str:
    """Fetch the official release once, verify it, and keep it under the data dir."""
    asset = _asset_name()
    try:
        version, archive, digest_text = _release_files(version, asset)
    except (OSError, urllib.error.URLError) as exc:
        sys.exit(f"xray download failed ({exc}); set XRAY_BIN to an existing xray binary")
    expected = re.search(r"SHA2-256=\s*([0-9a-f]{64})", digest_text)
    if expected is None or hashlib.sha256(archive).hexdigest() != expected.group(1):
        sys.exit("downloaded xray archive failed its SHA-256 check; not installing it")
    target = BIN_DIR / f"xray-{version}"
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        member = next((n for n in bundle.namelist() if Path(n).name in ("xray", "xray.exe")), None)
        if member is None:
            sys.exit(f"{asset} does not contain an xray binary")
        binary = target / Path(member).name
        binary.write_bytes(bundle.read(member))
    binary.chmod(0o755)
    print(f"installed {binary}", file=sys.stderr)
    return str(binary)


_XRAY: str | None = None


def xray(allow_download: bool = True) -> str:
    global _XRAY
    if _XRAY is None:
        found = find_xray()
        if found:
            _XRAY = found
        elif allow_download:
            _XRAY = download_xray()
        else:
            sys.exit("xray binary not found; run `tunnel.py setup` or set XRAY_BIN")
    return _XRAY


# ---------------------------------------------------------------- share links

def _q(query: dict, *names: str, default: str = "") -> str:
    for n in names:
        if query.get(n):
            return query[n][0]
    return default


def parse_uri(uri: str) -> dict:
    """Turn one vless:// or trojan:// share link into an xray outbound."""
    u = urlparse(uri.strip())
    scheme = u.scheme.lower()
    if scheme not in ("vless", "trojan"):
        raise ValueError(f"unsupported scheme {scheme!r} (only vless and trojan)")
    if not u.hostname or not u.port:
        raise ValueError("missing host or port")

    q = parse_qs(u.query)
    net = _q(q, "type", "network", default="tcp").lower()
    net = {"raw": "tcp", "http": "tcp"}.get(net, net)
    sec = _q(q, "security", default="none").lower()
    sni = _q(q, "sni", "peer") or u.hostname
    host_header = _q(q, "host") or sni

    stream: dict = {"network": net}
    if net == "ws":
        stream["wsSettings"] = {
            "path": _q(q, "path", default="/"),
            "headers": {"Host": host_header},
        }
    elif net == "grpc":
        stream["grpcSettings"] = {"serviceName": _q(q, "serviceName")}
    elif net == "tcp" and _q(q, "headerType").lower() == "http":
        stream["tcpSettings"] = {
            "header": {
                "type": "http",
                "request": {
                    "path": [_q(q, "path", default="/")],
                    "headers": {"Host": [host_header]},
                },
            }
        }
    elif net == "xhttp":
        stream["xhttpSettings"] = {
            "path": _q(q, "path", default="/"),
            "host": host_header,
            "mode": _q(q, "mode", default="auto"),
        }

    if sec in ("tls", "reality"):
        stream["security"] = sec
        tls = {"serverName": sni, "allowInsecure": _q(q, "allowInsecure") == "1"}
        alpn = _q(q, "alpn")
        if alpn:
            tls["alpn"] = [a for a in alpn.split(",") if a]
        fp = _q(q, "fp", "fingerprint")
        if fp:
            tls["fingerprint"] = fp
        stream["tlsSettings"] = tls
        if sec == "reality":
            stream["realitySettings"] = {
                "serverName": sni,
                "fingerprint": fp or "chrome",
                "publicKey": _q(q, "pbk"),
                "shortId": _q(q, "sid"),
                "spiderX": _q(q, "spx", default="/"),
            }
    elif sec not in ("none", ""):
        raise ValueError(f"unsupported security {sec!r}")

    if scheme == "vless":
        # Post-quantum VLESS carries its parameters in `encryption`
        # (mlkem768x25519plus...); xray refuses "none" for those servers.
        user = {"id": unquote(u.username or ""),
                "encryption": _q(q, "encryption", default="none")}
        flow = _q(q, "flow")
        if flow:
            user["flow"] = flow
        out = {"protocol": "vless", "settings": {"vnext": [{
            "address": u.hostname, "port": u.port, "users": [user]}]}}
    else:
        out = {"protocol": "trojan", "settings": {"servers": [{
            "address": u.hostname, "port": u.port,
            "password": unquote(u.username or "")}]}}

    out["streamSettings"] = stream
    return out


def build_uri(row: dict) -> str:
    """Rebuild a share link from a v2rayN ProfileItem row (trojan/vless, ws/tcp)."""
    extra = json.loads(row.get("TransportExtra") or "{}")
    proto = json.loads(row.get("ProtoExtra") or "{}")
    net = (row.get("Network") or "tcp").lower()
    net = "tcp" if net in ("raw", "tcp") else net
    sec = (row.get("StreamSecurity") or "none").lower()
    params = {"type": net, "security": sec}
    if sec in ("tls", "reality"):
        params["sni"] = row.get("Sni") or row["Address"]
        if row.get("Alpn"):
            params["alpn"] = row["Alpn"]
        if row.get("Fingerprint"):
            params["fp"] = row["Fingerprint"]
        if str(row.get("AllowInsecure")).lower() in ("1", "true"):
            params["allowInsecure"] = "1"
    if sec == "reality":
        for src, dst in (("PublicKey", "pbk"), ("ShortId", "sid"), ("SpiderX", "spx")):
            if row.get(src):
                params[dst] = row[src]
    if net == "ws":
        params["path"] = extra.get("Path") or row.get("Path") or "/"
        params["host"] = extra.get("Host") or row.get("RequestHost") or params.get("sni") or row["Address"]
    elif net == "tcp" and (extra.get("RawHeaderType") or row.get("HeaderType")) == "http":
        params["headerType"] = "http"
        params["path"] = extra.get("Path") or "/"
        params["host"] = extra.get("Host") or row.get("RequestHost") or row["Address"]
    elif net == "grpc":
        params["serviceName"] = extra.get("ServiceName") or ""
    flow = proto.get("Flow") or row.get("Flow")
    if flow:
        params["flow"] = flow

    query = urlencode(params, quote_via=quote)
    remarks = quote((row.get("Remarks") or "").strip(), safe="")
    if row.get("Id"):
        head = f"vless://{quote(row['Id'], safe='')}@{row['Address']}:{row['Port']}"
    else:
        head = f"trojan://{quote(row.get('Password') or '', safe='')}@{row['Address']}:{row['Port']}"
    return f"{head}?{query}#{remarks}"


# ---------------------------------------------------------------- files

def load_pool() -> list[str]:
    if not POOL.exists():
        return []
    out = []
    for line in POOL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def load_domains() -> list[str]:
    if not DOMAINS.exists():
        return []
    out = []
    for line in DOMAINS.read_text(encoding="utf-8").splitlines():
        line = line.strip().lower()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state: dict) -> None:
    HOME.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def key_of(uri: str) -> str:
    # Hash the whole link: these configs share a long identical prefix, so a
    # truncated encoding of the URI collides across the entire pool.
    return hashlib.sha256(uri.encode()).hexdigest()[:16]


# ---------------------------------------------------------------- gateway

def gateway_config(outbound: dict, domains: list[str]) -> dict:
    rules = []
    if domains:
        rules.append({"type": "field",
                      "domain": [f"domain:{d}" for d in domains],
                      "outboundTag": "proxy"})
    rules.append({"type": "field", "network": "tcp,udp", "outboundTag": "direct"})
    return {
        "log": {"loglevel": "warning"},
        "inbounds": [{"tag": "mixed", "listen": "127.0.0.1", "port": gateway_port(),
                      "protocol": "mixed", "settings": {"udp": False}}],
        "outbounds": [dict(outbound, tag="proxy"), {"protocol": "freedom", "tag": "direct"}],
        "routing": {"domainStrategy": "AsIs", "rules": rules},
    }


def gateway_port() -> int:
    return int(os.environ.get("PROXY_TUNNEL_PORT") or 1080)


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def wait_port(port: int, timeout: float = 5.0) -> bool:
    end = time.time() + timeout
    while time.time() < end:
        with socket.socket() as s:
            s.settimeout(0.2)
            if s.connect_ex(("127.0.0.1", port)) == 0:
                return True
        time.sleep(0.05)
    return False


def probe(port: int, timeout: int = SCAN_TIMEOUT, url: str = CANARY) -> tuple[bool, float]:
    """Fetch the canary through a local proxy port; returns (ok, seconds).

    urllib rather than curl: every platform that can run Python has it, and the
    check only needs one HTTPS request through a CONNECT proxy.
    """
    proxy = f"http://127.0.0.1:{port}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    started = time.time()
    try:
        with opener.open(url, timeout=timeout) as response:
            response.read(1024)
            ok = response.status == 200
    except (urllib.error.URLError, http.client.HTTPException, OSError):
        return False, timeout
    return (True, time.time() - started) if ok else (False, timeout)


def probe_best(port: int, attempts: int = 3, timeout: int = GATEWAY_TIMEOUT) -> tuple[float | None, int]:
    """Best latency over a few tries, plus how many failed.

    One reset says nothing here: the same config serves the next request fine.
    """
    best = None
    fails = 0
    for _ in range(attempts):
        ok, secs = probe(port, timeout)
        if ok:
            best = secs if best is None else min(best, secs)
        else:
            fails += 1
    return best, fails


def candidate_probe(uri: str, timeout: int = SCAN_TIMEOUT,
                    attempts: int = 1) -> tuple[bool, float]:
    """Start a throwaway xray for one config and fetch the canary through it.

    These public configs accept a canary and then reset the next connection, so
    a single failure is not proof; report the best of a few attempts.
    """
    port = free_port()
    cfg = {"log": {"loglevel": "error"},
           "inbounds": [{"tag": "mixed", "listen": "127.0.0.1", "port": port,
                         "protocol": "mixed", "settings": {"udp": False}}],
           "outbounds": [dict(parse_uri(uri), tag="proxy")]}
    HOME.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".probe-", suffix=".json", dir=HOME)
    path = Path(name)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh)
    try:
        proc = subprocess.Popen([xray(), "run", "-c", str(path)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        return False, timeout
    try:
        if not wait_port(port):
            return False, timeout
        best = None
        for _ in range(attempts):
            ok, secs = probe(port, timeout)
            if ok:
                best = secs if best is None else min(best, secs)
        return (True, best) if best is not None else (False, timeout)
    finally:
        proc.terminate()
        try:
            proc.wait(2)
        except subprocess.TimeoutExpired:
            proc.kill()
        path.unlink(missing_ok=True)


def port_pids(port: int) -> list[int]:
    """PIDs listening on a local port, best effort per platform."""
    try:
        if IS_WIN:
            out = subprocess.run(["netstat", "-ano", "-p", "tcp"],
                                 capture_output=True, text=True).stdout
            pids = []
            for line in out.splitlines():
                fields = line.split()
                if len(fields) >= 5 and fields[1].endswith(f":{port}") and fields[3] == "LISTENING":
                    pids.append(int(fields[4]))
            return pids
        if sys.platform == "darwin":
            out = subprocess.run(["lsof", "-nP", "-ti", f"tcp:{port}"],
                                 capture_output=True, text=True).stdout
            return [int(value) for value in out.split() if value.isdigit()]
        out = subprocess.run(["ss", "-ltnpH", f"sport = :{port}"],
                             capture_output=True, text=True).stdout
        return [int(match) for match in re.findall(r"pid=(\d+)", out)]
    except (OSError, ValueError):
        return []


def kill_stray_gateway() -> None:
    """A gateway started outside the unit survives a restart and shares the port.

    SO_REUSEPORT lets two xray processes bind 127.0.0.1:1080, silently splitting
    traffic between an old config and the new one.
    """
    if IS_WIN:
        if port_pids(gateway_port()):
            print(f"port {gateway_port()} is already in use by another program", file=sys.stderr)
        return
    for pid in port_pids(gateway_port()):
        try:
            if sys.platform.startswith("linux"):
                cmdline = Path(f"/proc/{pid}/cmdline").read_bytes().replace(b"\0", b" ").decode()
            else:
                cmdline = subprocess.run(["ps", "-p", str(pid), "-o", "comm="],
                                         capture_output=True, text=True).stdout
        except OSError:
            continue
        if "xray" in cmdline:
            try:
                os.kill(pid, signal.SIGTERM)
            except OSError:
                pass


def _spawn_flags() -> dict:
    if IS_WIN:
        flags = getattr(subprocess, "DETACHED_PROCESS", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
        return {"creationflags": flags}
    return {"start_new_session": True}


def rotate_log(max_bytes: int = LOG_MAX_BYTES, keep_lines: int = LOG_KEEP_LINES) -> bool:
    """Cap gateway.log, keeping the tail in gateway.log.1.

    xray inherits a descriptor opened with O_APPEND, so truncating the file here is
    safe: its next write lands at the new end of file instead of leaving a hole.
    Returns True when a rotation happened.
    """
    try:
        size = GATEWAY_LOG.stat().st_size
    except OSError:
        return False
    if size <= max_bytes:
        return False
    with open(GATEWAY_LOG, "rb") as fh:
        fh.seek(max(0, size - 256_000))
        tail = fh.read().decode("utf-8", "replace").splitlines()[-keep_lines:]
    LOG_BACKUP.write_text("\n".join(tail) + "\n", encoding="utf-8")
    with open(GATEWAY_LOG, "r+b") as fh:
        fh.truncate(0)
    return True


def start_gateway(outbound: dict, domains: list[str]) -> int:
    stop_gateway(quiet=True)
    kill_stray_gateway()
    HOME.mkdir(parents=True, exist_ok=True)
    GATEWAY.write_text(json.dumps(gateway_config(outbound, domains), indent=2), encoding="utf-8")
    rotate_log()
    log = open(GATEWAY_LOG, "ab")
    proc = subprocess.Popen([xray(), "run", "-c", str(GATEWAY)],
                            stdout=log, stderr=log, **_spawn_flags())
    PIDFILE.write_text(str(proc.pid), encoding="utf-8")
    if not wait_port(gateway_port()):
        stop_gateway(quiet=True)
        sys.exit(f"gateway did not come up; see {GATEWAY_LOG}")
    return proc.pid


def gateway_pid() -> int | None:
    try:
        pid = int(PIDFILE.read_text().strip())
    except (FileNotFoundError, ValueError):
        return None
    try:
        os.kill(pid, 0)
    except OSError:
        return None
    return pid


def stop_gateway(quiet: bool = False) -> None:
    pid = gateway_pid()
    if not pid:
        PIDFILE.unlink(missing_ok=True)
        return
    if IS_WIN:
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True)
    else:
        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except OSError:
            pass
    for _ in range(20):
        if not gateway_pid():
            break
        time.sleep(0.1)
    PIDFILE.unlink(missing_ok=True)
    if not quiet:
        print("gateway stopped")


# ---------------------------------------------------------------- selection

def mark_dead(state: dict, key: str) -> None:
    dead = state.setdefault("dead", {})
    dead[key] = int(time.time()) + DEAD_COOLDOWN


def candidates(state: dict, limit: int | None = None,
               workers: int = 1) -> "list[tuple[int, str, float]]":
    """Yield working configs in pool order, so the caller can stop at the first one.

    The default is sequential: these configs often share one backend, and probing
    several at once trips its rate limit into false failures.
    """
    pool = load_pool()
    if not pool:
        sys.exit(f"pool is empty: {POOL} (run: tunnel.py setup, or paste links into it)")
    now = int(time.time())
    dead = state.get("dead", {})
    if dead and all(dead.get(key_of(uri), 0) > now for uri in pool):
        # The whole pool is cooling down: a cooldown must never hide every option,
        # or a burst of failures would leave the tunnel unrecoverable for minutes.
        dead = state["dead"] = {}
        save_state(state)
    tried = 0

    def attempt(item: tuple[int, str]):
        # A failed probe is not a verdict here: the same config answers the next
        # request. Move on to the next candidate instead of cooling this one down.
        idx, uri = item
        ok, secs = candidate_probe(uri)
        return (idx, uri, secs) if ok else None

    if workers <= 1:
        for idx, uri in enumerate(pool):
            if dead.get(key_of(uri), 0) > now:
                continue
            if limit and tried >= limit:
                return
            tried += 1
            found = attempt((idx, uri))
            if found:
                yield found
        return

    start = 0
    while start < len(pool):
        window = [(i, pool[i]) for i in range(start, min(start + workers, len(pool)))
                  if dead.get(key_of(pool[i]), 0) <= now]
        if window:
            with ThreadPoolExecutor(max_workers=len(window)) as pool_exec:
                found = [r for r in pool_exec.map(attempt, window) if r]
            tried += len(window)
            if found:
                yield from sorted(found)
                return
            if limit and tried >= limit:
                return
        start += workers


def apply_config(uri: str, secs: float, idx: int, state: dict) -> None:
    """Write the gateway with this config and prove it still works through it."""
    start_gateway(parse_uri(uri), load_domains())
    for _ in range(3):
        ok, _lat = probe(gateway_port(), timeout=GATEWAY_TIMEOUT)
        if ok:
            state["last_good"] = {"uri": uri, "key": key_of(uri), "index": idx,
                                  "latency_s": round(secs, 2), "at": int(time.time())}
            save_state(state)
            return
        time.sleep(0.4)
    raise RuntimeError(f"config #{idx} failed through the gateway")


# ---------------------------------------------------------------- commands

def seed_pool(db: Path, group: str, force: bool = False) -> int:
    """Rewrite pool.txt from a v2rayN database; returns how many links were written."""
    import sqlite3

    if not db.is_file():
        sys.exit(f"v2rayN database not found: {db}")
    if POOL.exists() and not force:
        sys.exit(f"{POOL} already exists; pass --force to overwrite")
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "select p.* from ProfileItem p join SubItem s on p.Subid = s.Id "
        "where s.Remarks = ? order by p.IndexId", (group,)).fetchall()
    if not rows:
        sys.exit(f"group {group!r} has no configs in {db}")

    uris, skipped = [], 0
    for row in rows:
        try:
            uris.append(build_uri(dict(row)))
        except (ValueError, KeyError):
            skipped += 1
    HOME.mkdir(parents=True, exist_ok=True)
    POOL.write_text("\n".join(uris) + "\n", encoding="utf-8")
    if not DOMAINS.exists():
        DOMAINS.write_text("\n".join(SEED_DOMAINS) + "\n", encoding="utf-8")
    print(f"wrote {len(uris)} configs to {POOL}" + (f" ({skipped} skipped)" if skipped else ""))
    return len(uris)


def cmd_seed(args: argparse.Namespace) -> None:
    db = Path(args.db).expanduser() if args.db else v2rayn_db()
    if db is None:
        sys.exit(f"no v2rayN install found; pass --db PATH, or paste share links into {POOL}")
    seed_pool(db, args.group, args.force)
    print(f"domains: {DOMAINS} ({len(load_domains())} entries)")


def cmd_setup(args: argparse.Namespace) -> None:
    """One command that makes a fresh machine usable: binary, pool, wrapper, service."""
    HOME.mkdir(parents=True, exist_ok=True)
    binary = xray()
    print(f"xray      : {binary}")

    if not POOL.exists():
        db = Path(args.db).expanduser() if args.db else v2rayn_db()
        if db is not None and db.is_file():
            seed_pool(db, args.group, force=True)
        else:
            POOL.write_text("", encoding="utf-8")
            print(f"pool      : empty. Paste vless:// or trojan:// links into {POOL} (best first)")
    else:
        print(f"pool      : {len(load_pool())} configs in {POOL}")

    if not DOMAINS.exists():
        DOMAINS.write_text("\n".join(SEED_DOMAINS) + "\n", encoding="utf-8")
    print(f"domains   : {len(load_domains())} routed through the tunnel")

    cmd_install_wrapper(args)
    if getattr(args, "service", False):
        if sys.platform.startswith("linux") and shutil.which("systemctl"):
            cmd_install_service(argparse.Namespace(interval=args.interval))
        else:
            print("service   : no systemd here. Start the supervisor yourself:")
            print(f"            {sys.executable} {Path(__file__).resolve()} serve --interval 60")
    else:
        print("service   : not installed (setup leaves the system alone).")
        print("            optional supervisor: tunnel.py install-service")
    print()
    print("next      : tunnel.py up   then   tunnel.py doctor")


def service_active() -> bool:
    """True when the systemd user unit supervises the gateway (it owns the process)."""
    try:
        out = subprocess.run(["systemctl", "--user", "is-active", "proxy-tunnel.service"],
                             capture_output=True, text=True)
    except OSError:
        return False
    return out.stdout.strip() == "active"


def restart_service() -> bool:
    if not service_active():
        return False
    subprocess.run(["systemctl", "--user", "restart", "proxy-tunnel.service"], check=False)
    return wait_port(gateway_port(), timeout=15)


def cmd_up(args: argparse.Namespace) -> None:
    internal = getattr(args, "internal", False)
    unit = Path.home() / ".config/systemd/user/proxy-tunnel.service"
    if unit.exists() and not internal:
        # The unit owns xray; launching it here would put a second gateway on the
        # port (SO_REUSEPORT) and leave a process outside the unit's cgroup.
        if args.refresh:
            state = load_state()
            key = (state.get("last_good") or {}).get("key")
            state.pop("last_good", None)
            if key:
                mark_dead(state, key)
            save_state(state)
        verb = "restart" if service_active() else "start"
        subprocess.run(["systemctl", "--user", verb, "proxy-tunnel.service"], check=False)
        if not wait_port(gateway_port(), timeout=20):
            sys.exit("proxy-tunnel.service did not come up; check: journalctl --user -u proxy-tunnel")
        idx = None
        for _ in range(30):
            idx = (load_state().get("last_good") or {}).get("index")
            if idx is not None:
                break
            time.sleep(0.5)
        label = f" (config #{idx})" if idx is not None else ""
        print(f"gateway up on 127.0.0.1:{gateway_port()} via proxy-tunnel.service{label}")
        return
    state = load_state()
    last = state.get("last_good") or {}
    if last.get("uri") and not args.refresh:
        ok, secs = candidate_probe(last["uri"], timeout=GATEWAY_TIMEOUT, attempts=2)
        if ok:
            try:
                apply_config(last["uri"], secs, last.get("index", -1), state)
                print(f"gateway up on 127.0.0.1:{gateway_port()} with last-good config")
                return
            except RuntimeError:
                mark_dead(state, key_of(last["uri"]))
                save_state(state)
    for idx, uri, secs in candidates(state, limit=args.limit, workers=args.workers):
        try:
            apply_config(uri, secs, idx, state)
        except RuntimeError:
            mark_dead(state, key_of(uri))
            save_state(state)
            continue
        print(f"gateway up on 127.0.0.1:{gateway_port()} with config #{idx} ({secs:.2f}s)")
        return
    stop_gateway(quiet=True)
    sys.exit("no config in the pool could open the canary; pool may be stale (reseed it)")


def cmd_down(args: argparse.Namespace) -> None:
    if service_active():
        subprocess.run(["systemctl", "--user", "stop", "proxy-tunnel.service"], check=False)
    stop_gateway()


def cmd_status(args: argparse.Namespace) -> None:
    state = load_state()
    last = state.get("last_good") or {}
    pid = gateway_pid()
    print(f"gateway : {'running pid ' + str(pid) if pid else 'stopped'} on 127.0.0.1:{gateway_port()}")
    if pid:
        best, fails = probe_best(gateway_port())
        if best is None:
            print("canary  : FAILED (0/3)")
        else:
            print(f"canary  : ok {best:.2f}s ({fails}/3 resets)")
    if last:
        age = int(time.time()) - int(last.get("at", 0))
        print(f"last good: config #{last.get('index')} ({last.get('latency_s')}s, {age}s ago)")
        try:
            host = urlparse(last["uri"]).hostname
            print(f"          {host}  {last['uri'][:40]}...")
        except KeyError:
            pass
    print(f"pool    : {len(load_pool())} configs in {POOL}")
    print(f"domains : {len(load_domains())} routed via tunnel")
    try:
        print(f"log     : {GATEWAY_LOG.stat().st_size / 1024:.0f} KB (cap {LOG_MAX_BYTES / 1e6:.0f} MB)")
    except OSError:
        pass


def cmd_list(args: argparse.Namespace) -> None:
    pool = load_pool()
    state = load_state()
    dead = state.get("dead", {})
    now = int(time.time())
    for idx, uri in enumerate(pool):
        key = key_of(uri)
        cooling = dead.get(key, 0) > now
        try:
            u = urlparse(uri)
            host = f"{u.hostname}:{u.port}"
        except ValueError:
            host = "?"
        mark = "dead" if cooling else "   "
        print(f"{idx:3d} {mark} {u.scheme:6s} {host:45s} {unquote(u.fragment)[:40]}")


def cmd_allow(args: argparse.Namespace) -> None:
    domains = load_domains()
    added = [d.strip().lower() for d in args.domains if d.strip().lower() not in domains]
    if added:
        domains.extend(added)
        DOMAINS.write_text("\n".join(domains) + "\n", encoding="utf-8")
        print("added: " + ", ".join(added))
        if service_active():
            if restart_service():
                print("gateway reloaded via proxy-tunnel.service")
        elif gateway_pid():
            state = load_state()
            last = state.get("last_good")
            if last:
                start_gateway(parse_uri(last["uri"]), domains)
                print("gateway reloaded")
    else:
        print("already allowed")


def cmd_disallow(args: argparse.Namespace) -> None:
    domains = load_domains()
    keep = [d for d in domains if d not in args.domains]
    DOMAINS.write_text("\n".join(keep) + "\n", encoding="utf-8")
    print(f"removed {len(domains) - len(keep)} domain(s)")
    if service_active():
        restart_service()
    elif gateway_pid():
        last = (load_state().get("last_good") or {}).get("uri")
        if last:
            start_gateway(parse_uri(last), keep)
            print("gateway reloaded")


def cmd_domains(args: argparse.Namespace) -> None:
    for d in load_domains():
        print(d)


def cmd_fetch(args: argparse.Namespace) -> None:
    if not gateway_pid():
        sys.exit("gateway is stopped; run: tunnel.py up")
    proxy = f"http://127.0.0.1:{gateway_port()}"
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    try:
        with opener.open(args.url, timeout=args.timeout) as response:
            status = response.status
            body = response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        status = exc.code
        body = exc.read().decode("utf-8", "replace")
    except (urllib.error.URLError, http.client.HTTPException, OSError) as exc:
        sys.exit(f"fetch failed: {exc}")
    if args.raw:
        sys.stdout.write(body)
        return
    print(f"{status} {len(body)} bytes")
    print(body[: args.max_chars])


def cmd_env(args: argparse.Namespace) -> None:
    port = gateway_port()
    print(f"export URL_READER_HTTPS_PROXY=http://127.0.0.1:{port}")
    print(f"export URL_READER_HTTP_PROXY=http://127.0.0.1:{port}")
    print("export NO_PROXY=localhost,127.0.0.1,::1")
    print()
    print("MCP server env (JSON):")
    print(json.dumps({"URL_READER_HTTPS_PROXY": f"http://127.0.0.1:{port}",
                      "URL_READER_HTTP_PROXY": f"http://127.0.0.1:{port}",
                      "NO_PROXY": "localhost,127.0.0.1,::1"}, indent=2))
    print()
    print("Playwright MCP arg: --proxy-server=http://127.0.0.1:" + str(port))


def cmd_serve(args: argparse.Namespace) -> None:
    """Supervisor: keep the gateway alive and rotate configs when the tunnel dies."""
    state = load_state()
    failures = 0
    first = True
    while True:
        # Always (re)start on entry: a gateway left by an earlier run may still hold
        # the port from outside this unit's cgroup.
        if first or not gateway_pid():
            first = False
            failures = 0
            try:
                cmd_up(argparse.Namespace(refresh=False, limit=None, workers=1, internal=True))
            except SystemExit as exc:
                print(f"start failed: {exc}", file=sys.stderr)
                time.sleep(15)
                continue
        best, _fails = probe_best(gateway_port(), attempts=2)
        if best is not None:
            failures = 0
        else:
            failures += 1
            print(f"canary failed ({failures})", file=sys.stderr)
            if failures >= 3:
                state = load_state()
                key = (state.get("last_good") or {}).get("key")
                if key:
                    mark_dead(state, key)
                    save_state(state)
                try:
                    cmd_up(argparse.Namespace(refresh=True, limit=None, workers=1, internal=True))
                except SystemExit as exc:
                    print(f"rotate failed: {exc}", file=sys.stderr)
                failures = 0
        if rotate_log():
            print(f"rotated gateway.log past {LOG_MAX_BYTES} bytes into {LOG_BACKUP.name}",
                  file=sys.stderr)
        time.sleep(args.interval)


UNIT = """[Unit]
Description=proxy-tunnel gateway (domain-split HTTP proxy over VLESS/Trojan pool)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart={python} {script} serve --interval {interval}
Restart=always
RestartSec=5
Environment=PROXY_TUNNEL_PORT={port}
Environment=PROXY_TUNNEL_HOME={home}
Environment=PROXY_TUNNEL_CANARY={canary}
Environment=PATH={path}

[Install]
WantedBy=default.target
"""


WRAPPER = Path.home() / ".local" / "bin" / "proxy-tunnel-exec"


def cmd_pause(args: argparse.Namespace) -> None:
    state = load_state()
    state["paused"] = True
    save_state(state)
    print("tunnel paused: new launcher runs go direct (the gateway keeps running)")


def cmd_resume(args: argparse.Namespace) -> None:
    state = load_state()
    state["paused"] = False
    save_state(state)
    print("tunnel resumed")


def cmd_install_wrapper(args: argparse.Namespace) -> None:
    src = Path(__file__).resolve().parent / "launch.py"
    src.chmod(0o755)
    if IS_WIN:
        shim = WRAPPER.with_suffix(".cmd")
        shim.parent.mkdir(parents=True, exist_ok=True)
        shim.write_text(f'@echo off\r\n"{sys.executable}" "{src}" %*\r\n', encoding="utf-8")
        print(f"installed {shim}")
        print(f"add {shim.parent} to PATH if it is not there already")
        return
    WRAPPER.parent.mkdir(parents=True, exist_ok=True)
    if WRAPPER.is_symlink() or WRAPPER.exists():
        WRAPPER.unlink()
    WRAPPER.symlink_to(src)
    print(f"installed {WRAPPER} -> {src}")


def cmd_doctor(args: argparse.Namespace) -> None:
    """Report every link the tunnel needs, so drift is visible in one command."""
    problems = 0

    def line(ok: bool, text: str) -> None:
        nonlocal problems
        problems += 0 if ok else 1
        print(f"{'ok  ' if ok else 'FAIL'} {text}")

    pool = load_pool()
    line(bool(pool), f"pool: {len(pool)} configs in {POOL}")
    line(DOMAINS.exists(), f"domains: {len(load_domains())} routed through the tunnel")

    unit = Path.home() / ".config/systemd/user/proxy-tunnel.service"
    # The service is optional: `setup` deliberately installs none. Report its
    # absence as a note instead of failing an otherwise healthy manual setup.
    if unit.exists():
        line(service_active(), f"service active: {unit}")
    else:
        print("note service unit not installed (optional; run `serve` or use "
              "`setup --service` on Linux)")
    if service_active():
        best, fails = probe_best(gateway_port())
        line(best is not None, f"gateway canary: {'%.2fs' % best if best else 'FAILED'} ({fails}/3 resets)")

    line(WRAPPER.exists() and os.access(WRAPPER, os.X_OK), f"launcher: {WRAPPER}")
    if load_state().get("paused"):
        print("note tunnel is paused; launchers run direct until `resume`")

    # Client wiring is checked only where it already exists: a client that never
    # used the tunnel is not a failure, but a half-wired one is. The list is a set
    # of common clients, not a requirement — add your own config here if it differs.
    wired_any = False
    for config, name in ((Path.home() / ".dsh" / "cordis.patch.yml", "dsh"),
                         (Path.home() / ".config" / "opencode" / "opencode.json", "opencode"),
                         (Path.home() / ".claude.json", "Claude Code"),
                         (Path.home() / ".cursor" / "mcp.json", "Cursor")):
        if not config.is_file():
            continue
        text = config.read_text(encoding="utf-8", errors="replace")
        wired = "proxy-tunnel-exec" in text
        leftover = "URL_READER_HTTPS_PROXY" in text
        if not (wired or leftover):
            continue
        wired_any = wired_any or wired
        line(wired, f"{name} config runs MCP servers through the launcher")
        line(not leftover, f"{name} config carries no proxy variables of its own")

    if not wired_any:
        # A gateway nobody points at looks healthy here and does nothing for fetches,
        # so say it rather than leaving a silent all-ok report.
        print("note no known client config points at the launcher yet: each MCP server "
              "or fetch tool needs its command changed once — see references/setup.md. "
              "Ignore this if that client passes `tunnel.py env` variables instead.")

    sys.exit(1 if problems else 0)


def cmd_install_service(args: argparse.Namespace) -> None:
    if not (sys.platform.startswith("linux") and shutil.which("systemctl")):
        sys.exit("no systemd here; run `tunnel.py serve` under your platform's own "
                 "supervisor (launchd, Task Scheduler) or in a terminal")
    unit_dir = Path.home() / ".config/systemd/user"
    unit_dir.mkdir(parents=True, exist_ok=True)
    unit = unit_dir / "proxy-tunnel.service"
    unit.write_text(UNIT.format(python=sys.executable, script=Path(__file__).resolve(),
                                interval=args.interval, port=gateway_port(),
                                home=HOME, canary=CANARY,
                                path=os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin")),
                    encoding="utf-8")
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "--user", "enable", "--now", "proxy-tunnel.service"], check=True)
    print(f"installed {unit} and started it")


def cmd_uninstall_service(args: argparse.Namespace) -> None:
    subprocess.run(["systemctl", "--user", "disable", "--now", "proxy-tunnel.service"],
                   check=False)
    (Path.home() / ".config/systemd/user/proxy-tunnel.service").unlink(missing_ok=True)
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=False)
    print("service removed")


def main() -> None:
    parser = argparse.ArgumentParser(prog="tunnel.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("setup", help="install the binary, seed the pool, wire the launcher")
    p.add_argument("--db", help="path to v2rayN's guiNDB.db")
    p.add_argument("--group", default="good")
    p.add_argument("--interval", type=int, default=60)
    p.add_argument("--service", action="store_true",
                   help="also install and start the systemd user unit (Linux only)")
    p.set_defaults(func=cmd_setup)

    p = sub.add_parser("seed", help="fill pool.txt from v2rayN or a share-link file")
    p.add_argument("--group", default="good", help="v2rayN subscription group (default: good)")
    p.add_argument("--db", help="path to guiNDB.db")
    p.add_argument("--force", action="store_true", help="overwrite an existing pool")
    p.set_defaults(func=cmd_seed)

    p = sub.add_parser("up", help="start the gateway with the best config")
    p.add_argument("--refresh", action="store_true", help="skip the last-good config and rescan")
    p.add_argument("--limit", type=int, help="stop scanning after N attempts")
    p.add_argument("--workers", type=int, default=1,
                   help="parallel probes (default 1: parallel trips the shared backend)")
    p.set_defaults(func=cmd_up)

    sub.add_parser("down", help="stop the gateway").set_defaults(func=cmd_down)
    sub.add_parser("status", help="show gateway and pool state").set_defaults(func=cmd_status)
    sub.add_parser("list", help="list pool configs").set_defaults(func=cmd_list)
    sub.add_parser("domains", help="list tunneled domains").set_defaults(func=cmd_domains)
    sub.add_parser("env", help="print proxy env for MCP servers and browsers").set_defaults(func=cmd_env)

    p = sub.add_parser("allow", help="route domains through the tunnel")
    p.add_argument("domains", nargs="+")
    p.set_defaults(func=cmd_allow)

    p = sub.add_parser("disallow", help="stop routing domains through the tunnel")
    p.add_argument("domains", nargs="+")
    p.set_defaults(func=cmd_disallow)

    p = sub.add_parser("fetch", help="fetch a URL through the gateway")
    p.add_argument("url")
    p.add_argument("--raw", action="store_true", help="print the body only")
    p.add_argument("--max-chars", type=int, default=20000)
    p.add_argument("--timeout", type=int, default=40)
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("serve", help="supervise the gateway and rotate dead configs")
    p.add_argument("--interval", type=int, default=60)
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("install-service", help="install and start the systemd user unit")
    p.add_argument("--interval", type=int, default=60)
    p.set_defaults(func=cmd_install_service)

    sub.add_parser("uninstall-service", help="remove the systemd user unit").set_defaults(
        func=cmd_uninstall_service)

    sub.add_parser("pause", help="make launchers run direct until resume").set_defaults(func=cmd_pause)
    sub.add_parser("resume", help="let launchers use the tunnel again").set_defaults(func=cmd_resume)
    sub.add_parser("install-wrapper", help="install the proxy-tunnel-exec launcher").set_defaults(
        func=cmd_install_wrapper)
    sub.add_parser("doctor", help="check pool, service, launcher, and client wiring").set_defaults(
        func=cmd_doctor)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
