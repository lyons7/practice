# Exploratory data analysis!
# Load in and label our data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data (from here: http://archive.ics.uci.edu/ml/datasets/Abalone?pagewanted=all)
# Make sure to fix column names too
# We want to have it say Sex, Length, Diameter, Height, Whole Weight, Shucked Weight, Viscera Weight, Shell Weight and Rings
data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/abalone.csv', names = ["sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])
# Take a peek
# data.head()
# Get information about the data
# data.info()

# "Exploratory Data Analysis (EDA) is used on the one hand to answer questions, test business assumptions, generate hypotheses for further analysis.
# On the other hand, you can also use it to prepare the data for modeling. The thing that these two probably have in common is a good knowledge of your
# data to either get the answers that you need or to develop an intuition for interpreting the results of future modeling.
#
# There are a lot of ways to reach these goals: you can get a basic description of the data, visualize it, identify patterns in it,
# identify challenges of using the data, etc."
# From: https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python

# .describe is a very important function!
data.describe()

# To get a feel for your dataset if it is a HUGE dataset, you can use sample to get a random sample
data.sample(10)

# You can also query the data. You can test some simple hypotheses about the data:
data.query('diameter < height') # Compare things -- see cases in which diameter is less than height and vise versa
# E.g. not too many cases in which abalone heights are more than the diameter

# Change data types
data['sex'] = data['sex'].astype(object) # Or int

# Drop columns
data.drop(columns=['B', 'C'])


# CHECK FOR MISSING VALUES
data.isnull().values.any()


# CHECK FOR MISSING VALUES FOR EVERYTHING AT THE SAME TIME AND GET RELATIVE PERCENTAGES OF THOSE VALUES
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data

# How to deal with missing values:

# If more than 15% of the data is missing, good to think about deleting that variable entirely (unless we NEED it)
# You can also look at relationships between data to get rid of some (like if things are correlated, keep one that
# has less missing values)!

# "Besides deletion, there are also methods that you can use to fill up cells if they contain missing
# values with so-called 'imputation methods'. If you already have a lot of experience with statistics, you’ll know that imputation is the
# process of replacing missing data with substituted values. You can either fill in the mean, the mode or the median. Of course, here you need
# to think about whether you want to take, for example, the mean or median for all missing values of a variable, or whether you want to
# replace the missing values based on another variable. For example, for data in which you have records that have features with
# categorical variables such as 'male' or 'female', you might also want to consider those before replacing the missing values, as the observations might
# differ from males and females. If this is the case, you might just calculate the average of the female observations and then fill out the missing values
# for other 'female' records with this average."

# "Estimate the value with the help of regression, ANOVA, logistic regression or another modelling technique. This is by far the most
# complex way to fill in the values."

# "You fill in the cells with values of records that are most similar to the one that has missing values. You can use KNN or K-Nearest Neighbors in
# cases such as these."

# Let's pretend we have missing information on abalone shell height

# Imputation
# Import NumPy
import numpy as np

# Calculate the mean
mean = np.mean(data.height)

# Replace missing values with the mean
data. = data.height.fillna(mean)

# Replace missing values with other string
data. = data.height.fillna("missing")

# You can also fill values forward or backward -- method depends on the DATA

# Drop rows with missing values
data.dropna(axis=0)

# Drop columns with missing values
data.dropna(axis=1)

# Interpolate -- have it use linear interpolation to 'guess' what value might be:
data.interpolate() # You can use method argument to do fancier interpolations


# OUTLIERS
# How to identify them: first we need to establish a threshold to know what is an outlier and what is not. We will thus
# STANDARDIZE the data. This means we'll convert all data values to have a mean of 0 and standard deviation of 1.

abalone_scaled = StandardScaler().fit_transform(data['whole_weight'][:,np.newaxis]);
low_range = abalone_scaled[abalone_scaled[:,0].argsort()][:10]
high_range= abalone_scaled[abalone_scaled[:,0].argsort()][-10:]
print('outer range (low) of the distribution:')
print(low_range)
print('\nouter range (high) of the distribution:')
print(high_range)

# What this tells us: low range seem all close to one another. Does -2 count as not that far from 0 tho?
# High range is farther from 0 and has more variation, but still isn't THAT crazy...

# We can also look at scatterplots for outliers
#bivariate analysis saleprice/grlivarea
var = 'whole_weight'
data2 = pd.concat([data['rings'], data[var]], axis=1)
data2.plot.scatter(x=var, y='rings', ylim=(0,40));


# How to deal with them
# If things seem to be following the trend and make sense that they might be valuable, keep them
# If they seem to be flukes and make no sense (like a very heavy abalone with very small number of rings -- delete)

# How you might delete them:
# data2.sort_values(by = 'whole_weight', ascending = False)[:2] # For example, if we wanted to delete ones with high weight and small # of rings
# data = data.drop(data[data['Id'] == 1299].index) # This would change depending on our data, just deleting these specific ones
# data = data.drop(data[data['Id'] == 524].index)


# Imbalanced classes
# How to deal with them



# Overfitting issues
# How to deal with them
