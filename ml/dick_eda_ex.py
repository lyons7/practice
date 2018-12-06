# From here: https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
# Steps in data analysis:
# 1. Understand the problem. We'll look at each variable and do a philosophical analysis about their
# meaning and importance for this problem.
# 2. Univariable study. We'll just focus on the dependent variable ('SalePrice') and try to know a little bit more about it.
# 3. Multivariate study. We'll try to understand how the dependent variable and independent variables relate.
# 4. Basic cleaning. We'll clean the dataset and handle the missing data, outliers and categorical variables.
# 5. Test assumptions. We'll check if our data meets the assumptions required by most multivariate techniques.
# Libraries we'll be using here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

# load in data
df_train = data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/train.csv')
df_train.sample(5)

# Look at what variables we have
df_train.columns

# We need to understand our data! We can break down our data like so:
# 1. Variable: variable names
# 2. Type: for each variable, is it numeric or categorical?
# 3. Segment: Identification of a variable's segment. For this data we can say building, space or location.
# Basically, categories of things our variables describe. Could describe the building, could describe the
# space or location. Like HalfBath describes the building, for example.
# 4. Expectation: our thoughts on how the variable will influence our outcome (here SalesPrice)
# 5. Conclusions: our thoughts on how important the variable is.

# This is useful to identify things that might not be that useful / meaningful, or things that overlap (like if
# LandCountour gives flatness of property we don't really need landslope...)

# Let's investigate the independent variable
df_train['SalePrice'].describe()

# Min is larger than 0, which is good?
sns.distplot(df_train['SalePrice']);

# This shows a deviation from normal distribution, there is positive skewness? and peakedness. Not sure what these
# things mean...
# skewness and kurtosis
print("Skewness: %f" % df_train['SalePrice'].skew())
print("Kurtosis: %f" % df_train['SalePrice'].kurt())

# Look at relationship with other variables
#scatter plot grlivarea/saleprice
var = 'GrLivArea'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));

# Linear relationship between greater living area and Sales Price.

# For categorical variables:
#box plot overallqual/saleprice
var = 'OverallQual'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000);


# Missing data!
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)

# This is great, it tells you how much data is missing and what percent it is!
