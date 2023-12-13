# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from pymongo import MongoClient

# MongoDB connection setup
mongo_conn_string = 'mongodb+srv://bdat1004:1004@1004.vza4tnd.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_conn_string)
db = client['economic_data']
economic_series_collection = db['economic_series']

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# Function to fetch data from MongoDB
def fetch_data_from_mongo(series_id):
    document = economic_series_collection.find_one({'id': series_id})
    if document:
        return document['observations']
    else:
        return []

# App layout
app.layout = html.Div([
    html.H1("Economic Data Dashboard"),
    
    # Dropdown for series selection
    html.Div([
        dcc.Dropdown(
            id='series-dropdown',
            options=[
                {'label': 'Real Gross Domestic Product (GDPC1)', 'value': 'GDPC1'},
                {'label': 'Unemployment Rate (UNRATE)', 'value': 'UNRATE'},
                {'label': 'Inflation Rate (CPIAUCNS)', 'value': 'CPIAUCNS'},
            ],
            value='GDPC1',  # Default selection
            style={'width': '250px'}
        )
    ], style={'width': '300px', 'display': 'inline-block'}),

    # Plotly chart element
    dcc.Graph(id='line-chart')
])

# Callback to update Plotly chart
@app.callback(
    Output('line-chart', 'figure'),
    [Input('series-dropdown', 'value')]
)
def update_chart(selected_series):
    data_from_mongo = fetch_data_from_mongo(selected_series)

    if not data_from_mongo:
        return px.scatter(title='No Data Available')

    # Create Plotly figure
    fig = px.line(data_from_mongo, x='date', y='value', title=f'Economic Series - {selected_series}')
    fig.update_layout(xaxis_title='Date', yaxis_title='Value')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
