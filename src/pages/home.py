"""
Home page - Image processing workflow for the CNC Pen Plotter application.
"""
import dash
from dash import dcc, html, Input, Output, State, callback, MATCH
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import base64
import io
from PIL import Image
import numpy as np

from src.components.upload import create_upload_section
from src.components.controls import create_image_filter_controls, create_action_buttons
from src.components.preview import create_preview_section
from src.utils.image_processing import apply_filters, extract_paths
from src.utils.plotting import create_image_figure, create_empty_figure

# Register this page
dash.register_page(__name__, path='/', title='Image Processing')

# Page layout
layout = dbc.Container([
    dbc.Row([
        # Left Sidebar - Controls (Scrollable)
        dbc.Col([
            html.Div([
                create_upload_section(),
                create_image_filter_controls(),
            ], style={
                'height': '80vh',
                'overflowY': 'auto',
                'paddingRight': '10px'
            })
        ], width=4),

        # Right Main Area - Preview (Fixed)
        dbc.Col([
            html.Div([
                create_preview_section(),
                create_action_buttons(),
            ], style={
                'height': '80vh',
                'position': 'sticky',
                'top': '20px'
            })
        ], width=8),
    ]),
], fluid=True)


# Callbacks for image processing page
@callback(
    Output('global-image-data', 'data'),
    Output('upload-status', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename')
)
def upload_image(contents, filename):
    """Handle image upload."""
    if contents is None:
        raise PreventUpdate

    try:
        # Decode image
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        # Store image data
        return contents, dbc.Alert(f"Uploaded: {filename}", color="success")
    except Exception as e:
        return None, dbc.Alert(f"Error: {str(e)}", color="danger")


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
def process_image(n_clicks, brightness, contrast, threshold, 
                 invert, edge_method, vector_method, image_data):
    """Process uploaded image."""
    if not image_data:
        # Return empty figures
        empty_fig = create_empty_figure()
        return empty_fig, empty_fig, "Upload an image to get started"

    try:
        # Process uploaded image
        content_type, content_string = image_data.split(',')
        decoded = base64.b64decode(content_string)
        img = Image.open(io.BytesIO(decoded))
        source_img = img.convert('L')  # Convert to grayscale

        # Apply filters
        processed_img = apply_filters(source_img, brightness, contrast, 
                                    threshold, invert, edge_method)

        # Generate path statistics
        paths = extract_paths(processed_img, vector_method)
        stats = f"Paths: {len(paths)} | Est. time: {len(paths) * 2} seconds | Distance: {len(paths) * 10}mm"

        # Create figures
        source_fig = create_image_figure(source_img, "Source")
        processed_fig = create_image_figure(processed_img, "Processed")

        return source_fig, processed_fig, stats
        
    except Exception as e:
        empty_fig = create_empty_figure()
        return empty_fig, empty_fig, f"Error: {str(e)}"


# Single callback for all collapsible sections using pattern matching
@callback(
    Output({'type': 'collapse', 'index': MATCH}, 'is_open'),
    Output({'type': 'collapse-button', 'index': MATCH}, 'children'),
    Input({'type': 'collapse-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'collapse', 'index': MATCH}, 'is_open'),
    State({'type': 'collapse-button', 'index': MATCH}, 'children'),
    prevent_initial_call=True
)
def toggle_collapse(n_clicks, is_open, current_children):
    """Toggle any collapsible section."""
    if n_clicks:
        new_state = not is_open
        icon = "fas fa-chevron-up" if new_state else "fas fa-chevron-down"
        # Extract the text from current children
        text = current_children[1] if len(current_children) > 1 else "Section"
        return new_state, [html.I(className=f"{icon} me-2"), text]
    return is_open, current_children