"""Constants and configuration for the CNC Pen Plotter application."""
from dataclasses import dataclass


@dataclass
class PlotSettings:
    """Plot configuration defaults."""
    width: int = 100  # mm
    height: int = 100  # mm
    feed_rate: int = 1000  # mm/min
    pen_lift_height: int = 5  # mm


@dataclass
class ImageSettings:
    """Image processing default settings."""
    brightness: int = 0
    contrast: int = 0
    threshold: int = 128
    invert: bool = False
    edge_method: str = 'none'
    edge_sensitivity: int = 50
    vector_method: str = 'contour'
    hatch_spacing: int = 5
    hatch_angle: int = 45


@dataclass
class GenerativeSettings:
    """Generative art default settings."""
    algorithm: str = 'flow_field'
    seed: int = 42
    complexity: int = 5
    scale: float = 1.0


# Generative art algorithms
GENERATIVE_ALGORITHMS = {
    'flow_field': 'Flow Field',
    'spirograph': 'Spirograph',
    'voronoi': 'Voronoi Diagram',
    'l_system': 'L-System Tree',
    'sine_waves': 'Sine Wave Interference',
    'circle_packing': 'Circle Packing',
    'maze': 'Maze Generation',
    'parametric': 'Parametric Equations',
}

# Vectorization methods for image processing
VECTORIZATION_METHODS = {
    'contour': 'Contour Only',
    'hatch': 'Hatch Fill',
    'spiral': 'Spiral Fill',
    'concentric': 'Concentric Fill',
    'stipple': 'TSP Stippling',
}

# Edge detection methods
EDGE_DETECTION_METHODS = {
    'none': 'None',
    'canny': 'Canny Edge',
    'sobel': 'Sobel Filter',
    'laplacian': 'Laplacian',
}

# Default settings instances
DEFAULT_PLOT_SETTINGS = PlotSettings()
DEFAULT_IMAGE_SETTINGS = ImageSettings()
DEFAULT_GENERATIVE_SETTINGS = GenerativeSettings()

