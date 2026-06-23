# Architecture

## Module layout

```
barquitos/
├── app.py                  # Dash entry point — wires layout + callbacks, nothing else
├── ui/
│   ├── layout.py           # Top-level layout composition
│   ├── map.py              # Leaflet map component and vessel markers
│   └── sidebar.py          # Vessel list, detail panel
├── data/
│   ├── ais.py              # aisstream.io WebSocket client
│   ├── vessels.py          # LNG vessel registry (known MMSIs, type filtering)
│   └── satellite.py        # Sentinel Hub API client (Phase 3)
├── analysis/
│   ├── routes.py           # Route history, port call detection
│   ├── prediction.py       # Movement extrapolation (Phase 2)
│   └── dark_vessels.py     # AIS/SAR cross-reference (Phase 3)
├── db/
│   ├── schema.py           # SQLite table definitions
│   └── queries.py          # All DB reads/writes — no SQL outside this module
└── config.py               # Env vars, constants, terminal coordinates
```

## Data flow

```
aisstream.io WebSocket
        │
        ▼
   data/ais.py          ← parses raw AIS messages, maps to VesselPosition
        │
        ├──► db/queries.py   ← persists to SQLite
        │
        └──► Dash callback   ← triggers map refresh
                │
                ▼
          ui/map.py          ← renders markers, trails
```

## Key decisions

**SQLite over Postgres/Redis**
No infra to manage. The dataset is small: ~700 vessels × position updates every
few minutes. SQLite handles this easily and the file travels with the repo.

**WebSocket over polling**
aisstream.io pushes messages — polling would waste rate limits and add latency.
The Dash interval component triggers UI refresh on a schedule; ingestion runs
continuously in a background thread.

**Dash + dash-leaflet over custom frontend**
Pure Python stack — no JS build toolchain. dash-leaflet gives full Leaflet.js
power (tile layers, polylines, custom markers) through Python components.

**Modular satellite layer (Phase 3)**
SAR processing is heavy and slow relative to AIS. It runs on a separate schedule
(daily per terminal scan, not real-time). The dark vessel alert is an async result
that decorates the map — it never blocks the AIS live view.

## Interfaces between modules

Modules communicate through typed dataclasses defined in `config.py` (or a
dedicated `models.py` once needed). No raw dicts across module boundaries.

```python
@dataclass
class VesselPosition:
    mmsi: str
    lat: float
    lon: float
    speed: float
    heading: float
    timestamp: datetime

@dataclass
class PortCall:
    mmsi: str
    terminal: str
    arrived_at: datetime
    departed_at: datetime | None
```
