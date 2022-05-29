from dash.dependencies import Input, Output
from src.callbacks.simple_dash_callback import SimpleDashCallback

__all__ = ["callback"]


def _toggle_active_links(pathname):
    """
    this callback uses the current pathname to set the active state of the corresponding nav link
    to true, allowing users to tell see page they are on.
    """
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


callback = SimpleDashCallback(
    func=_toggle_active_links,
    output=[Output(f"page-{i}-link", "active") for i in range(1, 4)],
    input=[Input("url", "pathname")],
)
