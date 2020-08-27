import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv("./data/olympics_plot.csv")

trace_1 = go.Bar(x=csv["NOC"], y=csv["Gold"], name="Gold", marker={"color": "#FFDF00"})
trace_2 = go.Bar(
    x=csv["NOC"], y=csv["Silver"], name="Silver", marker={"color": "#c0c0c0"}
)
trace_3 = go.Bar(
    x=csv["NOC"], y=csv["Bronze"], name="Bronze", marker={"color": "#cd7f32"}
)

data = [trace_1, trace_2, trace_3]

layout = go.Layout(title="olympics")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="olympics_plot.html")
