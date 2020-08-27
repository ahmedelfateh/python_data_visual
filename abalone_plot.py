import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv("./data/abalone_plot.csv", index_col=0)

sample_1 = np.random.choice(csv["rings"], 10, replace=False)
trace_1 = go.Box(y=sample_1, name="sample_1")

sample_2 = np.random.choice(csv["rings"], 10, replace=False)
trace_2 = go.Box(y=sample_2, name="sample_2")

sample_3 = np.random.choice(csv["rings"], 10, replace=False)
trace_3 = go.Box(y=sample_3, name="sample_3")

data = [trace_1, trace_2, trace_3]

layout = go.Layout(title="Abalone Samples")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="abalone_plot.html")
