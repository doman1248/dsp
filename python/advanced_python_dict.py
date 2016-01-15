########################################################################
## Q6 (Part III)
########################################################################
import pandas as pd
import re
import itertools

# define file path
fname = "/Users/dlee/ds/metis/prework/dsp/python/faculty.csv"

# read csv into data frame using pandas
df = pd.read_csv(fname)
# remove spaces in column names
df.rename(columns=lambda x: x.replace(" ", ""), inplace=True)

# transform title column
df['title'] = df['title'].apply(lambda x: re.sub(" of.*", "", x))
df['title'] = df['title'].apply(lambda x: re.sub(" is.*", "", x))

# add first and last name columns
df['firstname'] = df['name'].map(lambda x: x.split()[0])
df['lastname'] = df['name'].map(lambda x: x.split()[-1])
# drop name column
df = df.drop('name', 1)

# separate the columns that will define the values
df_values = df[['lastname','degree','title','email']]
df_values.head(n=3)
# create list elements in a list
list_values = []
for row in df_values.iterrows():
    index, data = row
    list_values.append(data.tolist())

# separate lastname column that will used to define the keys
df_keys = df[['lastname']]
list_keys = []
for index, row in df_keys.iterrows():
    list_keys.append(row['lastname'])

# convert to set and convert back to list
set_keys = set(list_keys)
list_keys = []
for item in set_keys:
    list_keys.append(item)

# create dictionary with only keys with values being empty list
dict_keys = {}
for item in list_keys:
    dict_keys[item] = []

# create dictionary based on list_values
cnt = 0
for item in list_values:
    key = list_values[cnt][0]
    if key in dict_keys.keys():
        dict_keys[key].append(item[1:])
    cnt = cnt + 1 


########################################################################
## Q7 (Part III)
########################################################################
from collections import OrderedDict

# create firstname and last name list
list_names = zip(df['firstname'], df['lastname'])

# re-use the list_values list created in Q6
df_values = df[['degree','title','email']]

list_values = []

for row in df_values.iterrows():
    index, data = row
    list_values.append(data.tolist())

# create dictionary by merging the two lists
dict_names = {}
cnt = 0 
for item in list_names:
    dict_names[item] = list_values[cnt]
    cnt = cnt + 1

# use OrderedDict to create ordered dictionary
OrderedDict(sorted(dict_names.items(), key=lambda key: key[0]))


########################################################################
## Q8 (Part III)
########################################################################

# sort by last name and print first 3 key and value pairs
OrderedDict(sorted(dict_names.items(), key=lambda key: key[0][1]))


















































