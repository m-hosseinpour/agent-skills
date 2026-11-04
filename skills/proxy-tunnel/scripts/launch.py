#!/usr/bin/env python3
"""Launch a command with the proxy-tunnel gateway applied only when it is healthy.

MCP servers read their proxy settings from the environment at startup, so the
proxy has to be injected by whatever launches them. Putting that decision here
instead of in the client's config means the config never has to change when the
port moves, when the tunnel is paused, or when the gateway is down.

Usage:
  proxy-tunnel-exec [--url-reader|--global|--playwright|--none] -- <command> [args...]

Profiles:
  --url-reader   set URL_READER_HTTP(S)_PROXY (mcp-searxng's scoped settings)
  --global       also set HTTP_PROXY/HTTPS_PROXY for servers that only read those
  --playwright   append --proxy-server/--proxy-bypass to the browser server's args
  --none         never inject a proxy

When the gateway is not listening, or the tunnel is paused, inherited proxy
variables are dropped and the command runs direct.
"""

import json
import os
import socket
import sys
from pathlib import Path

HOME = Path(os.environ.get("PROXY_TUNNEL_HOME") or Path.home() / ".config" / "proxy-tunnel")
PORT = int(os.environ.get("PROXY_TUNNEL_PORT") or 1080)
PROXY_VARS = ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy",
              "URL_READER_HTTP_PROXY", "URL_READER_HTTPS_PROXY")
PROFILES = {"url-reader": "url-reader", "global": "global",
            "playwright": "playwright", "none": "none"}


def gateway_up() -> bool:
    sock = socket.socket()
    sock.settimeout(0.2)
    try:
        return sock.connect_ex(("127.0.0.1", PORT)) == 0
    finally:
        sock.close()


def paused() -> bool:
    try:
        return bool(json.loads((HOME / "state.json").read_text(encoding="utf-8")).get("paused"))
    except (OSError, ValueError):
        return False


def main() -> None:
    args = sys.argv[1:]
    profile = "global"
    while args and args[0].startswith("--"):
        flag = args.pop(0)
        if flag == "--":
            break
        name = flag[2:]
        if name not in PROFILES:
            sys.exit(f"unknown flag {flag}")
        profile = PROFILES[name]
    if not args:
        sys.exit("usage: proxy-tunnel-exec [--url-reader|--global|--playwright|--none] -- <command> [args...]")

    env = dict(os.environ)
    for key in PROXY_VARS:
        env.pop(key, None)

    url = f"http://127.0.0.1:{PORT}"
    use = profile != "none" and not paused() and gateway_up()

    if use:
        if profile in ("url-reader", "global"):
            env["URL_READER_HTTP_PROXY"] = url
            env["URL_READER_HTTPS_PROXY"] = url
        if profile == "global":
            for key in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
                env[key] = url
        env.setdefault("NO_PROXY", "localhost,127.0.0.1,::1")
        if profile == "playwright":
            args += [f"--proxy-server={url}", "--proxy-bypass=localhost,127.0.0.1"]

    try:
        os.execvpe(args[0], args, env)
    except FileNotFoundError:
        sys.exit(f"command not found: {args[0]}")


if __name__ == "__main__":
    main()
