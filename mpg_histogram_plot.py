import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv("./data/mpg_plot.csv")

trace_1 = go.Histogram(x=csv["mpg"], xbins=dict(start=0, end=100, size=1))

data = [trace_1]

layout = go.Layout(title="MGP Histogram", hovermode="closest")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="histogram_plot.html")
