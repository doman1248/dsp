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
df_values =df[['lastname','degree','title','email']]
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




testdict = df.set_index('firstname').T.to_dict('list')

{'Putt': [' PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu'], 
'Feng': [' Ph.D', 'Assistant Professor', 'ruifeng@upenn.edu'], `
'Bilker': ['Ph.D.', 'Professor', 'warren@upenn.edu'], 
'Shaw': [' PhD', 'Assistant Professor', 'shawp@upenn.edu'], 
'Landis': [' B.S.Ed. M.S. Ph.D.', 'Professor', 'jrlandis@mail.med.upenn.edu'], 
'Propert': [' Sc.D.', 'Professor', 'propert@mail.med.upenn.edu'], 
'Gimotty': [' Ph.D', 'Professor', 'pgimotty@upenn.edu'], 
'Joffe': [' MD MPH Ph.D', 'Professor', 'mjoffe@mail.med.upenn.edu'], 
'Ellenberg': [' Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], 
'Hubbard': [' PhD', 'Associate Professor', 'rhubb@mail.med.upenn.edu'], 
'Morales': [' Sc.D.', 'Associate Professor', 'knashawn@mail.med.upenn.edu'], 
'Mitra': [' Ph.D.', 'Associate Professor', 'nanditam@mail.med.upenn.edu'], 
'Ross': [' PhD', 'Assistant Professor', 'michross@upenn.edu'], 
'Troxel': [' ScD', 'Professor', 'atroxel@mail.med.upenn.edu'], 
'French': [' PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu'], 
'Ratcliffe': [' Ph.D.', 'Associate Professor', 'sratclif@upenn.edu'], 
'Hsu': [' Ph.D.', 'Assistant Professor', 'hsu9@mail.med.upenn.edu'], 
'Shults': [' Ph.D.', 'Professor', 'jshults@mail.med.upenn.edu'], 
'Xie': [' PhD', 'Assistant Professor', 'dxie@upenn.edu'], 
'Shinohara': ['0', 'Assistant Professor', 'rshi@mail.med.upenn.edu'], 
'Bryan': [' PhD', 'Assistant Professor', 'bryanma@upenn.edu'], 
'Guo': [' Ph.D', 'Professor', 'wguo@mail.med.upenn.edu'], 
'Localio': [' JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu'], 
'Yang': [' Ph.D.', 'Assistant Professor', 'weiyang@mail.med.upenn.edu'], 
'Sammel': [' Sc.D.', 'Professor', 'msammel@cceb.med.upenn.edu'], 
'Li': [' Ph.D', 'Professor', 'hongzhe@upenn.edu'], 
'Hwang': [' Ph.D.', 'Associate Professor', 'whwang@mail.med.upenn.edu'], 
'Bellamy': [' Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu'], 
'Shou': [' Ph.D.', 'Assistant Professor', 'hshou@mail.med.upenn.edu'], 
'Stephens': [' Ph.D.', 'Assistant Professor', 'alisaste@mail.med.upenn.edu'], 
'Xiao': [' PhD', 'Assistant Professor', 'rxiao@mail.med.upenn.edu'], 
'Roy': [' Ph.D.', 'Associate Professor', 'jaroy@mail.med.upenn.edu'], 
'Chen': [' Ph.D.', 'Associate Professor', 'jinboche@upenn.edu']}




