html.Div(
    className="container",
    children=[
        html.H1("404", style={'fontSize': '8rem', 'color': '#ff4757', 'textShadow': '0 0 10px rgba(255, 71, 87, 0.3)', 'margin': '0'}),
        html.P("Oops! The page you're looking for doesn't exist.", style={'fontSize': '1.5rem', 'color': '#cccccc', 'marginTop': '1rem', 'marginBottom': '1rem'}),
        html.A("Back to Home", href="/", className="home-link", style={'display': 'inline-block', 'marginTop': '2rem', 'padding': '1rem 2rem', 'backgroundColor': '#2196f3', 'color': 'white', 'textDecoration': 'none', 'borderRadius': '5px'})
    ],
    style={'textAlign': 'center', 'padding': '2rem', 'backgroundColor': '#2a2a2a', 'borderRadius': '10px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.3)', 'maxWidth': '90%', 'width': '500px'}
)