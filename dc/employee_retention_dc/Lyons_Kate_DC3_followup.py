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

# Turn this into a survival analysis format
# We want DURATION (how long -- so dates minus each other) and OBSERVED -- whether or not we have censorship
# Observed should be straightforward, let's do that
data['observed'] = data.quit_date.fillna(0)
data.loc[data['observed'].str.contains('-', na = False), 'observed'] = 1

# Still need duration for censored people, so fill those NaTs with date of observation
# Want to do this before changing it to date time to make it easier
data['quit_date'] = data.quit_date.fillna('None')

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


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

T = data["duration"]
E = data["observed"]

kmf.fit(T, event_observed=E)
kmf.survival_function_.plot()
plt.title('Survival function of employee churn');

# Timeline is days... end of the line is about 5 years (probably the length of our study)

# Median time for someone to work at this company
kmf.median_

# 1173 days is about 3 years.

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
depts = data['dept'].unique()

for i,dept in enumerate(depts):
    ax = plt.subplot(2, 3, i+1)
    ix = data['dept'] == dept
    kmf.fit( T[ix], E[ix], label=dept)
    kmf.plot(ax=ax, legend=False)
    plt.title(dept)
    plt.xlim(0, 1000)
    if i==0:
        plt.ylabel('Frac. in power after $n$ years')
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


rossi_dataset
