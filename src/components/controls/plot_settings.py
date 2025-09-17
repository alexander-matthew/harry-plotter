"""Plot settings control components."""
from dash import dcc, html
import dash_bootstrap_components as dbc
from src.constants import DEFAULT_PLOT_SETTINGS


def create_plot_settings() -> dbc.Card:
    """Create plot settings controls."""
    settings = DEFAULT_PLOT_SETTINGS
    return dbc.Card([
        dbc.CardHeader("Plot Settings"),
        dbc.CardBody([
            dbc.Label("Plot Width (mm)"),
            dbc.Input(id='plot-width', type='number', value=settings.width, min=10, max=300),

            dbc.Label("Plot Height (mm)", className="mt-2"),
            dbc.Input(id='plot-height', type='number', value=settings.height, min=10, max=300),

            dbc.Label("Feed Rate (mm/min)", className="mt-2"),
            dbc.Input(id='feed-rate', type='number', value=settings.feed_rate, min=100, max=5000),

            dbc.Label("Pen Lift Height (mm)", className="mt-2"),
            dbc.Input(id='pen-lift', type='number', value=settings.pen_lift_height, min=1, max=20),
        ])
    ], className="mt-3")

