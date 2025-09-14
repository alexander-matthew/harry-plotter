"""
Control components for the CNC Pen Plotter application.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc
from src.constants import EDGE_DETECTION_METHODS, VECTORIZATION_METHODS, GENERATIVE_ALGORITHMS


def create_image_filter_controls():
    """Create image filter controls with collapsible sections."""
    return dbc.Card([
        dbc.CardHeader("Image Processing"),
        dbc.CardBody([
            # Basic Adjustments - Collapsible
            dbc.Button(
                [html.I(className="fas fa-chevron-down me-2"), "Basic Adjustments"],
                id={'type': 'collapse-button', 'index': 'basic'},
                color="light",
                className="w-100 text-start mb-2",
                size="sm"
            ),
            dbc.Collapse([
                dbc.Label("Brightness"),
                dcc.Slider(
                    id='brightness-slider',
                    min=-100, max=100, value=0,
                    marks={-100: '-100', 0: '0', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),

                dbc.Label("Contrast", className="mt-2"),
                dcc.Slider(
                    id='contrast-slider',
                    min=-100, max=100, value=0,
                    marks={-100: '-100', 0: '0', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),

                dbc.Label("Threshold", className="mt-2"),
                dcc.Slider(
                    id='threshold-slider',
                    min=0, max=255, value=128,
                    marks={0: '0', 128: '128', 255: '255'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),

                dbc.Checklist(
                    id='invert-check',
                    options=[{"label": "Invert Colors", "value": 1}],
                    value=[],
                    className="mt-2 mb-3"
                ),
            ], id={'type': 'collapse', 'index': 'basic'}, is_open=True),

            # Edge Detection - Collapsible
            dbc.Button(
                [html.I(className="fas fa-chevron-down me-2"), "Edge Detection"],
                id={'type': 'collapse-button', 'index': 'edge'},
                color="light", 
                className="w-100 text-start mb-2",
                size="sm"
            ),
            dbc.Collapse([
                dbc.Label("Method"),
                dcc.Dropdown(
                    id='edge-method',
                    options=[{'label': v, 'value': k} for k, v in EDGE_DETECTION_METHODS.items()],
                    value='none',
                    clearable=False
                ),

                dbc.Label("Sensitivity", className="mt-2"),
                dcc.Slider(
                    id='edge-sensitivity',
                    min=0, max=100, value=50,
                    marks={0: '0', 50: '50', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),
            ], id={'type': 'collapse', 'index': 'edge'}, is_open=False, className="mb-3"),

            # Vectorization - Collapsible
            dbc.Button(
                [html.I(className="fas fa-chevron-down me-2"), "Vectorization"],
                id={'type': 'collapse-button', 'index': 'vector'},
                color="light",
                className="w-100 text-start mb-2", 
                size="sm"
            ),
            dbc.Collapse([
                dbc.Label("Method"),
                dcc.Dropdown(
                    id='vector-method',
                    options=[{'label': v, 'value': k} for k, v in VECTORIZATION_METHODS.items()],
                    value='contour',
                    clearable=False
                ),

                dbc.Label("Hatch Spacing", className="mt-2"),
                dcc.Slider(
                    id='hatch-spacing',
                    min=2, max=20, value=5, step=1,
                    marks={2: '2', 10: '10', 20: '20'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),

                dbc.Label("Hatch Angle", className="mt-2"),
                dcc.Slider(
                    id='hatch-angle',
                    min=0, max=180, value=45, step=15,
                    marks={0: '0°', 45: '45°', 90: '90°', 135: '135°', 180: '180°'},
                    tooltip={"placement": "bottom", "always_visible": False}
                ),
            ], id={'type': 'collapse', 'index': 'vector'}, is_open=False),
        ])
    ], className="mt-3")


def create_generative_controls():
    """Create generative art controls."""
    return dbc.Card([
        dbc.CardHeader("Generative Art"),
        dbc.CardBody([
            dbc.Label("Algorithm"),
            dcc.Dropdown(
                id='gen-algorithm',
                options=[{'label': v, 'value': k} for k, v in GENERATIVE_ALGORITHMS.items()],
                value='flow_field',
                clearable=False
            ),

            dbc.Label("Random Seed", className="mt-3"),
            dbc.InputGroup([
                dbc.Input(id='random-seed', type='number', value=42),
                dbc.Button("🎲", id='randomize-seed', color="secondary", size="sm"),
            ]),

            dbc.Label("Complexity", className="mt-3"),
            dcc.Slider(
                id='complexity-slider',
                min=1, max=10, value=5, step=1,
                marks={1: '1', 5: '5', 10: '10'},
                tooltip={"placement": "bottom", "always_visible": False}
            ),

            dbc.Label("Scale", className="mt-2"),
            dcc.Slider(
                id='scale-slider',
                min=0.5, max=3, value=1, step=0.1,
                marks={0.5: '0.5x', 1: '1x', 2: '2x', 3: '3x'},
                tooltip={"placement": "bottom", "always_visible": False}
            ),

            # Algorithm-specific parameters (dynamically shown)
            html.Div(id='algorithm-params', className="mt-3"),

            dbc.Button(
                "Generate Art",
                id='generate-btn',
                color="primary",
                className="w-100 mt-3"
            ),
        ])
    ], className="mt-3")


def create_plot_settings():
    """Create plot settings controls."""
    return dbc.Card([
        dbc.CardHeader("Plot Settings"),
        dbc.CardBody([
            dbc.Label("Plot Width (mm)"),
            dbc.Input(id='plot-width', type='number', value=100, min=10, max=300),

            dbc.Label("Plot Height (mm)", className="mt-2"),
            dbc.Input(id='plot-height', type='number', value=100, min=10, max=300),

            dbc.Label("Feed Rate (mm/min)", className="mt-2"),
            dbc.Input(id='feed-rate', type='number', value=1000, min=100, max=5000),

            dbc.Label("Pen Lift Height (mm)", className="mt-2"),
            dbc.Input(id='pen-lift', type='number', value=5, min=1, max=20),
        ])
    ], className="mt-3")


def create_action_buttons():
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