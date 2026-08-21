"""
Medical Operations Intelligence Dashboard — Milestone 2
Main entry point. Run from the REPO ROOT:
    python dashboard/app.py
Then open http://localhost:8050
"""

import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Medical Operations Intelligence Dashboard", style={"margin": "0"}),
                html.Div(
                    [
                        dcc.Link(page["name"], href=page["path"], style={"marginRight": "20px"})
                        for page in dash.page_registry.values()
                    ],
                    style={"marginTop": "10px"},
                ),
            ],
            style={
                "padding": "20px 24px",
                "borderBottom": "1px solid #e0e0e0",
                "fontFamily": "Arial, sans-serif",
            },
        ),
        dash.page_container,
    ],
    style={"fontFamily": "Arial, sans-serif"},
)

if __name__ == "__main__":
    app.run(debug=True)
