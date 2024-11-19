import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Create the app
app = dash.Dash(__name__)

# Load dataset using Plotly
tips = px.data.tips()
labels = ['Рождаемость','Миграция','Смертность','Браки', 'Разводы']
values = [4500, 2500, 1053, 500, 100]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H1(children='Мониторинг министерства', className= 'header')]),  # Create a title with H1 tag
    # html.Label('Количество'),

    html.Div([
        html.H2('Выберите Регион:'),
        dcc.Dropdown(
            id='demo_drop',
            options=[
                {'label': 'Москва', 'value': 'cut'},
                {'label': 'Санкт-Петербург', 'value': 'clarity'},
                {'label': 'Краснодарский Край', 'value': 'color'}
            ],
            value='cut', className="dropdown"
        ),
        dcc.Graph(figure=fig)])])



if __name__ == '__main__':
   app.run_server(debug=True) # Run the Dash app