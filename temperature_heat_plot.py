import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import pandas as pd

csv_1 = pd.read_csv("./data/temperature_plot.csv")
csv_2 = pd.read_csv("./data/temperature_plot_1.csv")
csv_3 = pd.read_csv("./data/temperature_plot_2.csv")

trace1 = go.Heatmap(
    x=csv_1["DAY"],
    y=csv_1["LST_TIME"],
    z=csv_1["T_HR_AVG"],
    colorscale="Jet",  # plot color scale
    zmin=5,  # color scale min / max
    zmax=40,
)
trace2 = go.Heatmap(
    x=csv_2["DAY"],
    y=csv_2["LST_TIME"],
    z=csv_2["T_HR_AVG"],
    colorscale="Jet",
    zmin=5,
    zmax=40,
)
trace3 = go.Heatmap(
    x=csv_3["DAY"],
    y=csv_3["LST_TIME"],
    z=csv_3["T_HR_AVG"],
    colorscale="Jet",
    zmin=5,
    zmax=40,
)

fig = subplots.make_subplots(  # this manage the way the plot will appear
    rows=1,  # all traces will appear on single raw
    cols=3,  # very trace will appear as a column
    subplot_titles=("Area 1", "Area 2", "Area 3"),
    shared_yaxes=True,  # all will appear to share the sam y axis
)

fig.append_trace(trace1, 1, 1)  # 1 >> for the raw 1 >> for the column
fig.append_trace(trace2, 1, 2)  # 1 >> for the raw 2 >> for the column
fig.append_trace(trace3, 1, 3)  # 1 >> for the raw 3 >> for the column

fig["layout"].update(title="Hourly Temperatures for a week")
pyo.plot(fig, filename="temperature_heat_plot.html")
