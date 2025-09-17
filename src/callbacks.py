"""Global callbacks for the CNC Pen Plotter application."""
import logging
from dash import Input, Output, callback
from dash.exceptions import PreventUpdate

from src.utils.plotting import generate_gcode, generate_svg, create_download_data
from src.constants import DEFAULT_PLOT_SETTINGS

logger = logging.getLogger(__name__)


@callback(
    Output("global-download-gcode", "data"),
    Input("download-gcode-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_gcode_global(n_clicks: int):
    """Generate and download G-code file globally."""
    if not n_clicks:
        raise PreventUpdate

    # TODO: Replace mock paths and settings with values from stores
    paths = [(0, 0), (100, 100), (200, 50)]
    plot_settings = DEFAULT_PLOT_SETTINGS

    logger.info("Generating G-code for %d paths", len(paths))
    gcode = generate_gcode(paths, plot_settings)
    return create_download_data(gcode, "gcode")


@callback(
    Output("global-download-svg", "data"),
    Input("download-svg-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_svg_global(n_clicks: int):
    """Generate and download SVG file globally."""
    if not n_clicks:
        raise PreventUpdate

    # TODO: Replace mock paths and settings with values from stores
    paths = [(0, 0), (100, 100), (200, 50)]
    plot_settings = DEFAULT_PLOT_SETTINGS

    logger.info("Generating SVG for %d paths", len(paths))
    svg = generate_svg(paths, plot_settings)
    return create_download_data(svg, "svg")
