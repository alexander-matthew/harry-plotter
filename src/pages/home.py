"""Home page - Image processing workflow for the CNC Pen Plotter application."""
import dash
from dash import html
import dash_bootstrap_components as dbc

from src.components.upload import create_upload_section
from src.components.controls import create_image_filter_controls, create_action_buttons
from src.components.preview import create_preview_section

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

