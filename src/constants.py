"""
Constants and configuration for the CNC Pen Plotter application.
"""

# Generative art algorithms
GENERATIVE_ALGORITHMS = {
    'flow_field': 'Flow Field',
    'spirograph': 'Spirograph',
    'voronoi': 'Voronoi Diagram',
    'l_system': 'L-System Tree',
    'sine_waves': 'Sine Wave Interference',
    'circle_packing': 'Circle Packing',
    'maze': 'Maze Generation',
    'parametric': 'Parametric Equations'
}

# Vectorization methods for image processing
VECTORIZATION_METHODS = {
    'contour': 'Contour Only',
    'hatch': 'Hatch Fill',
    'spiral': 'Spiral Fill',
    'concentric': 'Concentric Fill',
    'stipple': 'TSP Stippling'
}

# Edge detection methods
EDGE_DETECTION_METHODS = {
    'none': 'None',
    'canny': 'Canny Edge',
    'sobel': 'Sobel Filter',
    'laplacian': 'Laplacian'
}

# Default plot settings
DEFAULT_PLOT_SETTINGS = {
    'width': 100,  # mm
    'height': 100,  # mm
    'feed_rate': 1000,  # mm/min
    'pen_lift_height': 5,  # mm
}

# Image processing defaults
DEFAULT_IMAGE_SETTINGS = {
    'brightness': 0,
    'contrast': 0,
    'threshold': 128,
    'invert': False,
    'edge_method': 'none',
    'edge_sensitivity': 50,
    'vector_method': 'contour',
    'hatch_spacing': 5,
    'hatch_angle': 45,
}

# Generative art defaults
DEFAULT_GENERATIVE_SETTINGS = {
    'algorithm': 'flow_field',
    'seed': 42,
    'complexity': 5,
    'scale': 1.0,
}