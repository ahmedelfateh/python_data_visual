import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

csv = pd.read_csv("./data/mpg_plot.csv")

app = dash.Dash()

columns_list = []
for column in csv.columns:
    columns_list.append({"label": str(column), "value": column})

app.layout = html.Div(
    [
        dcc.Graph(id="graph"),
        html.Div(
            [dcc.Dropdown(id="xaxis", options=columns_list, value="mpg")],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [dcc.Dropdown(id="yaxis", options=columns_list, value="acceleration")],
            style={"width": "48%", "display": "inline-block"},
        ),
    ],
    style={"padding": 10},
)


@app.callback(
    Output("graph", "figure"), [Input("xaxis", "value"), Input("yaxis", "value")]
)
def update_plot(picked_xaxis, picked_yaxis):

    trace = go.Scatter(
        x=csv[picked_xaxis],
        y=csv[picked_yaxis],
        text=csv["name"],
        mode="markers",
        opacity=0.7,
        marker=dict(size=15),
    )

    data = [trace]

    return dict(
        data=data,
        layout=go.Layout(
            title="MPG Dashboard",
            xaxis=dict(title="Xaxis", type="log"),
            yaxis=dict(title="Yaxis"),
            hovermode="closest",
        ),
    )


if __name__ == "__main__":
    app.run_server(debug=True)