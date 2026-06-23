import dash_leaflet as dl

_TILE_URL = "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
_TILE_ATTRIBUTION = '&copy; <a href="https://www.openstreetmap.org">OSM</a> &copy; <a href="https://carto.com">CARTO</a>'


def _tooltip(vessel: dict) -> str:
    dest = vessel.get("destination") or "unknown destination"
    status = f"{vessel['speed']} kn" if vessel["speed"] > 0.5 else "at anchor"
    return f"{vessel['name']} · {status} → {dest}"


def _marker(vessel: dict) -> dl.CircleMarker:
    color = "#00d4ff" if vessel["speed"] > 0.5 else "#ff9f43"
    return dl.CircleMarker(
        center=[vessel["lat"], vessel["lon"]],
        radius=6,
        color=color,
        fill=True,
        fillOpacity=0.85,
        children=dl.Tooltip(_tooltip(vessel)),
        id={"type": "marker", "mmsi": vessel["mmsi"]},
    )


def make_markers(vessels: list[dict]) -> list:
    return [_marker(v) for v in vessels]


def build(vessels: list[dict]) -> dl.Map:
    return dl.Map(
        children=[
            dl.TileLayer(url=_TILE_URL, attribution=_TILE_ATTRIBUTION),
            dl.LayerGroup(id="vessel-markers", children=make_markers(vessels)),
        ],
        center=[20, 0],
        zoom=2,
        style={"height": "100%", "width": "100%"},
    )
