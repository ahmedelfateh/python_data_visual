import pandas as pd
import numpy as np

# data = np.arange(0, 6).reshape(2, 3)
# print(data)
# redata = pd.DataFrame(data=data, columns=["A", "B", "C"], index=[])
# print(redata)


np.random.seed(101)
data = np.random.randint(1, 101, (100, 5))
redata = pd.DataFrame(data=data)
print(redata)
# print("\n")

redata.columns = ["f1", "f2", "f3", "f4", "lable"]
print(redata)

# salaries = pd.read_csv("salaries.csv")

# print(salaries)
# print("\n")

# print(salaries["Salary"])
# print("\n")

# print(salaries[["Salary"]])
# print("\n")

# print(salaries[["Name", "Salary"]])
# print("\n")

# print(salaries["Salary"].min())
# print("\n")

# print(salaries["Salary"].max())
# print("\n")

# print(salaries["Salary"].mean())
# print("\n")

# result = salaries["Age"] > 30
# print(result)
# print("\n")

# print(salaries[salaries["Age"] > 30])
# print("\n")

# print(salaries["Age"].unique())
# print("\n")

# print(salaries.columns)
# print("\n")

# print(salaries.info())
# print("\n")

# print(salaries.describe())
# print("\n")

# print(salaries.index)
# print("\n")
