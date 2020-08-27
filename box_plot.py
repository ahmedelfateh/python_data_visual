import plotly.offline as pyo
import plotly.graph_objs as go

# the box plot give the ability to plot continues data with categorical aspects

snodgrass = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]
twain = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]


trace_1 = go.Box(y=snodgrass, name="QCS")
trace_2 = go.Box(y=twain, name="MT")

data = [trace_1, trace_2]

layout = go.Layout(
    title="Three-letter-word >>> Quintus Curtius Snodgrass VS. Mark Twain"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="box_plot.html")
