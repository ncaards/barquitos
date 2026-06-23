from dash import html

_STYLE_CARD = {
    "padding": "10px 14px",
    "borderBottom": "1px solid #1e1e3a",
    "cursor": "pointer",
}
_STYLE_NAME = {"fontWeight": "bold", "fontSize": "13px", "color": "#e0e0e0"}
_STYLE_DETAIL = {"fontSize": "11px", "color": "#888", "marginTop": "3px"}


def _vessel_card(vessel: dict) -> html.Div:
    dest = vessel.get("destination") or "—"
    speed = f"{vessel['speed']} kn" if vessel["speed"] > 0.5 else "At anchor"
    return html.Div(
        [
            html.Div(vessel["name"], style=_STYLE_NAME),
            html.Div(f"{speed} · {dest}", style=_STYLE_DETAIL),
        ],
        style=_STYLE_CARD,
        id={"type": "vessel-card", "mmsi": vessel["mmsi"]},
    )


def _header(vessel_count: int) -> html.Div:
    return html.Div(
        [
            html.Div("barquitos", style={"fontSize": "18px", "fontWeight": "bold", "color": "#00d4ff"}),
            html.Div(f"{vessel_count} LNG vessels", style={"fontSize": "12px", "color": "#666"}),
        ],
        style={"padding": "16px", "borderBottom": "1px solid #1e1e3a"},
    )


def build(vessels: list[dict]) -> html.Div:
    return html.Div(
        [
            _header(len(vessels)),
            html.Div([_vessel_card(v) for v in vessels], style={"overflowY": "auto", "flex": "1"}),
        ],
        style={"display": "flex", "flexDirection": "column", "height": "100%"},
    )
