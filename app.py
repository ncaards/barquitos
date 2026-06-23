import dash
from dash import Input, Output

from db.queries import latest_positions
from db.schema import init
from ui import layout
from ui import map as map_ui
from ui import sidebar as sidebar_ui

app = dash.Dash(__name__, title="barquitos")
init()

app.layout = layout.build()


@app.callback(
    Output("vessel-markers", "children"),
    Output("sidebar-container", "children"),
    Input("refresh-interval", "n_intervals"),
)
def refresh(n_intervals: int) -> tuple:
    vessels = latest_positions()
    return map_ui.make_markers(vessels), sidebar_ui.build(vessels)


if __name__ == "__main__":
    app.run(debug=True)
