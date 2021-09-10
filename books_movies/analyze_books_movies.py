"""
Created on Sun Nov 22 04:04:35 2020

@author: A

ideas: 
book graph
- timeline hovering over data
"""

import sqlite3
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from dash.dependencies import Input, Output


############
### MAIN ###
############
# direct_db = 'C:/Users/A/Documents/K/Projects/Interests Analysis/'
direct_db = ''
filename_db = 'media/interests.db'

# grab sql data and format as df
conn = sqlite3.connect(direct_db + filename_db)
cursor = conn.cursor()

cursor.execute('SELECT * FROM books')
df_books = pd.DataFrame(cursor.fetchall())

cursor.execute('PRAGMA table_info(books)')
df_books.columns = pd.DataFrame(cursor.fetchall())[1]

cursor.execute('SELECT * FROM movies')
df_movies = pd.DataFrame(cursor.fetchall())

cursor.execute('PRAGMA table_info(movies)')
df_movies.columns = pd.DataFrame(cursor.fetchall())[1]

conn.commit()
conn.close()

# format df_movies
df_movies['genres'] = ''
for i in range(len(df_movies)):
    string = ''
    for genre in ['genre 1', 'genre 2', 'genre 3', 'genre 4']:
        if df_movies[genre].loc[i]:
            string += df_movies[genre].loc[i] + ', '
    string = string[:-2]
    df_movies.loc[i, 'genres'] = string
df_movies = df_movies.sort_values('title')

# create dash/plotly
app = DjangoDash(name='books_movies_dash')
# app = dash.Dash()
# server = app.server

app.layout = html.Div([
        
    html.Div([
        html.H4(style={'font-family': 'Helvetica'}, children='Books read.'),
    
        html.Div(dash_table.DataTable(id='book-table',
            columns=[
#                {'name': 'Date finished', 'id': 'date finished'},
                {'name': 'Author', 'id': 'author'},
                {'name': 'Title', 'id': 'title'},
#                {'name': 'Year published', 'id': 'year published'},
            ],
            data=df_books.to_dict('records'),      
            page_size=15,                        
            style_data={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            style_cell={
                'whiteSpace': 'normal',
                'height': 'auto',
                'textAlign': 'left',
                'font-size': '12px',
                'font-family': 'Helvetica'
            },
#            style_table={'overflowX': 'auto'},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                }
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
            ), style={'padding-bottom':'30px'}
        ),

        html.Div(dcc.Graph(id='book-graph',
                           figure=px.bar(df_books, x='date finished', y=len(df_books)*[1],
                                         hover_data=['title', 'author'],
                                         title='Reading timeline',
                                         labels={'y': ''}),
                                         ),
        ),
    
    ], style={'width':'47%', 'float':'left', 'border-width':'2px', 'border-style':'dotted', 'border-color':'#7f7f7f', 'border-radius':'10px', 'padding':'10px'}),

#    html.Div([html.Hr()], style={'width':'2%', 'float':'left', 'height':'100%','border-style':'dotted'}),
    
    html.Div([
        html.H4(style={'font-family': 'Helvetica'}, children='Favourite movies.'),
        
        html.Div(dash_table.DataTable(id='movie-table',
            columns=[
                {'name': 'Favourite Movies', 'id': 'title'},
                {'name': 'Genres', 'id': 'genres'},
            ],
            data=df_movies.to_dict('records'),         
            page_size=15,                     
            style_data={
                'width': '100px', 'minWidth': '100px', 'maxWidth': '150px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            style_cell={
                'whiteSpace': 'normal',
                'height': 'auto',
                'textAlign': 'left',
                'font-size': '12px',
                'font-family': 'Helvetica'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                }
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
            ), style={'padding-bottom':'30px'},
        ),
    
        html.Div(dcc.Graph(id='histogram-movie-graph')),
    
        html.Div([
            html.Div([
                html.I(style={'font-family': 'Helvetica', 'width': '35%', 'float': 'left'}, children='Select category: ')
            ]),
            html.Div([dcc.RadioItems(id="x-dropdown",
                options=[{"label": x, "value": x} for x in ['genre', 'director', 'cast']],
                value='genre',
                labelStyle={'font-family':'Helvetica', 'margin': '0px 10px'}),
           ], style={'width':'48%', 'float':'left'}),
        ]), 
    
    ], style={'width':'47%', 'float':'right', 'border-width':'2px', 'border-style':'dotted', 'border-color':'#7f7f7f', 'border-radius':'10px', 'padding':'10px'}),
                                
])

@app.callback(
    Output("histogram-movie-graph", "figure"), 
    [Input("x-dropdown", "value")])
def update_movie_graph(value):
    if value != 'director':
        df_select = df_movies[value+' 1']
        for column in [value+' 2', value+' 3', value+' 4']:
            df_select = df_select.append(df_movies[column])
    else:
        df_select = df_movies[value]
    # plot histogram
    fig = px.bar(df_select.value_counts(), title='Most popular ' + value)
    # layout
    fig.update(layout_xaxis={'title':value})
    fig.update(layout_yaxis={'title':'# of movies'})
    fig.update(layout_showlegend=False)
    fig.update(layout_xaxis=dict(rangeslider=dict(visible=True), range=[-0.5, 9.5]))
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)
