# barquitos

Dash dashboard for tracking LNG vessels — inspired by Kpler. Combines real-time AIS data with Sentinel-1 SAR satellite imagery to detect dark vessels and monitor trade flows.

## Stack
- **Runtime:** Python 3.12
- **Framework:** Dash + dash-leaflet
- **Package manager:** uv — always use `uv add`, `uv run`, `uv sync`. Never pip.
- **Storage:** SQLite (no infra, stores position history and port calls)
- **AIS source:** aisstream.io (free WebSocket, filter by MMSI or bounding box)
- **Satellite source:** ESA Copernicus Sentinel-1 SAR (free, 60 processing units/month via Sentinel Hub)

## Project phases

### Phase 1 — Live map
- WebSocket connection to aisstream.io, filtered to LNG vessel type codes
- Dash-leaflet map: vessel positions, heading, speed
- Sidebar: vessel name, flag, status, destination
- Auto-refresh loop

### Phase 2 — Route intelligence
- SQLite: persist position history and port calls
- Route trails per vessel on map
- Port call detection (vessel stationary near known LNG terminal coordinates)
- Movement prediction: linear extrapolation from speed + heading

### Phase 3 — Satellite layer
- Pull Sentinel-1 SAR scenes for key LNG terminals (Qatar, Sabine Pass, Yamal, etc.)
- Open-source SAR vessel detection (SAR-Ship or similar)
- Dark vessel alerts: vessel visible in SAR but absent from AIS
- Sentinel Hub free tier (60 processing units/month) — targeted terminal monitoring only

### Phase 4 — Analytics
- Trade flow: origin → destination patterns
- Fleet utilization and voyage duration stats
- Anomaly detection: unusual routes, STS transfer zone loitering

## Domain notes
- ~700 active LNG carriers globally — finite, well-documented MMSIs
- AIS blind spots: vessels disable transponders near sanctioned terminals (Russia, Iran) or during ship-to-ship transfers
- Satellite (Sentinel-1) fills those gaps — not real-time (~6 day revisit, hours processing lag) but genuine data
- Key LNG terminals to monitor: Ras Laffan (Qatar), Sabine Pass (US), Yamal (Russia), Bintulu (Malaysia), Curtis Island (Australia)

## Code style
- No comments. Code must be self-documenting through naming.
- Functions and methods stay under 40 lines.
- Follow PEP 8 and idiomatic Python.
- Prefer composition over inheritance. Keep modules focused.

## Git
- Commit at logical checkpoints with conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`

## Running
```bash
uv run python app.py
```
