'''
    This file contains the code for the line chart 1.
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
    fig = go.Figure(layout=go.Layout(
        updatemenus=[dict(type="buttons", direction="right"), ]))
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[0:5], 
        y=df['Exportations internationales'].iloc[0:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict(color='#2D99FF'),
        name="Exportations internationales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[0:5], y=df['Importations internationales'].iloc[0:5],
        hoverinfo='x+y',
        mode='lines',
        line=dict( color='#FF40EC'),
        name="Importations internationales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'].iloc[0:5], y=df['Solde commerciale international'].iloc[0:5],
        hoverinfo='x+y',
        mode='lines',
        name="Solde commerciale international",
          line= dict(dash="dashdot", 
            color= "rgb(254, 204, 25)")),
      
    )


    fig.update(frames=[
    go.Frame(
        data=[
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Exportations internationales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Importations internationales'].iloc[:k]),
            go.Scatter(x=df['Annee'].iloc[:k], y=df['Solde commerciale international'].iloc[:k])
            ]
    )
    for k in range(5, len(df)+5)])


    alena_line = [dict(type="line", x0=1987, y0=-10.914171223568989, x1=1987, y1=45.36925324781082,line=dict(color="#9A9A9A", width=3, dash="dot")),dict(type="line", x0=1994, y0=-10.914171223568989, x1=1994, y1=45.36925324781082,line=dict(color="#9A9A9A", width=3, dash="dot"))]
    annotations = [dict(text='ALENA', x=1994, y=30, textposition="top right", color="#9A9A9A"), dict(text='ALENA', x=1987, y=30, textposition="top right", color="#9A9A9A")]

    fig.update_layout(yaxis_range=(-10.914171223568989, 45.36925324781082), xaxis_range=(1981,2019), title={
        'text': "<b>Commerce International, Québec 1981-2019 (en pourcentage PIB) </b>",
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

                dict(label="Exportation",
                    method="update",
                    args=[{"visible": [False, True,False]},
                          {"showlegend": True}]),
                dict(label="Importation",
                    method="update",
                    args=[{"visible": [True, False,False]},
                          {"showlegend": True}]),

                dict(label="Solde Commerciale",
                    method="update",
                    args=[{"visible": [False, False, True]},
                          {"showlegend": True}]),

                dict(label="ALENA",
                        method="relayout",
                        args=[dict(shapes=alena_line, annotations=annotations)]),
              
                dict(label="All",
                    method="update",
                    args=[{"visible": [True, True, True]},
                          {"showlegend": True}]),
            ]))])

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
    fig.update_yaxes(title_text="Pourcentage du PIB")

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
