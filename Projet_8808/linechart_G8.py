'''
    This file contains the code for the line chart 4.
'''

import plotly.graph_objects as go

from plotly.subplots import make_subplots


def get_plot(df):
    '''
        Args:
            df: The dataframe to display
        Returns:
            The generated figure
    '''
    fig = go.Figure()
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Exportations internationales'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict(color='#2D99FF'),
        name="Exportations internationales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Exportations interprovinciales'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict(color='#0868C3'),
        name="Exportations interprovinciales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Importations internationales'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict( color='#FF40EC'),
        name="Importations internationales"),
    )

    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Importations interprovinciales'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict( color='#D60437'),
        name="Importations interprovinciales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Solde commerciale international'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        name="Solde commerciale international",
        line=dict(dash="dashdot", 
            color= "rgb(254, 204, 25)")),
    )

    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[:5], y=df['Solde commerciale interprovincial'].iloc[:5],
        hoverinfo='x+y',
        mode='lines',
        name="Solde commerciale interprovincial",
        line= dict(dash="dashdot", 
            color= "#928613")),
    )


    fig.update(frames=[
    go.Frame(
        data=[
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Exportations internationales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Exportations interprovinciales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Importations internationales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Importations interprovinciales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Solde commerciale international'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Solde commerciale interprovincial'].iloc[:k])
            ]
    )
    for k in range(5, len(df)+5)])


    alena_line = [dict(type="line",x0=1994, x1= 1994, y0= 150000, y1= -50000, line=dict(color="#9A9A9A", width=3, dash="dot")),dict(type="line", x0=1988, x1= 1988, y0= 150000, y1= -50000,line=dict(color="#9A9A9A", width=3, dash="dot"))]
    annotations = [dict(text="Entrée en vigueur <br>de l'ALE", x=1987.9610619469026, y=83006.94642109668, textposition="top right", color="#9A9A9A"), dict(text="Entrée en vigueur <br>de l'ALENA", x=1993.9465791960401, y=109442.30413852815, textposition="top right", color="#9A9A9A")]
    
    fig.update_layout(yaxis_range=(-50734.757161928705, 171161.90574053905), xaxis_range=(1981,2019), title={
        'text': "<b>Commerce International et interprovincial, Québec 1981-2019 (en millions de dollars enchainés de 2012) </b>",
        'xanchor': 'left',
        'yanchor': 'middle'},

        updatemenus=[
        dict(
            type="buttons",
            y=0.25,
            yanchor="bottom",
            x=1.05,
            xanchor="left",
            buttons=list([
                dict(label="None",
                     method="relayout",
                     args=[dict(shapes=[], annotations=[])]),
                dict(label="Play",
                        method="animate",
                        
                    args=[None, {"frame": {"duration": 50}}]),

                dict(label="International",
                    method="update",
                    args=[{"visible": [True, False,True,False, True , False]},
                          {"showlegend": True}]),
                dict(label="Interprovincial",
                    method="update",
                    args=[{"visible": [False, True,False,True, False , True]},
                          {"showlegend": True}]),
                dict(label="ALENA",
                        method="relayout",
                        args=[dict(shapes=alena_line, annotations=annotations)]),

    
              
                dict(label="All",
                    method="update",
                    args=[{"visible": [True, True, True]},
                          {"showlegend": True}]),
            ]))]
        )

    fig.update_layout(hovermode="x unified")
    return fig


    

def update_axes_labels(fig):
    '''

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    fig.update_xaxes(title_text="Année")
    fig.update_yaxes(title_text="Millions de dollars enchaînés de 2012")

    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    fig.update_layout(template='plotly_white')
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    fig.update_layout(    
        legend_title="")
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="left",
        x=0
        )
    )
    return fig
