"""
Global callbacks for the CNC Pen Plotter application.
"""
import dash
from dash import Input, Output, callback, ctx
from dash.exceptions import PreventUpdate

from src.utils.plotting import generate_gcode, generate_svg, create_download_data
from src.constants import DEFAULT_PLOT_SETTINGS


@callback(
    Output("global-download-gcode", "data"),
    Input("download-gcode-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_gcode_global(n_clicks):
    """Generate and download G-code file globally."""
    if not n_clicks:
        raise PreventUpdate
        
    # Mock paths and settings - in real implementation, these would come from stores
    paths = [(0, 0), (100, 100), (200, 50)]
    plot_settings = DEFAULT_PLOT_SETTINGS
    
    gcode = generate_gcode(paths, plot_settings)
    return create_download_data(gcode, "gcode")


@callback(
    Output("global-download-svg", "data"), 
    Input("download-svg-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_svg_global(n_clicks):
    """Generate and download SVG file globally."""
    if not n_clicks:
        raise PreventUpdate
        
    # Mock paths and settings - in real implementation, these would come from stores
    paths = [(0, 0), (100, 100), (200, 50)]
    plot_settings = DEFAULT_PLOT_SETTINGS
    
    svg = generate_svg(paths, plot_settings)
    return create_download_data(svg, "svg")