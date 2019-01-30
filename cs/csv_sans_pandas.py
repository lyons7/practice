# How to do csv manipulation without pandas
# Can't use any libraries except standard ones
import csv
import os
import sys
import collections
# What we want:
# * `top_10_occupations.txt`: Top 10 occupations for certified visa applications
# * `top_10_states.txt`: Top 10 states for certified visa applications

# records = []
os.chdir('/Users/katelyons/Documents/Insight/data challenges/challenge 6')
# Want to make this openable from any system -- so we'll get the current working directory where the file is to navigate from there
dir = os.getcwd()

with open(dir + '/input/h1b_input.csv', encoding='utf-8') as csvfile:
    for row in csv.reader(csvfile, delimiter = ';'):
