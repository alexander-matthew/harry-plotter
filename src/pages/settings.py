"""Settings page - Plot configuration for the CNC Pen Plotter application."""
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.controls import create_plot_settings

# Register this page

dash.register_page(__name__, path='/settings', title='Plot Settings')

# Page layout
layout = dbc.Container([
    dbc.Row([
        # Left Side - Settings
        dbc.Col([
            create_plot_settings(),

            # Connection Settings
            dbc.Card([
                dbc.CardHeader("Plotter Connection"),
                dbc.CardBody([
                    dbc.Label("Serial Port"),
                    dcc.Dropdown(
                        id='serial-port',
                        options=[
                            {'label': '/dev/ttyUSB0', 'value': '/dev/ttyUSB0'},
                            {'label': '/dev/ttyACM0', 'value': '/dev/ttyACM0'},
                            {'label': 'COM3', 'value': 'COM3'},
                            {'label': 'COM4', 'value': 'COM4'},
                        ],
                        value='/dev/ttyUSB0',
                        clearable=False,
                    ),

                    dbc.Label("Baud Rate", className="mt-2"),
                    dcc.Dropdown(
                        id='baud-rate',
                        options=[
                            {'label': '9600', 'value': 9600},
                            {'label': '19200', 'value': 19200},
                            {'label': '38400', 'value': 38400},
                            {'label': '115200', 'value': 115200},
                        ],
                        value=115200,
                        clearable=False,
                    ),

                    dbc.Button(
                        "Test Connection",
                        id='test-connection-btn',
                        color="info",
                        className="w-100 mt-3",
                    ),
                    html.Div(id='connection-status', className="mt-2"),
                ])
            ], className="mt-3"),
        ], width=6),

        # Right Side - Preview and Export
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Export Options"),
                dbc.CardBody([
                    html.H6("G-Code Settings"),

                    dbc.Checklist(
                        id='gcode-options',
                        options=[
                            {"label": "Include header comments", "value": "header"},
                            {"label": "Add homing sequence", "value": "homing"},
                            {"label": "Enable Z-axis safety", "value": "z_safety"},
                        ],
                        value=["header", "homing", "z_safety"],
                        className="mb-3",
                    ),

                    html.Hr(),

                    html.H6("SVG Settings"),

                    dbc.Label("Stroke Width"),
                    dbc.Input(id='svg-stroke-width', type='number', value=0.5, min=0.1, max=5, step=0.1),

                    dbc.Label("Units", className="mt-2"),
                    dcc.Dropdown(
                        id='svg-units',
                        options=[
                            {'label': 'mm', 'value': 'mm'},
                            {'label': 'inches', 'value': 'in'},
                        ],
                        value='mm',
                        clearable=False,
                    ),

                    html.Hr(),

                    html.P(
                        "Export functionality is available on the Image Processing and Generative Art pages.",
                        className="text-muted text-center",
                    ),
                ])
            ]),

            # Statistics Card
            dbc.Card([
                dbc.CardHeader("Current Job Statistics"),
                dbc.CardBody([
                    html.Div(id='job-stats', children=[
                        html.P("No job loaded", className="text-muted"),
                    ])
                ])
            ], className="mt-3"),
        ], width=6),
    ]),
], fluid=True)

