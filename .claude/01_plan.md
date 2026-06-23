# Project Plan

## Goal
A Kpler-like LNG vessel tracker that combines real-time AIS data with Sentinel-1 SAR
satellite imagery to detect dark vessels — ships that disable AIS near sanctioned
terminals (Russia, Iran) or during ship-to-ship transfers.

AIS-only trackers miss this. That's the differentiator.

## Status

| Phase | Status | Description |
|-------|--------|-------------|
| 0 — Setup | ✅ Done | uv, Dash scaffold, GitHub, CLAUDE.md |
| 1 — Live map | 🔲 Next | AIS WebSocket → map with LNG vessels |
| 2 — Route intelligence | 🔲 Pending | SQLite history, port calls, prediction |
| 3 — Satellite layer | 🔲 Pending | Sentinel-1 SAR, dark vessel detection |
| 4 — Analytics | 🔲 Pending | Trade flows, fleet utilization, anomalies |

## Phase 1 — Live Map
- [ ] Sign up for aisstream.io API key (free)
- [ ] WebSocket client: connect, filter LNG vessel type codes, parse messages
- [ ] SQLite: create vessels and positions tables
- [ ] Dash-leaflet map: vessel markers with heading/speed
- [ ] Sidebar: vessel list with name, flag, status, destination
- [ ] Auto-refresh on interval

## Phase 2 — Route Intelligence
- [ ] Persist position history in SQLite
- [ ] Route trail overlay on map per selected vessel
- [ ] Port call detection (vessel stationary ≤ 0.5 knots near known terminal)
- [ ] Linear movement prediction (speed × heading extrapolation)

## Phase 3 — Satellite Layer
- [ ] Register for Sentinel Hub free tier (60 processing units/month)
- [ ] Fetch Sentinel-1 SAR scenes for monitored terminals
- [ ] Run SAR vessel detection (SAR-Ship model or equivalent)
- [ ] Cross-reference: vessel in SAR but absent in AIS → dark vessel alert
- [ ] Targeted terminals only (not global — free tier is limited)

## Phase 4 — Analytics
- [ ] Trade flow: origin → destination patterns per vessel
- [ ] Fleet utilization: voyage duration, port turnaround time
- [ ] Anomaly detection: unusual routes, STS transfer zone loitering

## Key Constraints
- AIS source: aisstream.io free WebSocket (no budget for paid APIs)
- Satellite: Sentinel Hub free tier, 60 processing units/month
- Satellite is NOT real-time: ~6 day revisit, hours processing lag
- Satellite is still valuable: confirms positions when AIS is off
