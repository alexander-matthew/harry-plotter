"""Callbacks for the settings page."""
import logging
from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc

logger = logging.getLogger(__name__)


@callback(
    Output('connection-status', 'children'),
    Input('test-connection-btn', 'n_clicks'),
    State('serial-port', 'value'),
    State('baud-rate', 'value'),
    prevent_initial_call=True,
)
def test_connection(n_clicks: int, port: str, baud_rate: int):
    """Test plotter connection.

    TODO: Replace mock implementation with real hardware connection test.
    """
    if n_clicks:
        # In a real implementation, this would attempt to connect to the plotter
        logger.info("Testing connection on %s at %s baud", port, baud_rate)
        return dbc.Alert("Connection successful!", color="success")
    return ""

