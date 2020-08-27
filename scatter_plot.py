import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)  # The Ultimate Answer to Life, The Universe and Everything

rand_x = np.linspace(1, 101, 100)
rand_y = np.random.randn(100)

trace_markers = go.Scatter(
    x=rand_x,
    y=rand_y + 5,
    mode="markers",
    marker=dict(size=12, line=dict(width=2, color="DarkSlateGrey")),
)

trace_lines = go.Scatter(x=rand_x, y=rand_y, mode="lines",)

trace_markers_lines = go.Scatter(x=rand_x, y=rand_y - 5, mode="lines+markers",)


data = [trace_markers, trace_lines, trace_markers_lines]

layout = go.Layout(
    title="test plot",
    xaxis=dict(title="X axis"),
    yaxis=dict(title="Y axis"),
    hovermode="closest",
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="scatter.html")

# pyo.plot(data, filename="scatter.html")
