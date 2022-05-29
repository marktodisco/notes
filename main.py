import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from src import layout
from src.callbacks import register_callbacks

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


content = html.Div(id="page-content", style=layout.CONTENT_STYLE)

app.layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Location(id="url"),
        layout.navbar,
        layout.sidebar,
        content,
    ],
)


register_callbacks(app)


if __name__ == "__main__":
    app.run(debug=True)
