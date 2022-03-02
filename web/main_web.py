import requests

import dash
import dash_bootstrap_components as dbc
from dash import callback, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.LUX]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#  IMPORTING COMPONENTS
from landing_layout import menu

app.layout = html.Div(children=[menu])

#  CALLBACKS

if __name__ == '__main__':

    app.run_server(host='0.0.0.0', port=8080, debug=True)
