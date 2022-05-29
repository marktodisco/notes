import dash
from src.callbacks.simple_dash_callback import SimpleDashCallback


def fetch_callbacks() -> list[SimpleDashCallback]:
    from src.callbacks import render_page_content, toggle_active_links, toggle_sidebar

    return [
        render_page_content.callback,
        toggle_active_links.callback,
        toggle_sidebar.callback,
    ]


def register_callbacks(app: dash.Dash) -> None:
    for callback in fetch_callbacks():
        callback.register(app)
