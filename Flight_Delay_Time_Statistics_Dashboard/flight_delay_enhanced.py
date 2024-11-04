# Import required libraries
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Load airline data from a public URL into a pandas DataFrame
# Note: Replace this URL with a local file path if running offline
airline_data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)

# Initialize the Dash application
app = dash.Dash(__name__)

# Define the layout of the app with header, input for year, and a placeholder for the graph
app.layout = html.Div(children=[
    html.H1(
        'Flight Delay Time Statistics',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 30}
    ),
    html.Div([
        "Input Year: ", 
        dcc.Input(id='input-year', value='2010', type='number', style={'margin': '10px'})
    ]),
    html.Br(),
    html.Div(id='output-graph')
])

# Define callback to update graph based on input year
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    Input(component_id='input-year', component_property='value')
)
def update_graph(entered_year):
    # Filter data for the selected year and create a Plotly figure
    filtered_df = airline_data[airline_data['Year'] == int(entered_year)]
    fig = px.histogram(
        filtered_df, 
        x='Month', y='ArrDelay', 
        title=f'Flight Delay Time per Month in {entered_year}',
        labels={'ArrDelay': 'Arrival Delay (minutes)', 'Month': 'Month'}
    )
    fig.update_layout(title_x=0.5)  # Center the title
    return dcc.Graph(figure=fig)

# Run the app on a local server
if __name__ == '__main__':
    app.run_server(debug=True)
