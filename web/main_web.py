import requests

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input', value='enter something', type='text'),
    html.Div(id='output1', ),
    html.Button('Make api call', id='button', n_clicks=0),
    html.Div(id='output2', ),
])


#  CALLBACKS
@app.callback(Output(component_id='output2', component_property='children'),
              [Input("button", "n_clicks")])
def update_data(nclicks):
    if nclicks in [0, None]:
        return ('NO CLICO TODAVIA!')
    else:
        data = requests.get('http://vaccined_api:8000')
        return (data.text)


@app.callback(Output(component_id='output1', component_property='children'),
              [Input(component_id='input', component_property='value')])
def update_value(input_data):
    return ("Input: {0}".format(input_data))


if __name__ == '__main__':

    app.run_server(host='0.0.0.0', port=8080, debug=True)
