import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

csv = pd.read_csv("./data/gdp_5Y_plot.csv")

app = dash.Dash()

y_value = []
for year in csv["year"].unique():
    y_value.append({"label": str(year), "value": year})

app.layout = html.Div(
    [
        dcc.Graph(id="graph"),
        dcc.Dropdown(id="year-picker", options=y_value, value=csv["year"].min()),
    ]
)


@app.callback(Output("graph", "figure"), [Input("year-picker", "value")])
def update_plot(picked_year):

    filter_csv = csv[csv["year"] == picked_year]

    traces = []

    for conti_name in filter_csv["continent"].unique():
        filter_continent_csv = filter_csv[filter_csv["continent"] == conti_name]

        traces.append(
            go.Scatter(
                x=filter_continent_csv["gdpPercap"],
                y=filter_continent_csv["lifeExp"],
                text=filter_continent_csv["country"],
                mode="markers",
                opacity=0.7,
                marker=dict(size=15),
                name=conti_name,
            )
        )

    return dict(
        data=traces,
        layout=go.Layout(
            title="Continant plot over Years",
            xaxis=dict(title="gdpPercap", type="log"),
            yaxis=dict(title="lifeExp"),
            hovermode="closest",
        ),
    )


if __name__ == "__main__":
    app.run_server(debug=True)
