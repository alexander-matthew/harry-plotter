"""Generate page - Generative art workflow for the CNC Pen Plotter application."""
import dash
from dash import html
import dash_bootstrap_components as dbc

from src.components.controls import create_generative_controls, create_action_buttons
from src.components.preview import create_single_preview

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

