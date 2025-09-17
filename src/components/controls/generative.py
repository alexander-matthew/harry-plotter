"""Generative art control components."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from src.constants import GENERATIVE_ALGORITHMS


def create_generative_controls() -> dbc.Card:
    """Create generative art controls."""
    return dbc.Card([
        dbc.CardHeader("Generative Art"),
        dbc.CardBody([
            dbc.Label("Algorithm"),
            dcc.Dropdown(
                id='gen-algorithm',
                options=[{'label': v, 'value': k} for k, v in GENERATIVE_ALGORITHMS.items()],
                value='flow_field',
                clearable=False,
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
                tooltip={"placement": "bottom", "always_visible": False},
            ),

            dbc.Label("Scale", className="mt-2"),
            dcc.Slider(
                id='scale-slider',
                min=0.5, max=3, value=1, step=0.1,
                marks={0.5: '0.5x', 1: '1x', 2: '2x', 3: '3x'},
                tooltip={"placement": "bottom", "always_visible": False},
            ),

            # Algorithm-specific parameters (dynamically shown)
            html.Div(id='algorithm-params', className="mt-3"),

            dbc.Button(
                "Generate Art",
                id='generate-btn',
                color="primary",
                className="w-100 mt-3",
            ),
        ])
    ], className="mt-3")

