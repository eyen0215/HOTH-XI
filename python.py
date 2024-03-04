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

company100 = ["Dryer's Grand Ice Cream", 'Broadcom Inc.', 'Qualcomm Incorporated', 'Jabil Inc.', 'Cisco Systems, Inc.', 'Activision Blizzard', 'Ojai Valley Inn', 'Alvarado Hospital, LLC dba Alvarado Hospital Medical Center', 'Intel Corporation', 'Tower Semiconductor', 'Boardriders Wholesale, LLC', 'Southern California Pizza Company LLC', 'LinkedIn Corporation', 'Ajinomoto Foods North America, Inc.', 'California Institute of Technology', 'BILL Operations, LLC', 'El Dorado National (California), Inc.', 'Constellis', 'Surefox North America Inc', 'ResMEd Inc.', 'Rivian Automotive, LLC', 'Riot Games', 'Cruise LLC - Headquarters', 'Amyris, Inc.', 'Fashion Institute of Design & Merchandising FIDM', 'PayPal', "Dreyer's Grand Ice Cream", 'Foundation for California Community Colleges', 'Illumina, Inc.', 'Thermo Fisher Scientific', 'Sunrun Inc.', 'eBay Inc.', 'SK hynix NAND Product Solutions Corp. dba Solidigm', 'Becton, Dickinson and Company', 'Hawker Pacific Aerospace, Inc.', 'Bank of the West', "Mexi-Grill, LLC dba Javier's Newport Beach", 'Viasat, Inc.', 'Invitae Corporation', 'Flexport, Inc.', 'BMO Bank N.A. successor in interest to Bank of the West', 'David&rsquo;s Bridal, LLC', 'Twitch Interactive, Inc. SFO19 Facility', 'Terre du Soleil dba Auberge du Soleil', 'Kaiser Foundation Hospitals', 'Carbon Health', 'The Hotel del Coronado', 'ChargePoint, Inc.', 'Cruise LLC', 'Bloom Energy Corporation', 'Splunk Inc.', 'Snap Inc.', 'William Kreysler & Associates, Inc.', 'Amazon', 'Ericsson Inc.', 'Ace Hotel Group LLC at Ace Hotel Los Angeles', 'Los Angeles Times Communications LLC', 'Blue Shield of California', "David's Bridal, LLC", 'John Muir Health (JMH)', 'SPS Ventures Inc.', 'Nestle USA', 'Discord Inc.', 'Juniper Networks, Inc.', 'Headspace, Inc.', 'Farmers Group, Inc.', 'NuVasive, Inc.', 'Daifuku Services America Corporation', 'Charles Schwab & Co., Inc.', 'AVMAC LLC', 'ContextLogic Inc.', 'Gemological Institute of America, Inc. (GIA)', 'Acutus Medical, Inc.', 'Exelixis, Inc.', 'Pac-12 Enterprises, LLC', 'Plenty Unlimited Inc.', 'Paramount Global', 'Clari Inc.', 'Valiant Integrated Services', 'Roku, Inc.', 'Marvell Semiconductor, Inc.', 'SoCal Pizza Holdings, LLC', 'Owens-Brockway Glass Container, Inc.', 'City National Bank', 'AppFolio, Inc.', 'ITC Federal', 'Farmers Insurance Exchange', 'Lance Camper Mfg. Corp', 'Apple Inc.', 'Unity Technologies SF', 'Pixelberry Studios', 'Anaplan, Inc.', 'Sony Interactive Entertainment LLC', 'Western Digital', 'Lund Motion Products, Inc.', 'Atara Biotherapeutics', 'BlackLine Systems, Inc.', 'Aurora Solar Inc.', 'Brookfield Properties (USA II) LLC', 'Spotify USA Inc.']

layoff100 = [2336, 1267, 1258, 1129, 1081, 897, 870, 808, 762, 699, 698, 686, 625, 538, 521, 468, 425, 402, 386, 364, 340, 336, 330, 328, 322, 311, 306, 298, 291, 282, 281, 281, 270, 270, 260, 248, 239, 239, 238, 233, 228, 224, 218, 217, 207, 199, 197, 195, 182, 180, 176, 174, 171, 170, 170, 169, 168, 165, 165, 164, 162, 161, 160, 159, 158, 158, 157, 155, 155, 153, 152, 151, 147, 143, 141, 141, 141, 139, 137, 135, 131, 130, 130, 127, 127, 125, 124, 123, 121, 120, 120, 119, 118, 117, 117, 117, 116, 115, 113, 112]


# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Python Dashboard with Pycharts and Bar Graphs",
            style={
                'backgroundColor':'cadetblue',
                'color':'floralwhite',
                'text-align':'center'
            }),

    # Section for charts

    html.Div(className='chart-section', children=[
        # Pycharts graph
        html.Div(className='chart-box', children=[
            html.H2(""),
            dcc.Graph(
                id='pycharts-graph',
                figure={
                    'data': [
                        {'x': unique_dates, 'y': layoff_counts, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Layoffs by Day (By Effective Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
            
        ],style={'width': '100%', 'display': 'inline-block'}),
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='pycharts-graph2',
                figure={
                    'data': [
                        {'x': months, 'y': months_layoffs, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Number of Lay-offs per Month (By Effective Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
            
        ]),
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='pycharts-graph3',
                figure={
                    'data': [
                        {'x': updated_months, 'y': updated_months_layoffs, 'type': 'scatter', 'name': 'Pycharts Plot'},
                    ],
                    'layout': {
                        'title': 'Number of Lay-offs per Month (By Notice Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
            
        ]),

        # Bar graph
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='bar-graph',
                figure={
                    'data': [
                        {'x': updated_months, 'y': updated_months_layoffs, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Layoffs per Month (By Notice Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                        
                    }
                }
            )
        ]),
        
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='bar-graph2',
                figure={
                    'data': [
                        {'x': countysorted, 'y': countylayoffs_sorted, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Layoffs by County (By Notice Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
        ]),
        
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='bar-graph3',
                figure={
                    'data': [
                        {'x': countysorted2, 'y': countylayoffs_sorted2, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        'title': 'Sorted Layoffs by County (By Notice Date)',
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
        ]),
        html.Div(className='chart-box', children=[
            html.H2("PlaceHolder",
            style={
                'backgroundColor':'cadetblue',
                'color':'cadetblue',
                'text-align':'center'
            }),
            dcc.Graph(
                id='bar-graph4',
                figure={
                    'data': [
                        {'x': company100, 'y': layoff100, 'type': 'bar', 'name': 'Bar Graph'}
                    ],
                    'layout': {
                        
                        'title': "Top 100 Comopanies with Most Layoffs (Non-Closure)",
                        'yaxis': {'title': 'Number of Layoffs'},
                        'plot_bgcolor': '#ADD8E6',
                        'paper_bgcolor' : '#ADD8E6'
                    }
                }
            )
        ]),
    ]),

    # Text boxes
    html.Div(className='text-boxes', children=[
        html.H2("Text Boxes",
                style={'backgroundColor':'cadetblue',
                'color':'floralwhite',
                'text-align':'center'
                }),
        html.Div([
            html.P("Text Box 1: I LOVE MEN"),
            html.P("Text Box 2: I LOVE MEN"),
            html.P("Text Box 3: Even more sample text."),
        ])
    ])
])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
