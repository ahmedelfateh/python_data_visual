import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

csv = pd.read_csv("./data/flights_plot.csv")

trace1 = go.Heatmap(x=csv["year"], y=csv["month"], z=csv["passengers"])

data = [trace1]

layout = go.Layout(title="Flight data")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="flights_plot.html")
