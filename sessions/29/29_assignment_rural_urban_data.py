# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("../../data/FAOSTAT_data_rural_urban_population.csv")
# required_data = data.loc[0:, ["Element", "Year", "Value"]]

required_data = data[["Element", "Year", "Value"]]
# Convert into original Values
# required_data["Value"] = required_data["Value"].apply(lambda x: int(x * 1000))

# Convert into Million
required_data["Value"] = required_data["Value"].apply(lambda x: int(x // 1000))

# Task: Add a new data row for each year by adding rural and urban value
# Pseudo code:
# Read Value for year, sum the values of Value and add a new row

# Task: Getting values based on group
# for group_data in required_data.groupby(["Year"]):
#     print(group_data)
    # print("Total population in", x["Year"], "is: ", x)
    # print(group_data, "\n----", group_data[0], group_data[1].iloc[1], "\n=======")

# for index, row in required_data.groupby(["Year"]):
#     print(index, row)
#     print(row["Year"], row["Value"])

sum_values = required_data.groupby(["Year"])["Value"].sum()

sns.lineplot(x="Year", y="Value", hue="Element", data=required_data)
plt.title("Pakistan Rural and Urban Population 1990-2018")
plt.xlabel("Year")
plt.ylabel("Population (Million)")
plt.show()
