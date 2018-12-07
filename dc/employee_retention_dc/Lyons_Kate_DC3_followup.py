# Main issue:
# Understanding why and when employees are most likely to leave can lead to actions to improve employee retention as well as planning new hiring in advance.
# In this challenge, you have a data set with info about the employees and have to predict when employees are going to quit by understanding the main drivers of employee churn.

# Questions:
# The goal is to predict employee retention and understand its main drivers.

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
# Senority is number of years work experience, join and quit date should be 
