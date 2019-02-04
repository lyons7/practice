# How to do csv manipulation without pandas
# Can't use any libraries except standard ones
import csv
import os
import sys
import collections
# What we want:
# Get a count of the number of entries of abalone records that have more than 10 rings

# records = []
os.chdir('/Users/katelyons/Documents/Insight/practice/ml')
# Want to make this openable from any system -- so we'll get the current working directory where the file is to navigate from there
dir = os.getcwd()
# This one is tricky because we don't have column names. We can just access the column by it's index (it's the 9th one, we could just
# know that OR we can just go in and change the file to have col names...
with open(dir + '/abalone.csv', encoding='utf-8') as csvfile:
    # no_entries = collections.Counter() # Maybe we don't need a counter
    sum = 0 # This would serve as our base, keep adding to get the total sum
    count = 0 # Just a simple counter to see how many instances we have
    for row in csv.reader(csvfile, delimiter = ','):
        # no_entries[row[8]] += 1 # Use a counter
        if int(row[8]) > 10: # If what is at that spot is more than 10
        # no_entries += 1 # Increase our counter by one
            count += 1
            sum = int(row[8]) + sum

count
sum

# Don't need a counter! Can just sum them up




# How to do this in pandas:
import pandas as pd
data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/abalone.csv', names = ["sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])
data.columns
# Get entries more than 10 rings
more_than_ten = data[data['rings'] > 10]
more_than_ten.groupby('rings').size() # Treats these as a category
# more_than_ten.groupby('rings').count() # Gives you a breakdown by category
more_than_ten.shape[0] # Tells you number of rows
more_than_ten['rings'].sum() # Tells you the total of the column (sum of column values)
