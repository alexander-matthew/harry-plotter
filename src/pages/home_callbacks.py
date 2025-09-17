"""Callbacks for the home (image processing) page."""
import base64
import io
import logging
from dash import Input, Output, State, callback, MATCH, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from PIL import Image

from src.utils.image_processing import apply_filters, extract_paths
from src.utils.plotting import create_image_figure, create_empty_figure

logger = logging.getLogger(__name__)


@callback(
    Output('global-image-data', 'data'),
    Output('upload-status', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename')
)
def upload_image(contents: str | None, filename: str | None):
    """Handle image upload."""
    if contents is None:
        raise PreventUpdate

    try:
        content_type, content_string = contents.split(',')
        base64.b64decode(content_string)
        return contents, dbc.Alert(f"Uploaded: {filename}", color="success")
    except Exception as exc:  # pragma: no cover - placeholder
        logger.error("Failed to upload image: %s", exc)
        return None, dbc.Alert(f"Error: {exc}", color="danger")


@callback(
    Output('source-preview', 'figure'),
    Output('processed-preview', 'figure'),
    Output('path-stats', 'children'),
    [Input('process-btn', 'n_clicks'),
     Input('brightness-slider', 'value'),
     Input('contrast-slider', 'value'),
     Input('threshold-slider', 'value'),
     Input('invert-check', 'value'),
     Input('edge-method', 'value'),
     Input('vector-method', 'value')],
    State('global-image-data', 'data'),
)
def process_image(
    n_clicks: int | None,
    brightness: int,
    contrast: int,
    threshold: int,
    invert: list[int],
    edge_method: str,
    vector_method: str,
    image_data: str | None,
):
    """Process uploaded image."""
    if not image_data:
        empty_fig = create_empty_figure()
        return empty_fig, empty_fig, "Upload an image to get started"

    try:
        content_type, content_string = image_data.split(',')
        decoded = base64.b64decode(content_string)
        img = Image.open(io.BytesIO(decoded)).convert('L')

        processed_img = apply_filters(img, brightness, contrast, threshold, bool(invert), edge_method)

        paths = extract_paths(processed_img, vector_method)
        stats = f"Paths: {len(paths)} | Est. time: {len(paths) * 2} seconds | Distance: {len(paths) * 10}mm"

        source_fig = create_image_figure(img, "Source")
        processed_fig = create_image_figure(processed_img, "Processed")

        return source_fig, processed_fig, stats
    except Exception as exc:  # pragma: no cover - placeholder
        logger.error("Image processing failed: %s", exc)
        empty_fig = create_empty_figure()
        return empty_fig, empty_fig, f"Error: {exc}"


@callback(
    Output({'type': 'collapse', 'index': MATCH}, 'is_open'),
    Output({'type': 'collapse-button', 'index': MATCH}, 'children'),
    Input({'type': 'collapse-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'collapse', 'index': MATCH}, 'is_open'),
    State({'type': 'collapse-button', 'index': MATCH}, 'children'),
    prevent_initial_call=True,
)
def toggle_collapse(n_clicks: int, is_open: bool, current_children: list):
    """Toggle any collapsible section."""
    if n_clicks:
        new_state = not is_open
        icon = "fas fa-chevron-up" if new_state else "fas fa-chevron-down"
        text = current_children[1] if len(current_children) > 1 else "Section"
        return new_state, [html.I(className=f"{icon} me-2"), text]
    return is_open, current_children

