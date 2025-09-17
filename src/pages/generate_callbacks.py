"""Callbacks for the generative art page."""
import logging
import numpy as np
from dash import Input, Output, State, callback

from src.utils.generative_art import generate_art
from src.utils.image_processing import extract_paths
from src.utils.plotting import create_image_figure, create_empty_figure

logger = logging.getLogger(__name__)


@callback(
    Output('random-seed', 'value'),
    Input('randomize-seed', 'n_clicks'),
    prevent_initial_call=True,
)
def randomize_seed(n_clicks: int) -> int:
    """Generate a random seed for reproducibility."""
    return int(np.random.randint(0, 10000))


@callback(
    Output('main-preview', 'figure'),
    Output('gen-path-stats', 'children'),
    Input('generate-btn', 'n_clicks'),
    State('gen-algorithm', 'value'),
    State('random-seed', 'value'),
    State('complexity-slider', 'value'),
    State('scale-slider', 'value'),
)
def generate_and_preview(
    n_clicks: int | None,
    algorithm: str,
    seed: int,
    complexity: int,
    scale: float,
):
    """Generate art and create preview."""
    if not n_clicks:
        return create_empty_figure(), "Click 'Generate Art' to create artwork"

    try:
        np.random.seed(seed)
        generated_img = generate_art(algorithm, complexity, scale)
        paths = extract_paths(generated_img, 'contour')
        stats = f"Algorithm: {algorithm} | Paths: {len(paths)} | Est. time: {len(paths) * 2} seconds"
        fig = create_image_figure(generated_img, f"Generated Art - {algorithm}")
        return fig, stats
    except Exception as exc:  # pragma: no cover - placeholder
        logger.error("Generative art failed: %s", exc)
        return create_empty_figure(), f"Error: {exc}"

