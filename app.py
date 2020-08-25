import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
colors = {"background": "gray", "text": "white"}
app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Dash", style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="Dash for Python.",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(
            id="Graph1",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": u"Montréal",
                    },
                    {"x": [1, 2, 3], "y": [10, 7, 9], "type": "bar", "name": u"Cairo",},
                ],
                "layout": {
                    "plot_bgcolor": colors["background"],
                    "paper_bgcolor": colors["background"],
                    "font": {"color": colors["text"]},
                },
            },
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
