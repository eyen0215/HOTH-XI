import dash
from dash import dcc, html
import plotly.graph_objs as go

# Sample data for charts
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 18]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Python Dashboard with Pycharts and Bar Graphs"),

    # Section for charts
    html.Div(className='chart-section', children=[
        # Pycharts graph
        html.Div(className='chart-box', children=[
            html.H2("Pycharts Graph"),
            dcc.Graph(
                id='pycharts-graph',
                figure={
                    'data': [
                        {'x': x_values, 'y': y_values, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Pycharts Graph'
                    }
                }
            )
        ]),

        # Bar graph
        html.Div(className='chart-box', children=[
            html.H2("Bar Graph"),
            dcc.Graph(
                id='bar-graph',
                figure={
                    'data': [
                        {'x': ['A', 'B', 'C', 'D', 'E'], 'y': [3, 5, 7, 9, 11], 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Bar Graph'
                    }
                }
            )
        ]),
    ]),

    # Text boxes
    html.Div(className='text-boxes', children=[
        html.H2("Text Boxes"),
        html.Div([
            html.P("Text Box 1: This is some sample text."),
            html.P("Text Box 2: More sample text."),
            html.P("Text Box 3: Even more sample text."),
        ])
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
