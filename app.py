import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

# Initialize Dash app with Bootstrap theme and pages support
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                use_pages=True,
                suppress_callback_exceptions=True,
                pages_folder="src/pages")

# Define the main layout with navigation
logging.basicConfig(level=logging.INFO)

app.layout = dbc.Container([
    # Navigation bar
    dbc.Navbar(
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.NavbarBrand("CNC Pen Plotter Control", className="text-white"),
                ], width=6),
                dbc.Col([
                    dbc.Badge("Ready", color="success", id="status-badge", className="float-end mt-2"),
                ], width=6),
            ], className="w-100"),
        ]),
        color="dark",
        dark=True,
        className="mb-3"
    ),
    
    # Navigation links
    dbc.Nav([
        dbc.NavItem(dbc.NavLink("Image Processing", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("Generative Art", href="/generate", active="exact")),
        dbc.NavItem(dbc.NavLink("Plot Settings", href="/settings", active="exact")),
    ], pills=True, className="mb-3"),
    
    # Page content will be inserted here
    dash.page_container,
    
    # Global stores for shared data
    dcc.Store(id='global-image-data'),
    dcc.Store(id='global-processed-data'),
    dcc.Store(id='global-gcode-data'),
    dcc.Store(id='global-svg-data'),
    
    # Hidden download components
    dcc.Download(id="global-download-gcode"),
    dcc.Download(id="global-download-svg"),
    
], fluid=True)

# Import callbacks to register them
import src.callbacks  # global callbacks
import src.pages.home_callbacks  # noqa: F401
import src.pages.generate_callbacks  # noqa: F401
import src.pages.settings_callbacks  # noqa: F401

if __name__ == '__main__':
    app.run(debug=True, port=8050)

