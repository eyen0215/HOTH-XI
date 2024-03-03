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
# with open("months_layoffs.txt") as filee:
#     for linee in filee:
#         c,d = linee.split(" ")
#         months.append(c)
#         months_layoffs.append(d)

#values for layoffs per month by notified date
updated_months = ['2023/04', '2023/05', '2023/06', '2023/07', '2023/08', '2023/09', '2023/10', '2023/11', '2023/12', '2024/01']
updated_months_layoffs = [501, 240, 4369, 5124, 6521, 7935, 8111, 7324, 6023, 11069]

#values for layoffs per county
county = ['Alameda County', 'Butte County', 'Contra Costa County', 'El Dorado County', 'Fresno County', 'Glenn County', 'Humboldt County', 'Imperial County', 'Kern County', 'Kings County', 'Los Angeles County', 'Madera County', 'Marin County', 'Mariposa County', 'Merced County', 'Monterey County', 'Napa County', 'Nevada County', 'Orange County', 'Placer County', 'Plumas County', 'Riverside County', 'Sacramento County', 'San Bernardino County', 'San Diego County', 'San Francisco County', 'San Joaquin County', 'San Luis Obispo County', 'San Mateo County', 'Santa Barbara County', 'Santa Clara County', 'Santa Cruz County', 'Shasta County', 'Solano County', 'Sonoma County', 'Stanislaus County', 'Tulare County', 'Ventura County', 'Yolo County']
county_layoffs = [3372, 169, 1566, 50, 437, 112, 10, 25, 2584, 44, 11960, 6, 164, 2, 158, 15, 245, 58, 4848, 229, 62, 1858, 1784, 2607, 7589, 4264, 598, 31, 2334, 298, 9736, 63, 149, 321, 408, 501, 1342, 1272, 523]


x_values=unique_dates
y_values=layoff_counts


countysorted = ['Los Angeles County', 'Santa Clara County', 'San Diego County', 'Orange County', 'San Francisco County', 'Alameda County', 'San Bernardino County', 'Kern County', 'San Mateo County', 'Riverside County', 'Sacramento County', 'Contra Costa County', 'Tulare County', 'Ventura County', 'San Joaquin County', 'Yolo County', 'Stanislaus County', 'Fresno County', 'Sonoma County', 'Solano County', 'Santa Barbara County', 'Napa County', 'Placer County', 'Butte County', 'Marin County', 'Merced County', 'Shasta County', 'Glenn County', 'Santa Cruz County', 'Plumas County', 'Nevada County', 'El Dorado County', 'Kings County', 'San Luis Obispo County', 'Imperial County', 'Monterey County', 'Humboldt County', 'Yuba County', 'Madera County', 'Mariposa County']
countylayoffs_sorted = [11960, 9736, 7589, 4848, 4264, 3318, 2607, 2584, 2334, 1858, 1784, 1566, 1342, 1272, 598, 523, 501, 437, 408, 321, 298, 245, 229, 169, 164, 158, 149, 112, 63, 62, 58, 50, 44, 31, 25, 15, 10, 7, 6, 2]

countysorted2 = [  'San Joaquin County', 'Yolo County', 'Stanislaus County', 'Fresno County', 'Sonoma County', 'Solano County', 'Santa Barbara County', 'Napa County', 'Placer County', 'Butte County', 'Marin County', 'Merced County', 'Shasta County', 'Glenn County', 'Santa Cruz County', 'Plumas County', 'Nevada County', 'El Dorado County', 'Kings County', 'San Luis Obispo County', 'Imperial County', 'Monterey County', 'Humboldt County', 'Yuba County', 'Madera County', 'Mariposa County']
countylayoffs_sorted2 = [ 598, 523, 501, 437, 408, 321, 298, 245, 229, 169, 164, 158, 149, 112, 63, 62, 58, 50, 44, 31, 25, 15, 10, 7, 6, 2]


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
                        'title': 'Number of Lay-offs per Month (By Effective Date)'
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
                        'title': 'Number of Lay-offs per Month (By Notice Date)'
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
                        {'x': updated_months, 'y': updated_months_layoffs, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Bar Graph'
                    }
                }
            )
        ]),
        
        html.Div(className='chart-box', children=[
            html.H2("Bar Graph"),
            dcc.Graph(
                id='bar-graph2',
                figure={
                    'data': [
                        {'x': countysorted, 'y': countylayoffs_sorted, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Bar Graph'
                    }
                }
            )
        ]),
        
        html.Div(className='chart-box', children=[
            html.H2("Bar Graph"),
            dcc.Graph(
                id='bar-graph3',
                figure={
                    'data': [
                        {'x': countysorted2, 'y': countylayoffs_sorted2, 'type': 'bar', 'name': 'Bar Graph'}
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
