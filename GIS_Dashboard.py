import dash
import dash_html_components as html
import dash_core_components as dcc

import datetime
from datetime import datetime as dt, datetime
import pandas as pd
import plotly.express as px


df = pd.read_csv('E:/DE2020Spring/Geo-Informatics/out4.csv')

fig = px.line(df, x='EC', y='TIME', title='EC sensor data')

fig2 = px.scatter(df, x='RTD', y='TIME', title='RTD sensor data')

fig3 = px.box(df, x='PH', y='TIME', title='PH sensor data')

source_image_url = 'https://52north.org/wp-content/uploads/2020/03/geospatial-sensing1.png'

app = dash.Dash()

app.layout = html.Div([
    html.Div(
        dcc.Graph(id='x-time-series', figure=fig)
    , style={'display': 'inline-block', 'width': '49%'}),
    html.Div([
        dcc.Graph(id='y-time-series', figure=fig2),
        dcc.Graph(id='z-time-series', figure=fig3),
    ], style={'display': 'inline-block', 'width': '49%', 'textAlign': 'center'})

    # html.Div(dcc.Slider(
    #     id='crossfilter-year--slider',
    #     min=df['EC'].min(),
    #     max=df['EC'].max(),
    #     value=df['EC'].max(),
    #     step=None,
    #     marks={str(time): str(time) for time in df['EC'].unique()}
    # ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])

if __name__ == '__main__':
    app.run_server(debug=True)