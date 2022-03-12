import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", color_codes=True)

titanic = sns.load_dataset("titanic")

# These charts are only created by just copy/pasting the code snippets - Don't know what it is.

# BarPlot
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# plt.show()

# Count Plots
# p1 = sns.countplot(x='sex', data=titanic, hue='class')
# p1.set_title("Plot for counting")
# plt.show()

# ScatterPlot
g = sns.FacetGrid(titanic, row="sex", hue='alone')
g = (g.map(plt.scatter, "age", "fare").add_legend())
plt.show()
