# import all the libraries
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.express as px

# That external_stylesheets code is used to add Bootstrap CSS to your Dash app.
external_stylesheets = [
    {
        'rel': "stylesheet",
        'href': "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css",
        'integrity': "sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        'crossorigin': "anonymous"
    }
]

patient =pd.read_csv('state_wise_daily data.csv')
total=patient.shape[0]
active=patient[patient['Status']=='Confirmed'].shape[0]
recover=patient[patient['Status']=='Recovered'].shape[0]
deaths=patient[patient['Status']=='Deceased'].shape[0]

options = [
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

options1=[
    {'label': 'All', 'value': 'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}
]

options2=[
    {'label': 'All', 'value': 'Status'},
    {'label': 'Red Zone', 'value': 'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'}
]

# creating your Dash application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# add heading & alignment and add card , change color of card

app.layout = html.Div([
    html.H1('Covid-19 Impact Analysis', style={'color':'#fff', 'text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', className='text-light'),
                    html.H4(total,  className='text-light')
                ], className='card-body'),
            ], className='card bg-danger'),
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases', className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body'),
            ], className='card bg-info')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recover Cases', className='text-light'),
                    html.H4(recover, className='text-light')
                ], className='card-body'),
            ], className='card bg-warning')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Deaths', className='text-light'),
                    html.H4(deaths, className='text-light')
                ], className='card-body'),
            ], className='card bg-success')
        ],className='col-md-3')
    ],className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph',options=options1, value='All'),
                    dcc.Graph(id='graph'),
                ],className='card-body'),
            ],className='card bg-success'),
        ],className='col-md-6'),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown',options=options2, value='Status'),
                    dcc.Graph('the_graph')
                ],className='card-body'),
            ],className='card bg-info'),
        ],className='col-md-6'),
    ],className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body'),
            ],className='card'),
        ],className='col-md-12'),
    ],className='row')
], className="container")


@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):

    if type == 'All':
        return {'data': [go.Bar(x=patient['State'], y=patient['Total'])],
        'layout':go.Layout(title='State Total Count', plot_bgcolor='orange')
        }

    if type == 'Hospitalized':
        return {'data': [go.Bar(x=patient['State'], y=patient['Hospitalized'])],
        'layout':go.Layout(title='State Total Count', plot_bgcolor='orange')
        }

    if type == 'Recovered':
        return {'data': [go.Bar(x=patient['State'], y=patient['Recovered'])],
        'layout':go.Layout(title='State Total Count', plot_bgcolor='orange')
        }

    if type == 'Deceased':
        return {'data': [go.Bar(x=patient['State'], y=patient['Deceased'])],
        'layout':go.Layout(title='State Total Count', plot_bgcolor='orange')
        }

@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):

     if type == 'All':
         return {'data': [go.Line(x=patient['Status'], y=patient['Total'])],
                 'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}

     if type == 'Mask':
         return {'data': [go.Line(x=patient['Status'], y=patient['Mask'])],
                 'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}

     if type == 'Sanitizer':
         return {'data': [go.Line(x=patient['Status'], y=patient['Sanitizer'])],
                 'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}

     if type == 'Oxygen':
         return {'data': [go.Line(x=patient['Status'], y=patient['Oxygen'])],
                 'layout': go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}


@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame = patient.head(10), names=my_dropdown, hole=0.51)
    return (piechart)



# flask
# Runs the Dash app (with auto-reload & error debug) when the file is executed directly.
if __name__ == '__main__':
    app.run(debug=True)





