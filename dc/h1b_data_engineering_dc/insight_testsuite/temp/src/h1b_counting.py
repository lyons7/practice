# Can't use any libraries except standard ones
import csv
import os
import sys
import collections
# What we want:
# * `top_10_occupations.txt`: Top 10 occupations for certified visa applications
# * `top_10_states.txt`: Top 10 states for certified visa applications

# records = []
# os.chdir('/Users/katelyons/Documents/Insight/data challenges/challenge 6')
# Want to make this openable from any system -- so we'll get the current working directory where the file is to navigate from there
dir = os.getcwd()

# Loop that is opening the file and counting instances of statuses, occupations and states
with open(dir + '/input/h1b_input.csv', encoding='utf-8') as csvfile:
    status = collections.Counter()
    occupation = collections.Counter()
    state = collections.Counter()
    for row in csv.reader(csvfile, delimiter=';'):
        try: # Have to do this because indexes are not the same for every file -- we have to go by their name!
            status_index = row.index("CASE_STATUS") # This is saying, find out what the index is for this value
            occupation_index = row.index("JOB_TITLE")
            state_index = row.index("EMPLOYER_STATE")
        except ValueError:
            status[row[status_index]] += 1 # Then we use the value we set earlier to get other things in this column
            occupation[row[occupation_index]] += 1
            state[row[state_index]] += 1


# Open a text file and start putting stuff into it
f = open(dir+"/output/top_10_occupations.txt","w+")
f.write('TOP_OCCUPATIONS; NUMBER_CERTIFIED_APPLICATIONS; PERCENTAGES\n')
for occ, i in occupation.most_common(10):
    f.write(occ+';%d'%(i)+';%.1f'%((i/status['CERTIFIED'])*100)+'%'+'\n')
f.close()

f2 = open(dir+"/output/top_10_states.txt","w+")
f2.write('TOP_STATES; NUMBER_CERTIFIED_APPLICATIONS; PERCENTAGES\n')
for stat, i in state.most_common(10):
    f2.write(stat+';%d'%(i)+';%.1f'%((i/status['CERTIFIED'])*100)+'%'+'\n')
f2.close()

# i = 12
# i/status['CERTIFIED']
#
# for occ, i in occupation.most_common(10):
#     print('TOP_OCCUPATIONS; NUMBER_CERTIFIED_APPLICATIONS; PERCENTAGES\n',occ,';',i)
    # print('Number of Certified Applications: %s' % status['CERTIFIED'])
# print('TOP_OCCUPATIONS; NUMBER_CERTIFIED_APPLICATIONS; PERCENTAGES\n''hello')

# print(occupation.most_common(10))
# print(state.most_common(10))
# [occupation.most_common(10)[0][0]]
#
# for occupation, i in occupation.most_common(10):
#     print (occupation, i)

# for occpuation, count in occupation.most_common(10):
#     print('%s: %d' % (occupation, count))
# print('TOP_OCCUPATIONS;')

# Prior attempts down here
# with open(dir + '/input/h1b_input.csv', encoding='utf-8') as csvfile:
    # reader = csv.DictReader(csvfile, delimiter=';')# , quoting=csv.QUOTE_NONE, fieldnames=('LCA_CASE_NUMBER','STATUS','LCA_CASE_SUBMIT','DECISION_DATE','VISA_CLASS','LCA_CASE_EMPLOYMENT_START_DATE','LCA_CASE_EMPLOYMENT_END_DATE','LCA_CASE_EMPLOYER_NAME','LCA_CASE_EMPLOYER_ADDRESS','LCA_CASE_EMPLOYER_CITY','LCA_CASE_EMPLOYER_STATE','LCA_CASE_EMPLOYER_POSTAL_CODE','LCA_CASE_SOC_CODE','LCA_CASE_SOC_NAME','LCA_CASE_JOB_TITLE','LCA_CASE_WAGE_RATE_FROM','LCA_CASE_WAGE_RATE_TO','LCA_CASE_WAGE_RATE_UNIT','FULL_TIME_POS','TOTAL_WORKERS','LCA_CASE_WORKLOC1_CITY','LCA_CASE_WORKLOC1_STATE','PW_1','PW_UNIT_1','PW_SOURCE_1','OTHER_WAGE_SOURCE_1','YR_SOURCE_PUB_1','LCA_CASE_WORKLOC2_CITY','LCA_CASE_WORKLOC2_STATE','PW_2','PW_UNIT_2','PW_SOURCE_2','OTHER_WAGE_SOURCE_2','YR_SOURCE_PUB_2','LCA_CASE_NAICS_CODE'))
    # for row in reader:
    #     records.append(row)
    # for row in reader:
    #     print(row['STATUS'])
    # line_count = 0
    # for row in reader:
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')

# with open(dir + '/input/h1b_input.csv', encoding='utf-8') as csvfile:
#     status = collections.Counter()
#     occupation = collections.Counter()
#     state = collections.Counter()
    # try:
    # for row in csv.reader(csvfile, delimiter=';'):
    #     status[row[2]] += 1
    #     occupation[row[15]] += 1
    #     state[row[11]] += 1
    # # except IndexError:
    #     pass
