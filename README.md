# Harry Plotter - CNC Pen Plotter Control

A multipage Dash application for controlling CNC pen plotters with image processing and generative art capabilities.

## Project Structure

```
harry-plottr/
├── app.py                    # Main application entry point
├── requirements.txt          # Python dependencies
├── main.py                   # Original single-file version (deprecated)
└── src/
    ├── __init__.py
    ├── constants.py          # Shared constants and configuration
    ├── callbacks.py          # Global callback functions
    ├── components/           # Reusable UI components
    │   ├── __init__.py
    │   ├── controls.py       # Control widgets (sliders, dropdowns, etc.)
    │   ├── preview.py        # Preview/visualization components
    │   └── upload.py         # File upload components
    ├── pages/                # Individual pages for multipage app
    │   ├── __init__.py
    │   ├── home.py           # Main image processing page
    │   ├── generate.py       # Generative art page
    │   └── settings.py       # Plot configuration page
    └── utils/                # Utility functions
        ├── __init__.py
        ├── generative_art.py # Art generation algorithms
        ├── image_processing.py # Image filtering and processing
        └── plotting.py       # Plotly figure creation and G-code/SVG export
```

## Features

### Image Processing Page (/)
- Upload and process images for plotting
- Image filters: brightness, contrast, threshold, invert
- Edge detection: Canny, Sobel, Laplacian
- Vectorization methods: contour, hatch, spiral, concentric, stipple
- Real-time preview of source and processed images

### Generative Art Page (/generate)
- Generate procedural art using various algorithms:
  - Flow Field
  - Spirograph
  - Voronoi Diagram
  - Circle Packing
  - And more...
- Customizable parameters: complexity, scale, random seed
- Preview generated artwork before plotting

### Plot Settings Page (/settings)
- Configure plot dimensions and feed rates
- Set pen lift height and other mechanical parameters
- Plotter connection settings (serial port, baud rate)
- Export options for G-code and SVG formats
- Connection testing

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser to `http://localhost:8050`

## Usage

1. **Image Processing**: Upload an image, adjust filters, and process for plotting
2. **Generative Art**: Create algorithmic artwork with customizable parameters
3. **Settings**: Configure your plotter and export settings

## Development

The application is built using:
- **Dash**: Web framework for Python
- **Plotly**: Interactive plotting
- **OpenCV**: Image processing
- **NumPy**: Numerical computations
- **Pillow**: Image handling

## Export Formats

- **G-code**: CNC machine instructions for plotting
- **SVG**: Vector graphics format for design software
