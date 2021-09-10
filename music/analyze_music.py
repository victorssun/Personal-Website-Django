# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 04:04:35 2020

@author: A

ideas: 
graph 1
- genre/genre_detailed vs. year_downloaded/year_released (based on scollbar and table paras) [bar] {showcase temporal trend}

graph 2
- aggregate artist, genre/genre_detailed based on year_downloaded/released (based on scrollbar and table paras) [pie x2] {showcase favourite artist and genres}

table 1
- search songs based on all parameters and show filtered data on all graphs
"""

import sqlite3
import pandas as pd

import plotly.express as px

import dash
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table


############
### MAIN ###
############
#direct_db = 'C:/Users/A/Documents/K/Projects/Interests Analysis/'
direct_db = ''
filename_db = 'media/interests.db'

# grab sql data and format as df
conn = sqlite3.connect(direct_db + filename_db)
cursor = conn.cursor()

cursor.execute('SELECT * FROM music')
df = pd.DataFrame(cursor.fetchall())

cursor.execute('PRAGMA table_info(music)')
df.columns = pd.DataFrame(cursor.fetchall())[1]

conn.commit()
conn.close()

# create dash/plotly
x_selected = 'year released'
y_selected = 'genre'

app = DjangoDash(name='music_dash')
# server = app.server

app.layout = html.Div([
    # GRAPHS
    html.Div(dcc.Graph(id='temporal-graph'),
             style={'width': '48%', 'display': 'inline-block'}),
    html.Div(dcc.Graph(id='top-chart'),
             style={'width': '50%', 'float': 'right', 'display': 'inline-block'}),

    # PARAMETERS
    html.Div([
        html.Div([
            html.I(style={'font-family': 'Helvetica', 'width': '23%', 'float': 'left'}, children='Select year type: ')
        ]),
        html.Div([
            dcc.RadioItems(id="year-dropdown",
                           options=[{"label": x, "value": x}
                                    for x in ['year downloaded', 'year released']],
                           value='year released',
                           labelStyle={'font-family': 'Helvetica', 'margin': '0px 10px'}),
        ], style={'width': '48%', 'float': 'left'}),
        html.Br(),
        html.Br(),
        html.Div([
            html.I(style={'font-family': 'Helvetica', 'width': '23%', 'float': 'left'}, children='Select legend info: ')
        ]),
        html.Div([
            dcc.Dropdown(id="genre-dropdown",
                         options=[{"label": x, "value": x} for x in df[y_selected].unique()],
                         value=df[y_selected].unique(),
                         multi=True),
        ], style={'width': '73%', 'float': 'left'}),
    ], style={'width': '48%', 'display': 'inline-block'}
    ),

    html.Div([
        html.Div([
            html.I(style={'font-family': 'Helvetica', 'width': '22%', 'float': 'left'}, children='Select category: ')
        ]),
        html.Div([
            dcc.RadioItems(id="second-graph-dropdown",
                           options=[{"label": x, "value": x}
                                    for x in ['genre', 'genre detailed', 'artist']],
                           value='genre',
                           labelStyle={'font-family': 'Helvetica', 'margin': '0px 10px'}),
        ], style={'width': '48%', 'float': 'left'}),
        html.Br(),
        html.Br(),
        html.Div([
            html.I(style={'font-family': 'Helvetica', 'width': '20%', 'float': 'left'}, children='Select top range: ')
        ]),
        html.Div([
            dcc.RangeSlider(
                id='top-range-slider',
                min=1,
                max=50,
                step=1,
                value=[1, 10],
                marks={
                    1: {'label': '1'},
                    10: {'label': '10'},
                    20: {'label': '20'},
                    30: {'label': '30'},
                    40: {'label': '40'},
                    50: {'label': '50'}
                }
            ),
        ], style={'width': '75%', 'float': 'left'}),
        html.Div([
            html.I(style={'font-family': 'Helvetica', 'width': '20%', 'float': 'left'}, children='Select year range: ')
        ]),
        html.Div(
            dcc.RangeSlider(
                id='date-range-slider',
                min=1900,
                max=int(df[x_selected].max()),
                step=1,
                value=[1920, 2020],
                marks={
                    1900: {'label': '1900'},
                    1920: {'label': '1920'},
                    1940: {'label': '1940'},
                    1960: {'label': '1960'},
                    1980: {'label': '1980'},
                    2000: {'label': '2000'},
                    2020: {'label': '2020'}
                }
            ), style={'width': '75%', 'float': 'left'}
        ),
    ],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    # DATATABLE
    html.Div([
        html.H4(style={'font-family': 'Helvetica'}, children='Songs.'),
    ]),
    html.Div(dash_table.DataTable(id='song-table',
                                  columns=[
                                      {'name': 'Song', 'id': 'song'},
                                      {'name': 'Artist', 'id': 'artist'},
                                      {'name': 'Genre', 'id': 'genre'},
                                      {'name': 'Genre-detailed', 'id': 'genre detailed'},
                                      {'name': 'Year-released', 'id': 'year released'},
                                      {'name': 'Year-downloaded', 'id': 'year downloaded'}
                                  ],
                                  data=df.to_dict('records'),
                                  sort_action='native',
                                  filter_action='native',
                                  page_size=20,
                                  style_cell={
                                      'font-size': '12px',
                                      'font-family': 'Helvetica'
                                  },
                                  style_data={
                                      'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                                      'overflow': 'hidden',
                                      'textOverflow': 'ellipsis',
                                  },
                                  style_cell_conditional=[
                                      {
                                          'if': {'column_id': c},
                                          'textAlign': 'left'
                                      } for c in ['Date', 'Region']
                                  ],
                                  style_data_conditional=[
                                      {
                                          'if': {'row_index': 'odd'},
                                          'backgroundColor': 'rgb(248, 248, 248)'
                                      }
                                  ],
                                  style_header={
                                      'backgroundColor': 'rgb(230, 230, 230)',
                                      'fontWeight': 'bold'
                                  }

                                  ))
])

@app.callback(
    Output("temporal-graph", "figure"), 
    [Input("genre-dropdown", "value"),
    Input("year-dropdown", "value"),
    dash.dependencies.Input('date-range-slider', 'value')])
def update_graph1(genres, years, date_range):
    # plot histogram
    fig = px.histogram(df[df[y_selected].isin(genres)],
                          title='Song count vs. ' + years + ' by genre',
                          x=years, color=y_selected, # marginal="rug", 
                          nbins=len(range(int(df[years].min()), 
                                          int(df[years].max())+1)), 
#                                          range_x=[str(min(date_range)), str(max(date_range))],
                       )
    # layout
    fig.update(layout_xaxis={'title':years})
    fig.update(layout_yaxis={'title':'# of songs'})
    fig.update(layout_xaxis=dict(rangeslider=dict(visible=True), type="linear", range=[1920, 2020]))
    return fig

@app.callback(
    Output("top-chart", "figure"),
    [Input("year-dropdown", "value"),
    Input("second-graph-dropdown", "value"),
    Input('date-range-slider', 'value'),
    Input('top-range-slider', 'value')]
)
def update_graph2(years, second_graph_dropdown, date_range, top_range):
    # convert date range to list of strings for matching
    list_date = []
    for date in range(date_range[0], date_range[1]):
        list_date.append(str(date))
    # plot
    fig = px.bar(df[df[years].isin(list_date)][second_graph_dropdown].value_counts()[top_range[0]-1:top_range[1]-1],
                    title = 'Top ' + str(top_range[0]) + '-' + str(top_range[1]) + ' ' + second_graph_dropdown + ': ' + str(date_range[0]) + '-' + str(date_range[1]) + ' by ' + years)
    # layout
    fig.update(layout_showlegend=False)
    fig.update(layout_xaxis={'title':second_graph_dropdown})
    fig.update(layout_yaxis={'title':'# of songs'})
    return fig

@app.callback(
    Output('song-table', 'data'),
    [Input("genre-dropdown", "value"),
    Input("year-dropdown", "value"),
    Input('date-range-slider', 'value')])
def update_table(genres, years, date_range):
    list_date = []
    for date in range(date_range[0], date_range[1]):
        list_date.append(str(date))
    # plot
    return df[df[years].isin(list_date) & df[y_selected].isin(genres)].to_dict('records')

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)