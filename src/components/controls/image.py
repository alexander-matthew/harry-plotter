"""Image filter control components."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from src.constants import EDGE_DETECTION_METHODS, VECTORIZATION_METHODS


def create_image_filter_controls() -> dbc.Card:
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
                    className="mt-2 mb-3",
                ),
            ], id={'type': 'collapse', 'index': 'basic'}, is_open=True),

            # Edge Detection - Collapsible
            dbc.Button(
                [html.I(className="fas fa-chevron-down me-2"), "Edge Detection"],
                id={'type': 'collapse-button', 'index': 'edge'},
                color="light",
                className="w-100 text-start mb-2",
                size="sm",
            ),
            dbc.Collapse([
                dbc.Label("Method"),
                dcc.Dropdown(
                    id='edge-method',
                    options=[{'label': v, 'value': k} for k, v in EDGE_DETECTION_METHODS.items()],
                    value='none',
                    clearable=False,
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
                size="sm",
            ),
            dbc.Collapse([
                dbc.Label("Method"),
                dcc.Dropdown(
                    id='vector-method',
                    options=[{'label': v, 'value': k} for k, v in VECTORIZATION_METHODS.items()],
                    value='contour',
                    clearable=False,
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

