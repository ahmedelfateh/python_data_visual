import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash()

data = pd.read_excel("data.xls")

app.layout = html.Div(
    [
        dcc.Graph(
            id="Dash Chart",
            figure={
                "data": [
                    go.Scatter(
                        x=data["country"], y=data["life expectancy"], mode="markers"
                    )
                ],
                "layout": go.Layout(
                    xaxis={"title": "country"},
                    yaxis={"title": "life expectancy"},
                    hovermode="closest",
                ),
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
