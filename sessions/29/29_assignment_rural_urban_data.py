# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Define required function to add population
def add_total(year, total):
    """Adds Total Population Value after each year row

        Args:
            year: Year to add total population

            total: Total population for the provided year

        Returns:
            None
    """
    rindex = list(required_data.loc[required_data['Year'] == year].index)[-1]
    new_index = rindex + 0.5
    required_data.loc[new_index] = {'Element': 'Total Population', 'Year': year, 'Value': total}


required_columns = ["Element", "Year", "Value"]
# load only required data
required_data = pd.read_csv("../../data/FAOSTAT_data_rural_urban_population.csv", usecols=required_columns)

# Current data is in Thousands, Convert into Million i.e. from K to M
required_data["Value"] = required_data["Value"].apply(lambda x: int(x // 1000))

year_sum = required_data.groupby(["Year"])["Value"].sum()

years_list = list(year_sum.index)

# add Total Population Value after each year in a loop
for index_year, total_value in year_sum.iteritems():
    add_total(index_year, total_value)

required_data = required_data.sort_index().reset_index(drop=True)

required_data.to_csv("../../data/rural_urban_total_population_pakistan.csv", index=False)
sns.lineplot(x="Year", y="Value", hue="Element", data=required_data)
plt.title("Pakistan Rural and Urban Population 1990-2018")
plt.xlabel("Year")
plt.ylabel("Population (Million)")
plt.show()

# Draw a bar graph
plt.figure(figsize=(15.0, 10.0))  # its important to mention figure size before generating the graph
barplot = sns.barplot(x="Year", y="Value", hue="Element", data=required_data, orient="v")
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=0, ha="center")
barplot.set_xticks(range(len(required_data.groupby('Year'))))
plt.tight_layout(pad=2.08)
plt.title("Pakistan Rural and Urban Population 1990-2018")
plt.xlabel("Year")
plt.ylabel("Population (Million)")
plt.figtext(x=0.65, y=0.03, s="Twitter: @abidalifsd")
plt.show()
