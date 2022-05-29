from dash import html
from dash.dependencies import Input, Output
from src.callbacks.simple_dash_callback import SimpleDashCallback

__all__ = ["callback"]


def _render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P("This is the content of page 1!")
    elif pathname == "/page-2":
        return html.P("This is the content of page 2. Yay!")
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


callback = SimpleDashCallback(
    func=_render_page_content,
    output=[Output("page-content", "children")],
    input=[Input("url", "pathname")],
)
