import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv("./data/intervals_durations_plot.csv")

app.layout = html.Div(
    [
        dcc.Graph(
            id="old_faithful",
            figure={
                "data": [go.Scatter(x=df["X"], y=df["Y"], mode="markers")],
                "layout": go.Layout(
                    title="Intervals v Durations",
                    xaxis={"title": "Duration"},
                    yaxis={"title": "Interval"},
                    hovermode="closest",
                ),
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
