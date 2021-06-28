'''
    This file contains the code for the G3 bar-chart.
'''

import plotly.graph_objects as go
def plot_g3(df):
    '''
        Args:
            df: The dataframe to display
        Returns:
            The generated figure
    '''
    #initialiser les couleurs appropriees
    colors=['RGBA(50,171,96,0.65)',]*14
    colors[5]='#F1be03'
    #creatuib du barchart horizontal
    fig=go.Figure(go.Bar(
        x=df.PIB*100,
        y=df.Pays,
        hoverinfo='y,x',
        marker_color=colors,
        orientation='h'))
    fig.update_layout(yaxis=dict(autorange="reversed"))
    #changement des details (titre, template, nom des axes)
    fig.update_layout(template='plotly_white')
    fig.update_layout(title={
        'text':"<b>Part des exportations deans le PIB pour certains pays de l'OCDE et du Québec </b>"})
    fig.update_xaxes(title_text="Pourcentage %")
    fig.update_yaxes(title_text="Pays")
    fig.update_layout(hovermode="y")
    return fig


