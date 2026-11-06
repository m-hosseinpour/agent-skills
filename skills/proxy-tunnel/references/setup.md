# Setup, wiring, and troubleshooting

Most of this is optional for daily use, with one exception: **each fetch client has to be
pointed at the wrapper once** (see [Wiring a fetch tool](#wiring-a-fetch-tool)). After
that, `SKILL.md` is enough. Read this when installing, moving to another agent or client,
or fixing a broken tunnel.

## Requirements

- **Python 3.8+**. macOS and most Linux distributions ship it; on Windows use
  `winget install Python.Python.3.12` (or python.org) and make sure `python` works.
- **Network access to GitHub on the first run**, to fetch xray (≈17 MB). After that the
  binary is cached and no download happens.
- **No v2rayN needed.** When it is installed, the skill reuses both its database and its
  bundled xray; when it is not, xray comes from the official release and the pool is
  filled by pasting share links.
- **Your own configs.** The skill ships no share links: the pool is filled from a local
  v2rayN database or from `vless://` / `trojan://` links you paste into `pool.txt`. With
  an empty pool the gateway cannot start.
- **Tested on Linux.** The macOS and Windows branches (data dir, launcher shim, PATH
  notes) follow the same code paths but have not been exercised.

## First run, any OS

Run these from this skill's directory, or use the absolute path to
`scripts/tunnel.py`:

```bash
python3 scripts/tunnel.py setup          # xray + pool + launcher; touches nothing else
python3 scripts/tunnel.py up             # pick a config and start the gateway
python3 scripts/tunnel.py doctor         # required lines should say ok; optional service is a note
```

`setup` is idempotent: it downloads xray only if no binary is found, seeds the pool only
if `pool.txt` is missing, and reinstalls the launcher each time. It deliberately installs
no background service; add `--service` (Linux/systemd) when you want the supervisor that
rotates dead configs on its own. It also never edits an agent's config — that edit is
yours to make, once per MCP server, as described under
[Wiring a fetch tool](#wiring-a-fetch-tool).

Data lives in the platform config directory (override with `PROXY_TUNNEL_HOME`):

| OS | directory |
|---|---|
| Linux | `~/.config/proxy-tunnel` |
| macOS | `~/Library/Application Support/proxy-tunnel` |
| Windows | `%APPDATA%\proxy-tunnel` |

with `pool.txt`, `domains.txt`, `state.json`, `gateway.log`, and the cached xray under
`bin/xray-<version>/`.

### Where xray comes from

1. `XRAY_BIN`, if set.
2. `xray` on `PATH`.
3. v2rayN's bundled binary (`bin/xray/xray` or `xray.exe` under its data dir).
4. The cached download in `bin/`.
5. Otherwise the default pinned release (`XRAY_VERSION`, currently `26.10.31`) is
   fetched, its SHA-256 checked against the release `.dgst`, and unpacked into `bin/`.
   If that tag returns 404, the latest published release is resolved from the GitHub
   API and used instead, so an outdated pin does not break a fresh install.

Pin a different release with `XRAY_VERSION=...` when a newer one misbehaves.

The gateway's canary — the URL that proves a config works — defaults to
`https://www.youtube.com/`. Override it with `PROXY_TUNNEL_CANARY` when that host is
reachable directly in your network, or blocked for a reason unrelated to the tunnel. The
generated systemd unit records the value it saw, so rerun `install-service` after
changing it.

### Filling the pool

If v2rayN is present, `setup` (or `seed --group good`) reads
`guiConfigs/guiNDB.db` and writes one share link per line in database order. Otherwise
paste `vless://…` / `trojan://…` links into `pool.txt`, best first; lines starting with
`#` are ignored. The parser understands ws, grpc, xhttp, and tcp+http-header transports
with tls/reality/none, plus `flow`, `sni`, `alpn`, `fp`, `pbk`, `sid`, `spx`, and the
post-quantum VLESS `encryption` value (`mlkem768x25519plus…`).

Point `--db` at another location when v2rayN stores its data elsewhere; the skill only
auto-detects the default per platform.

### Windows notes

- The launcher installs as `%USERPROFILE%\.local\bin\proxy-tunnel-exec.cmd` (the
  installer prints the exact path); add that directory to `PATH`, or reference
  `launch.py` directly in the client config
  (`command: python`, `args: ['C:\\path\\to\\launch.py', '--url-reader', ...]`).
- There is no systemd. Run `python tunnel.py serve --interval 60` in a terminal, or let
  the client start the gateway with `up`; the supervisor is only needed for automatic
  rotation.
- The gateway still listens on loopback only, so the Windows firewall needs no rule.

## Wiring a fetch tool

The gateway speaks HTTP proxy (and SOCKS5) on `127.0.0.1:1080`. Rather than baking the
proxy into each client's config, launch the client through the wrapper:

```bash
python3 scripts/tunnel.py install-wrapper     # ~/.local/bin/proxy-tunnel-exec
```

**This is a per-server edit, and it is required.** Every MCP server that fetches pages —
a URL reader, Playwright, a browser tool — keeps its own command and args, and gets the
wrapper in front plus one profile flag. Nothing else in the config changes, and servers
that only call a local service (a search server, for example) need no edit at all. Reuse
the original command and args verbatim after the flag:

```yaml
# original: npx -y mcp-searxng
command: proxy-tunnel-exec
args: ['--url-reader', 'npx', '-y', 'mcp-searxng']

# original: npx -y @playwright/mcp@latest --browser=chromium
command: proxy-tunnel-exec
args: ['--playwright', 'npx', '-y', '@playwright/mcp@latest', '--browser=chromium']
```

Restart the agent or harness after the edit: an MCP server started from the old config
keeps running direct until it is relaunched. `tunnel.py doctor` says so when no known
client config mentions the launcher yet.

Where that block goes depends on the client. These two are examples with the fields each
client takes; the tool names are illustrative, not required:

```jsonc
// opencode — ~/.config/opencode/opencode.json
"mcp": { "servers": { "searxng": {
  "type": "local",
  "command": ["/home/you/.local/bin/proxy-tunnel-exec", "--url-reader", "npx", "-y", "mcp-searxng"],
  "environment": { "SEARXNG_URL": "http://127.0.0.1:7964" }
} } }
```

```jsonc
// Claude Code — ~/.claude.json
"mcpServers": { "searxng": {
  "type": "stdio",
  "command": "/home/you/.local/bin/proxy-tunnel-exec",
  "args": ["--url-reader", "npx", "-y", "mcp-searxng"],
  "env": { "SEARXNG_URL": "http://127.0.0.1:7964" }
} }
```

Use the absolute path to the launcher when the client cannot rely on `PATH` — common for
GUI-launched apps and on Windows. Any other client that takes a command, args and env
follows the same pattern; only the launcher's profile flag differs.

Profiles: `--url-reader` sets `URL_READER_HTTP(S)_PROXY`, `--global` also sets
`HTTP(S)_PROXY`, `--playwright` appends `--proxy-server`/`--proxy-bypass`, `--none`
never injects.

Why a launcher rather than an `env` block: the launcher decides at each launch whether
the gateway is listening and whether the tunnel is paused, and it falls back to direct
when either is false. Nothing in the client config mentions a port or a proxy, so a
port change, a paused tunnel, or a dead gateway never needs a config edit. `pause` and
`resume` flip that decision at runtime:

```bash
python3 scripts/tunnel.py pause     # next launches run direct; gateway keeps running
python3 scripts/tunnel.py resume
```

`tunnel.py doctor` checks the pool, the service, the launcher, and any client config it
recognizes that already mentions the launcher, so a silent mis-wiring shows up as `FAIL`
instead of a mysterious fetch error.

**Clients that cannot change their command** can still take raw variables from
`tunnel.py env` (`URL_READER_HTTPS_PROXY`, `URL_READER_HTTP_PROXY`, `NO_PROXY`). They
carry the same values, with none of the fallback. mcp-searxng accepts only `http://`
and `https://` proxies — a `socks5://` value is rejected, which is why the gateway
exposes a mixed port.

**Search is not routed.** A search tool that only calls a local service (a local
SearXNG, for instance) gains nothing from the hop: results and latency stay the same, and
it breaks whenever the gateway is down. Leave the search tool's proxy settings unset.

**Anything with curl:** `curl -x http://127.0.0.1:1080 <url>`, or `tunnel.py fetch <url>`.

Do not set `HTTPS_PROXY` globally in the shell or in the harness process: that routes
every request, including pages reachable directly, and a dead pool then looks like a
dead network.

## Running as a service

`setup` never installs one; opt in explicitly when you want the supervisor that rotates
dead configs. Linux (systemd user unit, `Restart=always`):

```bash
python3 scripts/tunnel.py install-service
systemctl --user status proxy-tunnel
journalctl --user -u proxy-tunnel -f
python3 scripts/tunnel.py uninstall-service
```

macOS and Windows have no equivalent here: run `serve` in a terminal, or add the same
command to launchd / Task Scheduler yourself. Without a supervisor the gateway still
works; it just will not rotate a dead config on its own.

The service runs `serve`: it restarts the gateway if xray dies, probes the canary every
60 s, and rotates to the next working config after three consecutive failed checks.
Rotation is deliberately slow — these configs reset occasionally and a rotation on the
first blip would thrash.

## How a config is chosen

1. The last config that passed the canary is tried first (`state.json`).
2. Otherwise `pool.txt` is probed from the top, one at a time, until one opens the
   canary; that one starts the gateway and is then verified through the gateway.
3. Failures during rotation cool a config down for 60 s. A whole-pool cooldown is
   cleared rather than reporting "no config".
4. `up --refresh` skips step 1.

Probing is sequential by default on purpose: the pool usually points at one backend,
and parallel probes trip its rate limit and produce false failures. `--workers N`
exists for pools with independent servers.

## Sites these exits do not unlock

Reachability through the tunnel was measured with a browser user agent on one datacenter
exit (Frankfurt); some sites refuse datacenter addresses regardless of block lists.
Treat the table as a snapshot: your configs exit somewhere else, so results differ.

| Site | Direct | Through tunnel | Notes |
|---|---|---|---|
| reddit.com / old.reddit.com | blocked | 302 to a login wall | anti-bot for datacenter IPs; treat as unavailable |
| quora.com, medium.com | blocked / 403 | 403 challenge | Cloudflare challenge; a real browser sometimes passes |
| imdb.com | 403 | 202 challenge | ditto |
| trustpilot.com, producthunt.com | 403 | 403 | refused for datacenter IPs in both paths; do not add |
| askubuntu.com, douban.com | blocked | 200 | routed and working |
| stackoverflow.com, superuser.com, news.ycombinator.com, lobste.rs | 200 | unnecessary | leave direct |

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `status` says `stopped` | run `up`; if the service is installed, `systemctl --user restart proxy-tunnel` |
| `canary: FAILED (0/3)` | tunnel is dead: `up --refresh`; if that fails too, reseed the pool |
| `canary: ok … (1/3 resets)` | normal for public configs; fetchers retry, nothing to do |
| fetch works for one blocked site, fails for another | the second domain is not routed: `allow <domain>` |
| every fetch fails, including normal sites | gateway is down and the tool insists on it: start the gateway, or unset the proxy env for that tool |
| `pool is empty` | `seed --force`, or add links to `pool.txt` |
| `xray binary not found` | run `setup` to download it, or set `XRAY_BIN` |
| xray download fails | GitHub is unreachable from this machine; set `XRAY_BIN` to a binary you already have |
| port 1080 already used | set `PROXY_TUNNEL_PORT` for both the CLI and the service, then rewire the env |
| `canary: FAILED` while the site loads by hand | the canary host does not suit this network; set `PROXY_TUNNEL_CANARY` to a URL that does |
| gateway starts then exits | read `~/.config/proxy-tunnel/gateway.log`; a bad link makes xray refuse the config |

`gateway.json` is rewritten from `pool.txt`, `domains.txt`, and the chosen config on
every `up`/`allow`; edit the inputs, never the generated file.

## Log size

`gateway.log` is capped at 2 MB. When it passes the cap, the last 200 lines move to
`gateway.log.1` and the live file is truncated in place — safe because xray appends
through an `O_APPEND` descriptor, so its next write starts at the new end of file. The
supervisor checks every cycle, and every gateway start rotates before writing, so the
pair never exceeds roughly two cap sizes.

Raise or lower it with `PROXY_TUNNEL_LOG_MAX` (bytes) in the unit's `Environment=`.
`tunnel.py status` prints the current size, and `gateway.log.1` is the place to look
right after a rotation.

Manual `up` runs rotate on start-up only; the periodic check belongs to the service.
