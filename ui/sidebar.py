from dash import html

_S = {
    "card": {"padding": "10px 14px", "borderBottom": "1px solid #1e1e3a", "cursor": "pointer"},
    "name": {"fontWeight": "bold", "fontSize": "13px", "color": "#e0e0e0"},
    "detail": {"fontSize": "11px", "color": "#888", "marginTop": "3px"},
    "label": {"fontSize": "11px", "color": "#555", "marginBottom": "2px"},
    "value": {"fontSize": "13px", "color": "#e0e0e0", "marginBottom": "10px"},
}


def _vessel_card(vessel: dict) -> html.Div:
    dest = vessel.get("destination") or "—"
    speed = f"{vessel['speed']} kn" if vessel["speed"] > 0.5 else "At anchor"
    return html.Div(
        [html.Div(vessel["name"], style=_S["name"]),
         html.Div(f"{speed} · {dest}", style=_S["detail"])],
        style=_S["card"],
        id={"type": "vessel-card", "mmsi": vessel["mmsi"]},
    )


def _stat(label: str, value: str) -> html.Div:
    return html.Div([
        html.Div(label, style=_S["label"]),
        html.Div(value, style=_S["value"]),
    ])


def _detail_panel(vessel: dict, history: list[dict]) -> html.Div:
    speed = f"{vessel['speed']} kn" if vessel["speed"] > 0.5 else "At anchor"
    last_seen = vessel.get("timestamp", "")[:16].replace("T", " ") if vessel.get("timestamp") else "—"
    return html.Div([
        html.Div(
            html.Button("← Fleet", id="btn-back",
                        style={"background": "none", "border": "none", "color": "#00d4ff",
                               "cursor": "pointer", "fontSize": "12px", "padding": "0"}),
            style={"padding": "12px 14px", "borderBottom": "1px solid #1e1e3a"},
        ),
        html.Div([
            html.Div(vessel["name"],
                     style={"fontSize": "16px", "fontWeight": "bold", "color": "#00d4ff", "marginBottom": "4px"}),
            html.Div(f"MMSI {vessel['mmsi']}", style={"fontSize": "11px", "color": "#555"}),
        ], style={"padding": "14px", "borderBottom": "1px solid #1e1e3a"}),
        html.Div([
            _stat("STATUS", speed),
            _stat("HEADING", f"{vessel['heading']}°" if vessel["heading"] else "—"),
            _stat("DESTINATION", vessel.get("destination") or "—"),
            _stat("LAST UPDATED", last_seen),
            _stat("TRAIL POINTS", str(len(history))),
        ], style={"padding": "14px"}),
    ])


def _header(vessel_count: int) -> html.Div:
    return html.Div([
        html.Div("barquitos", style={"fontSize": "18px", "fontWeight": "bold", "color": "#00d4ff"}),
        html.Div(f"{vessel_count} LNG vessels", style={"fontSize": "12px", "color": "#666"}),
    ], style={"padding": "16px", "borderBottom": "1px solid #1e1e3a"})


def build(vessels: list[dict]) -> html.Div:
    return html.Div([
        _header(len(vessels)),
        html.Div([_vessel_card(v) for v in vessels], style={"overflowY": "auto", "flex": "1"}),
    ], style={"display": "flex", "flexDirection": "column", "height": "100%"})


def build_detail(vessel: dict, history: list[dict]) -> html.Div:
    return html.Div(
        _detail_panel(vessel, history),
        style={"height": "100%", "overflowY": "auto"},
    )
