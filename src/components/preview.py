"""
Preview components for the CNC Pen Plotter application.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_preview_section():
    """Create preview section with dual canvases."""
    return dbc.Card([
        dbc.CardHeader("Preview"),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id='source-preview',
                        config={'displayModeBar': False},
                        style={'height': '400px'}
                    ),
                ], width=6),
                dbc.Col([
                    dcc.Graph(
                        id='processed-preview',
                        config={'displayModeBar': False},
                        style={'height': '400px'}
                    ),
                ], width=6),
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.Div(id='path-stats', className="text-muted"),
                ], width=12),
            ]),
        ])
    ])


def create_single_preview():
    """Create a single preview graph."""
    return dcc.Graph(
        id='main-preview',
        config={'displayModeBar': False},
        style={'height': '600px'}
    )