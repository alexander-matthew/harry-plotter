"""
Image upload components for the CNC Pen Plotter application.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_upload_section():
    """Create image upload section."""
    return dbc.Card([
        dbc.CardHeader("Image Upload"),
        dbc.CardBody([
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select an Image')
                ]),
                style={
                    'width': '100%',
                    'height': '100px',
                    'lineHeight': '100px',
                    'borderWidth': '2px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px 0'
                },
                multiple=False
            ),
            html.Div(id='upload-status', className="mt-2"),
        ])
    ])


def create_file_info_section():
    """Create file information display section."""
    return dbc.Card([
        dbc.CardHeader("File Information"),
        dbc.CardBody([
            html.Div(id='file-info', children="No file selected"),
        ])
    ], className="mt-3")