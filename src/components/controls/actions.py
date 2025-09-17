"""Action button components."""
from dash import html
import dash_bootstrap_components as dbc


def create_action_buttons() -> dbc.Card:
    """Create action buttons."""
    return dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Button("Process Image", id='process-btn', color="primary", className="w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button("Download G-Code", id='download-gcode-btn', color="success", className="w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button("Download SVG", id='download-svg-btn', color="success", className="w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button("Send to Plotter", id='send-plot-btn', color="warning", className="w-100",
                               disabled=True),
                ], width=3),
            ]),
            dbc.Progress(id='progress-bar', value=0, className="mt-3", style={'height': '20px'}),
            html.Div(id='status-message', className="mt-2 text-center"),
        ])
    ])

