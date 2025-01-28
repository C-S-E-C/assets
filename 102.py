html.Div([
    html.H1('Error 102 - Processing Error', style={'textAlign': 'center', 'marginTop': 50}),
    dcc.Markdown('''
        ## Oops! Something went wrong.

        We are currently experiencing a processing error (Error 102). Please try again later or contact support for assistance.
    ''', style={'textAlign': 'center', 'marginTop': 50}),
    html.Div([
        html.A('Go Back', href='/'),
        html.A('Contact Support', href='mailto:support@example.com', style={'marginLeft': 20})
    ], style={'textAlign': 'center', 'marginTop': 50})
])