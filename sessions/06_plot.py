import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks", color_codes=True)

kashti = sns.load_dataset("titanic")

# These charts are only created by just copy/pasting the code snippets - Don't know what it is.

# BarPlot
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=kashti)
plt.show()

# Count Plots
p = sns.countplot(x='sex', data=kashti, hue='class')
p.set_title("Plot for counting")
plt.show()

# ScatterPlot
g = sns.FacetGrid(kashti, row="sex", hue='alone')
g = (g.map(plt.scatter, "age", "fare").add_legend())
plt.show()

# print(titanic)
