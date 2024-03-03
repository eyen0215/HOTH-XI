import dash
from flask import Flask
from dash import dcc, html
import plotly.graph_objs as go

# Sample data for charts



#read and process files
unique_dates = []
layoff_counts = []
with open('dates_layoffs') as openfileobject:
    for line in openfileobject:
        a,b = line.split(" ")
        unique_dates.append(a)
        layoff_counts.append(b)

months = ['2023/03', '2023/05', '2023/06', '2023/07', '2023/08', '2023/09', '2023/10', '2023/11', '2023/12', '2024/01', '2024/02', '2024/03', '2024/04', '2024/05', '2024/06', '2024/07', '2024/08']
months_layoffs = [224, 112, 555, 3576, 3858, 4413, 3937, 5433, 11425, 8515, 5308, 8954, 4942, 295, 2, 15, 73]
with open("months_layoffs.txt") as filee:
    for linee in filee:
        c,d = linee.split(" ")
        months.append(c)
        months_layoffs.append(d)

updated_months = ['2023/04', '2023/05', '2023/06', '2023/07', '2023/08', '2023/09', '2023/10', '2023/11', '2023/12', '2024/01']
updated_months_layoffs = [501, 240, 4369, 5124, 6521, 7935, 8111, 7324, 6023, 11069]

x_values=unique_dates
y_values=layoff_counts
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
                        {'x': unique_dates, 'y': layoff_counts, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Pycharts Graph'
                    }
                }
            )
            
        ]),
        html.Div(className='chart-box', children=[
            html.H2("Pycharts Graph"),
            dcc.Graph(
                id='pycharts-graph2',
                figure={
                    'data': [
                        {'x': months, 'y': months_layoffs, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Pycharts Graph'
                    }
                }
            )
            
        ]),
        html.Div(className='chart-box', children=[
            html.H2("Pycharts Graph"),
            dcc.Graph(
                id='pycharts-graph3',
                figure={
                    'data': [
                        {'x': updated_months, 'y': updated_months_layoffs, 'type': 'scatter', 'name': 'Pycharts Plot'},
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
            html.P("Text Box 1: I LOVE MEN"),
            html.P("Text Box 2: I LOVE MEN"),
            html.P("Text Box 3: Even more sample text."),
        ])
    ])
])

# Run the app
if __name__ == '__main__':
    print(months_layoffs)
    app.run_server(debug=True)
