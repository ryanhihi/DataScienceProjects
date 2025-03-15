import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  sns.countplot(df[column], order=df[column].value_counts().index)
  # rotates the value labels slightly so they don’t overlap, also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
  # increases the variable label font size slightly to increase readability
  plt.xlabel(column, fontsize=12)
  plt.title(column + " Value Counts")
  plt.show()
  plt.clf()
