import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv("./data/mpg_plot.csv")

# Bubble Charts is the same as original marker but with som twist to visual mote that two attributes on the same
# two dimension plot using the (marker) dict

trace_1 = go.Scatter(
    x=csv["horsepower"],
    y=csv["mpg"],
    text=csv["name"],
    mode="markers",
    marker=dict(size=2 * csv["acceleration"], color=csv["cylinders"], showscale=True),
)

data = [trace_1]

layout = go.Layout(title="MGP Results", hovermode="closest")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="mpg_plot.html")
