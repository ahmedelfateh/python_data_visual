import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv("./data/abalone_plot.csv")

trace_1 = go.Histogram(x=csv["length"], xbins=dict(start=0, end=1, size=0.02))

data = [trace_1]

layout = go.Layout(title="abalone Length Histogram", hovermode="closest")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="abalone_histogram_plot.html")
