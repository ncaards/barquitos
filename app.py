import json

import dash
from dash import ALL, Input, Output, ctx

from db.queries import latest_positions, position_history
from db.schema import init
from ui import layout
from ui import map as map_ui
from ui import sidebar as sidebar_ui

app = dash.Dash(__name__, title="barquitos", suppress_callback_exceptions=True)
init()

app.layout = layout.build()


@app.callback(
    Output("selected-mmsi", "data"),
    Input({"type": "vessel-card", "mmsi": ALL}, "n_clicks"),
    Input("btn-back", "n_clicks"),
    prevent_initial_call=True,
)
def update_selection(card_clicks, _back) -> str | None:
    if not ctx.triggered_id:
        return dash.no_update
    if ctx.triggered_id == "btn-back":
        return None
    if isinstance(ctx.triggered_id, dict):
        return ctx.triggered_id["mmsi"]
    return dash.no_update


@app.callback(
    Output("sidebar-container", "children"),
    Output("vessel-markers", "children"),
    Output("vessel-trail", "children"),
    Input("selected-mmsi", "data"),
    Input("refresh-interval", "n_intervals"),
)
def refresh(selected_mmsi: str | None, _n: int) -> tuple:
    vessels = latest_positions()
    markers = map_ui.make_markers(vessels)

    if selected_mmsi:
        vessel = next((v for v in vessels if v["mmsi"] == selected_mmsi), None)
        if vessel:
            history = position_history(selected_mmsi)
            return sidebar_ui.build_detail(vessel, history), markers, map_ui.make_trail(history)

    return sidebar_ui.build(vessels), markers, []


if __name__ == "__main__":
    app.run(debug=True)
