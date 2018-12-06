import pandas as pd
from scipy.stats.stats import pearsonr
import numpy as np
from scipy import stats

# Correlation and regression lines


# Karl Pearson's Coefficient
# A.K.A. Pearson correlation coefficient. Used to measure the strength between two variables. Also known as a
# Pearson R test. "When conducting a statistical test between two variables, it is a good idea to conduct a Pearson
# correlation coefficient value to determine just how strong that relationship is between those two variables."
# From here: https://study.com/academy/lesson/pearson-correlation-coefficient-formula-example-significance.html

# What we are doing is coming up with coefficient values. These can range from -1.0 to 1.0. If it is negative, that
# means the relationship between our variables is negatively correlated. If it positive... it's positively correlated.
# 0 means no relationship at all.

# This is a measure of LINEAR CORRELATION

# More from Scipy: Calculate a Pearson correlation coefficient and the p-value for testing non-correlation.
# The Pearson correlation coefficient measures the linear relationship between two datasets. Strictly speaking,
# Pearson’s correlation requires that each dataset be normally distributed, and not necessarily zero-mean. Like other
# correlation coefficients, this one varies between -1 and +1 with 0 implying no correlation. Correlations of -1 or +1
# imply an exact linear relationship. Positive correlations imply that as x increases, so does y.
# Negative correlations imply that as x increases, y decreases.

# The p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Pearson
# correlation at least as extreme as the one computed from these datasets. The p-values are not entirely reliable but are
# probably reasonable for datasets larger than 500 or so.
# From: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html#scipy.stats.pearsonr

# Let's use our abalone example:
data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/abalone.csv', names = ["sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])
data.sample(5)

# Let's look at correlations between ... sex and viscera_weight
# Can we look at categories? I don't think so... NO WE CANNOT SO let's do viscera and rings
viscera = np.array(data.viscera_weight)
rings = np.array(data.rings)

stats.pearsonr(viscera, rings)

# This gives us Pearson's correlation coefficient and the p value
# This suggests viscera weight and ring number are positively correlated

# How to do this with all of your variables at once. Note viscera_weight is the same value as calculated on its own.
data.corr()['rings'].sort_values()
