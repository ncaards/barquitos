from dash import html, dcc

from db.queries import latest_positions
from ui import map as map_ui
from ui import sidebar as sidebar_ui

_STYLE_ROOT = {
    "display": "flex", "height": "100vh",
    "background": "#0a0a1a", "fontFamily": "'Courier New', monospace", "overflow": "hidden",
}
_STYLE_SIDEBAR = {
    "width": "280px", "flexShrink": "0",
    "background": "#10102a", "color": "white", "borderRight": "1px solid #1e1e3a",
}
_STYLE_MAP = {"flex": "1", "position": "relative", "height": "100%"}


def build() -> html.Div:
    vessels = latest_positions()
    return html.Div([
        dcc.Store(id="selected-mmsi", data=None),
        dcc.Interval(id="refresh-interval", interval=30_000, n_intervals=0),
        html.Div(sidebar_ui.build(vessels), id="sidebar-container", style=_STYLE_SIDEBAR),
        html.Div(map_ui.build(vessels), style=_STYLE_MAP),
    ], style=_STYLE_ROOT)
