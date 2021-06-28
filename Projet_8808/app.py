
# -*- coding: utf-8 -*-
import json

import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

import barchart_G2
import barchart_g3
import areachart
import linechart_G6
import linechart_G8
import chart_studio
import plotly.io as pio





app = dash.Dash(__name__)
app.title = 'Projet | INF8808'



'''
    Contains the server to run our application.
'''

#manipulation des données pour le graphique 
data2='assets/data/Data2.xlsx'
df2=pd.read_excel(data2,engine='openpyxl')    
df_exp=df2[df2['Type']=='Export']
df_imp=df2[df2['Type']=='Import']
fig2=barchart_G2.plot_g2(df_exp,df_imp)

#manipulation des données pour le graphique 3
data3='assets/data/Data3.xlsx'
df3=pd.read_excel(data3,engine='openpyxl')    
df3=df3.set_axis(['Ranking','Pays','Country','PIB'],axis=1,inplace=False)
fig3=barchart_g3.plot_g3(df3)

#manipulation des donnees pour le graphique 5
with open('assets/data/G10.json') as data_file:
    data = json.load(data_file)

df = pd.json_normalize(data, 'G10')

fig = areachart.get_plot(df)
fig = areachart.update_animation_hover_template(fig)
fig = areachart.update_axes_labels(fig)
fig = areachart.update_template(fig)
fig = areachart.update_legend(fig)
fig = areachart.add_animation(fig,df)

fig.update_layout(height=600, width=1200)
fig.update_layout(dragmode=False)

#manipulation des donnees pour les graphiques 1 et 4
with open('assets/data/G6.json') as data_file:
    data = json.load(data_file)

df_G6 = pd.json_normalize(data, 'G6')


fig1 = linechart_G6.get_plot(df_G6)
fig1 = linechart_G6.update_axes_labels(fig1)
fig1= linechart_G6.update_template(fig1)
fig1 = linechart_G6.update_legend(fig1)
fig1.update_layout(height=600, width=1100)
fig1.update_layout(dragmode=False)

with open('assets/data/G8.json') as data_file:
    data = json.load(data_file)

df_G8 = pd.json_normalize(data, 'G8')


fig4 = linechart_G8.get_plot(df_G8)
fig4 = linechart_G8.update_axes_labels(fig4)
fig4 = linechart_G8.update_template(fig4)
fig4 = linechart_G8.update_legend(fig4)
fig4.update_layout(height=600, width=1100)
fig4.update_layout(dragmode=False)


app.layout = html.Div(className='content', children=[



    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig1, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),


    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig2, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),
 
    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig3, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),

    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig4, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),
        

    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ])
])

chart_studio.tools.set_credentials_file(username='Rihab_Hajlaoui', api_key='wlWzciUmZyEtVWQdoItT')

chart_studio.tools.set_config_file(world_readable=False,
                             sharing='private')

pio.write_html(fig1, file='fig1.html', auto_open=True)
pio.write_html(fig2, file='fig2.html', auto_open=True)
pio.write_html(fig3, file='fig3.html', auto_open=True)
pio.write_html(fig4, file='fig4.html', auto_open=True)
pio.write_html(fig, file='fig.html', auto_open=True)
