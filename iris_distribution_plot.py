import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

csv = pd.read_csv("./data/iris_plot.csv")

trace_1 = [csv[csv["class"] == "Iris-setosa"]["petal_length"]]
teace_2 = [csv[csv["class"] == "Iris-versicolor"]["petal_length"]]
trace_3 = [csv[csv["class"] == "Iris-virginica"]["petal_length"]]

hist_data = [trace_1, teace_2, trace_3]
group_labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename="iris_distribution_plot.html")
