from dash.dependencies import Input, Output, State
from src import layout
from src.callbacks.simple_dash_callback import SimpleDashCallback

__all__ = ["callback"]


def _toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = layout.SIDEBAR_HIDEN
            content_style = layout.CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = layout.SIDEBAR_STYLE
            content_style = layout.CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = layout.SIDEBAR_STYLE
        content_style = layout.CONTENT_STYLE
        cur_nclick = "SHOW"

    return sidebar_style, content_style, cur_nclick


callback = SimpleDashCallback(
    func=_toggle_sidebar,
    output=[
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],
    input=[Input("btn_sidebar", "n_clicks")],
    state=[State("side_click", "data")],
)
