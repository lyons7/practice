import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.feature_selection import RFE, f_regression
from sklearn.linear_model import (LinearRegression, Ridge, Lasso, RandomizedLasso)
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
import math
import statsmodels.api as sm
import statsmodels.formula.api as smf
# difference of lasso and ridge regression is that some of the coefficients can be zero i.e. some of the features are
# completely neglected
from sklearn.model_selection import train_test_split

data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/abalone.csv', names = ["sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])

data.info()

# Want to know what is the best predictor of the number of rings of an abalone
# Ordinary Least Squares Regression
# We do have a normal distribution so this is an okay choice

# We will use Statsmodels. "Statsmodel is a Python library designed for more statistically-oriented approaches to data
# analysis, with an emphasis on econometric analyses. It integrates well with the pandas and numpy libraries we covered
# in a previous post. It also has built in support for many of the statistical tests to check the quality of the fit and a
# dedicated set of plotting functions to visualize and diagnose the fit. Scikit-learn also has support for linear regression,
# including many forms of regularized regression lacking in statsmodels, but it lacks the rich set of statistical tests and
# diagnostics that have been developed for linear models."
# From here: https://blog.datarobot.com/ordinary-least-squares-in-python

mod = smf.ols(formula='rings ~ length + diameter + C(sex) + height + whole_weight + shucked_weight + viscera_weight + shell_weight', data=data)
res = mod.fit()
print(res.summary())


# Do this from scratch:
# Let's say we just want to look at shucked_weight and rings
X = data.shucked_weight
y = data.rings


# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))

mean = mean(X)

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

variance(X, mean)

# Get variance and mean of outcome
mean_y = mean(y)
