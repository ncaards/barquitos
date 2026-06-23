import dash

app = dash.Dash(__name__)

app.layout = dash.html.Div("barquitos")

if __name__ == "__main__":
    app.run(debug=True)
