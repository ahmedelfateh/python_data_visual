import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

csv_data = pd.read_csv("./data/population_plot.csv")

new_csv_data = csv_data[csv_data["DIVISION"] == "1"]  # Filter data with the DIVISION==1

new_csv_data.set_index("NAME", inplace=True)  # index new_csv_data with the name

pop_col_list = [
    col for col in new_csv_data.columns if col.startswith("POP")
]  # get list of all population col

new_csv_data = new_csv_data[pop_col_list]  # filter new_csv_data with the pop col

data = [
    go.Scatter(
        x=new_csv_data.columns,  # set col as x
        y=new_csv_data.loc[name],  # set name raw as y
        mode="markers+lines",
        name=name,  # set y value to the raw value
    )
    for name in new_csv_data.index  # iterate over the columns and raw to populate x and y
]

layout = go.Layout(title="Population Estimates of the Six New England States")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="population_plot.html")

