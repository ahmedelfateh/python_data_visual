import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

csv = pd.read_csv(
    "./data/mocksurvey_plot.csv", index_col=0
)  # we used index_col=0 because the first col don't have name to be called in the x axis plot

trace_1 = go.Bar(
    x=csv.index,
    y=csv["Strongly Agree"],
    # orientation="h", # when using this you need to revers x and y values
    name="Strongly Agree",
    marker={"color": "#FFDF00"},
)
trace_2 = go.Bar(
    x=csv.index,
    y=csv["Somewhat Agree"],
    # orientation="h",
    name="Somewhat Agree",
    marker={"color": "red"},
)
trace_3 = go.Bar(
    x=csv.index,
    y=csv["Neutral"],
    # orientation="h",
    name="Neutral",
    marker={"color": "blue"},
)
trace_4 = go.Bar(
    x=csv.index,
    y=csv["Somewhat Disagree"],
    # orientation="h",
    name="Somewhat Disagree",
    marker={"color": "green"},
)
trace_5 = go.Bar(
    x=csv.index,
    y=csv["Strongly Disagree"],
    # orientation="h",
    name="Strongly Disagree",
    marker={"color": "#cd7f32"},
)

data = [trace_1, trace_2, trace_3, trace_4, trace_5]

layout = go.Layout(title="Survey Results", barmode="stack")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="mocksurvey_plot.html")
