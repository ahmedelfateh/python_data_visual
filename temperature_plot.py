import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


csv = pd.read_csv("./data/temperature_plot.csv")
days = ["TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", "MONDAY"]


# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(
        x=csv["LST_TIME"],
        y=csv[csv["DAY"] == day]["T_HR_AVG"],
        mode="markers+lines",
        name=day,
    )
    data.append(trace)

# Define the layout
layout = go.Layout(title="Temperature in week days")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="temperature_plot.html")

# Create a fig from data and layout, and plot the fig
