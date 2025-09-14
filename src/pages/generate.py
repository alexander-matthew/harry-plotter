"""
Generate page - Generative art workflow for the CNC Pen Plotter application.
"""
import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import numpy as np

from src.components.controls import create_generative_controls, create_action_buttons
from src.components.preview import create_single_preview
from src.utils.generative_art import generate_art
from src.utils.image_processing import apply_filters, extract_paths
from src.utils.plotting import create_image_figure, create_empty_figure

# Register this page
dash.register_page(__name__, path='/generate', title='Generative Art')

# Page layout
layout = dbc.Container([
    dbc.Row([
        # Left Sidebar - Controls
        dbc.Col([
            create_generative_controls(),
        ], width=4),

        # Right Main Area - Preview
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Generated Art Preview"),
                dbc.CardBody([
                    create_single_preview(),
                    html.Hr(),
                    html.Div(id='gen-path-stats', className="text-muted"),
                ])
            ]),
            create_action_buttons(),
        ], width=8),
    ]),
], fluid=True)


# Callbacks for generative art page
@callback(
    Output('random-seed', 'value'),
    Input('randomize-seed', 'n_clicks'),
    prevent_initial_call=True
)
def randomize_seed(n_clicks):
    """Generate random seed."""
    return np.random.randint(0, 10000)


@callback(
    Output('main-preview', 'figure'),
    Output('gen-path-stats', 'children'),
    Input('generate-btn', 'n_clicks'),
    State('gen-algorithm', 'value'),
    State('random-seed', 'value'),
    State('complexity-slider', 'value'),
    State('scale-slider', 'value'),
)
def generate_and_preview(n_clicks, algorithm, seed, complexity, scale):
    """Generate art and create preview."""
    if not n_clicks:
        return create_empty_figure(), "Click 'Generate Art' to create artwork"

    try:
        # Generate art
        np.random.seed(seed)
        generated_img = generate_art(algorithm, complexity, scale)

        # Extract paths for stats
        paths = extract_paths(generated_img, 'contour')
        stats = f"Algorithm: {algorithm} | Paths: {len(paths)} | Est. time: {len(paths) * 2} seconds"

        # Create figure
        fig = create_image_figure(generated_img, f"Generated Art - {algorithm}")

        return fig, stats
        
    except Exception as e:
        return create_empty_figure(), f"Error: {str(e)}"