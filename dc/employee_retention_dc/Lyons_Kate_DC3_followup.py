# Main issue:
# Understanding why and when employees are most likely to leave can lead to actions to improve employee retention as well as planning new hiring in advance.
# In this challenge, you have a data set with info about the employees and have to predict when employees are going to quit by understanding the main drivers of employee churn.

# Questions:
# The goal is to predict employee retention and understand its main drivers.
# We already did some work before in visualizing and looking at the data, now we will try survival analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
from time import gmtime, strftime
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import os

os.chdir('/Users/katelyons/Documents/Insight/practice/dc/employee_retention_dc')
data = pd.read_csv('employee_retention.csv', index_col = 0)
data.info()

data.sample(5)

# We know employee_id and company_id are actually categories, so we want to make these strings
# Senority is number of years work experience, join and quit date should be in date format
data['employee_id'] = data['employee_id'].astype(object)
data['company_id'] = data['company_id'].astype(object)

# Check for missing values
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data

# We are missing some salary data which is a small percent of the data, so we can get rid of that
# ALSO temp_contracter automatically means they will leave, so get rid of all of those
data = data.dropna(subset=['salary'])
data = data[~data.dept.str.contains("temp_contractor")]
data.sample(10)

# Turn this into a survival analysis format
# We want DURATION (how long -- so dates minus each other) and OBSERVED -- whether or not we have censorship
# Observed should be straightforward, let's do that
data['observed'] = data.quit_date.fillna(0) # This says create a new column that puts a 0 for every instance in which the end date was not observed
data.loc[data['observed'].str.contains('-', na = False), 'observed'] = 1 # Put ones in the places we did observe

# Still need duration for censored people, so fill those NaTs with date of observation
# Want to do this before changing it to date time to make it easier
data['quit_date'] = data.quit_date.fillna('2015-12-13')

data['quit_date'] = pd.to_datetime(data['quit_date'])
data['join_date'] = pd.to_datetime(data['join_date'])

# data['duration'] = data['quit_date'] - data['join_date']

# Turn this into an integer so we can work with it
# data['duration'] = data['duration'].dt.days

# Actually, there is a built in function to get DURATION appropriate for SA
from lifelines.utils import datetimes_to_durations

start_date = data['join_date']
end_date = data['quit_date']
T, E = datetimes_to_durations(start_date, end_date)
print('T (durations): ', T)
print('E (event_observed): ', E)
data2 = data
data2['duration'],data2['observed'] = datetimes_to_durations(start_date, end_date)

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

# Made T and E up there ^

kmf.fit(T, event_observed=E)
kmf.survival_function_.plot()
plt.title('Survival function of employee churn');

# Timeline is days... end of the line is about 5 years (probably the length of our study)

# Median time for someone to work at this company
kmf.median_

# 1173 days is about 3 years.
# 424 days is about 1 year
# What did I do wrong? Why are these different...

# Graph different groups
# Get different group names
data.dept.value_counts()
customer_service = (data["dept"] == "customer_service")
engineer = (data["dept"] == "engineer")
data_science = (data["dept"] == "data_science")
data_science

# NEVERMIND -- no wonder we are getting inf, this is a binary thing, true false and these aren't two categories, there are more than just two things here!

# Remember that we are more interested WHY someone leaves, not necessarily when they will? Like what are the most influential reasons WHY they leave.

# Let's compare different departments:
depts = data2['dept'].unique()

for i,dept in enumerate(depts):
    ax = plt.subplot(2, 3, i+1)
    ix = data['dept'] == dept
    kmf.fit( T[ix], E[ix], label=dept)
    kmf.plot(ax=ax, legend=False)
    plt.title(dept)
    plt.xlim(0, 1000)
    if i==0:
        plt.ylabel('Frac. in staying after $n$ years')
plt.tight_layout()

for i,dept in enumerate(depts):
    ix = data['dept'] == dept
    kmf.fit( T[ix], E[ix], label=dept)
    print(dept, kmf.median_)

# Looking at a hazard curve
from lifelines import NelsonAalenFitter
naf = NelsonAalenFitter()

naf.fit(T,event_observed=E)
print(naf.cumulative_hazard_.head())
naf.plot()

# This hazard curve shows us that there is low hazard of someone leaving starting off, then it gets worse,
# once you stay for 500 days you stay at least a bit more, then exponentially it gets worse!


# SURVIVAL REGRESSION -- figuring out the influences of other aspects on whether or not someone survives
# Can't use regular linear regression. Want to use Cox's model or Aalen's additive model.

# Cox's Proportional Hazard model
# "The idea behind the model is that the log-hazard of an individual is a linear function of their static covariates
# and a population-level baseline hazard that changes over time" - from https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html

from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter

rossi_dataset = load_rossi()
cph = CoxPHFitter()
cph.fit(rossi_dataset, duration_col='week', event_col='arrest', show_progress=True)

cph.print_summary()
rossi_dataset.info()
rossi_dataset.sample(20)

# Try this with our data
# First have to make categorical columns into number columns and get rid of columns we don't want for regression
data2.head()
# Get rid of join_date, quit_date, event_observed, employee_id and make sure company_id and dept are categorical so they get dummified
data2 = data2.drop(['employee_id', 'join_date', 'quit_date'], axis = 1)
data3 = pd.get_dummies(data2)
data3.info()
data4 = data3.astype('int64')

cph.fit(data3, duration_col='duration', event_col='observed', show_progress=True)
cph.print_summary()

# Having an error that suggests a linear combination in my dataset.
# Look at correlation matrix
import matplotlib.pyplot as plt

import seaborn as sns
corr = data4.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)

# I guess senority and salary are correlated, which could be causing a problem? Let's see what happens when I get rid of it
# Graphs can be difficult to interpret -- let's do Pearson's coefficient
# data3.corr()['durations'].sort_values()
corrs = data3.corr()['durations']

# If I want to cut values, I want to do the absolute value to see what ones are closest to 0 in an ordered way
# Let's cut it down to 10 predictors
corrs2 = corrs.abs()
corrs2.sort_values()
# This is a little more informative -- we see that salary is up there, but not TOO much!

# Compare this with values of rossi_dataset
rossi_dataset.corr()['week'].sort_values()

# Maybe the problem is there are too many features? I could get rid of some of the companies I guess...
# Using abolute values, I'll get rid of everything before company_id_5
corrs2.sort_values()
data3.columns
data4 = data3.astype('int64')

data4 = data4.drop(['seniority','company_id_12','company_id_9','company_id_10','company_id_6','company_id_7','company_id_8','company_id_1','dept_design','company_id_11', 'company_id_5'], axis = 1)

data3.head()
data4 = data3.astype('int64')
data4.info()
data4.columns

cph.fit(data4, duration_col='duration', event_col='observed', show_progress=True)
cph.print_summary()

# Finally! Got rid of enough variables -- had too many features for the model to converge.

# Seems like salary is a big predictor of people leaving -- the lower the salary, the more likely they will leave?
# And if they work for company 2
# And if you are an engineer you are also more likely to leave

# Well aspects of this model suggest this way of modeling is not the best -- I don't think we have a linear
# relationship so shouldn't use it...
cph.score_
cph.check_assumptions(data4)
import pkg_resources
import lifelines
pkg_resources.get_distribution("lifelines").version
