# Exploratory data analysis!
# Load in and label our data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data (from here: https://archive.ics.uci.edu/ml/datasets/Pittsburgh+Bridges)
# Make sure to fix column names too
data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/bridges.data.version2.csv', names = ["id", "river", "location", "erected", "purpose", "length", "lanes", "clear-g", "t-or-d","material","span","rel-l", "type"], na_values="?")
# Take a peek
data.head()

# Because we have ? for missing values, we'll read these in so ? becomes Nans. (See above ^)

# Get information about the data
data.info()

# Value counts
data.river.value_counts()

data.river.value_counts(normalize=True)

# To do this all together
s = data.river.value_counts()
s_len = s / len(data.index)

res = pd.concat([s, s_len], axis=1)\
        .set_axis(['count', 'pct'], axis=1, inplace=False)

print(res)


# Cross tabs!
pd.crosstab(data.river, data.purpose)

pd.crosstab(data.erected, data.purpose)

# We can also get total counts
pd.crosstab(data.river, data.purpose, margins=True, margins_name="Total")

# Get percent break down
pd.crosstab(data.river, data.purpose, normalize = True, margins_name = "Total", margins = True)

# Get breakdown of all column
pd.crosstab(data.river, data.purpose, normalize='index')

# Do more than one group at a time
pd.crosstab(data.purpose, [data.river, data.erected], margins = True, margins_name = "Total")

# Graph
# Frequency Distribution
river_count = data['river'].value_counts()
sns.set(style="darkgrid")
sns.barplot(river_count.index, river_count.values, alpha=0.9)
plt.title('Distribution of Bridges', fontsize = 14)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('River', fontsize=12)
plt.show()
