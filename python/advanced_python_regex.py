########################################################################
## Q1 (Part I)
########################################################################
import pandas as pd
import itertools
import collections from Counter

# define file path
fname = "/Users/dlee/ds/metis/prework/dsp/python/faculty.csv"

# read csv into data frame using pandas
df = pd.read_csv(fname)
df.head(n=5)
df['name'].count()
list(df)
df.columns

# remove spaces in column names
df.rename(columns=lambda x: x.replace(" ", ""), inplace=True)

# remove periods (.) degree column
df['degree'] = df['degree'].apply(lambda x: x.replace('.',''))

# frequency of unique rows 
df['degree'].value_counts()

# take degree column and convert to list 
degree_list = []
degree_list.append(df['degree'])
merged = list(itertools.chain(*degree_list))

# split each element by space, which creates lists within the list
count = 0
for i in merged:
    new_merged.append(merged[count].split())
    count = count + 1

# unlist the list elements within the list
new_merged = list(itertools.chain.from_iterable(new_merged))

# remove element where len is less than 2, which are not degrees
for item in new_merged:
    if len(item) < 2:
        new_merged.remove(item)

# use the Counter package to count fequency of each degree
counts = Counter(new_merged)

# fequencies: Counter({'PhD': 32, 'ScD': 6, 'MPH': 2, 'MS': 2, 'MD': 1, 'MA': 1, 'BSEd': 1, '0': 1, 'JD': 1})
print(counts)

# count of unique degrees = 8
len(counts)


########################################################################
## Q2 (Part I)
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
# fequency by different titles
df['title'].value_counts()

# Professor of Biostatistics              13
# Associate Professor of Biostatistics    12
# Assistant Professor of Biostatistics    11
# Assistant Professor is Biostatistics     1

# transform title column
df['title'] = df['title'].apply(lambda x: re.sub(" of.*", "", x))
df['title'] = df['title'].apply(lambda x: re.sub(" is.*", "", x))

# re-run fequency script
df['title'].value_counts()

# Professor              13
# Associate Professor    12
# Assistant Professor    12

# number of unique titles
title_list = []
title_list.append(df['title'])
title_list = list(itertools.chain(*title_list))
print(len(set(title_list)))


########################################################################
## Q3 (Part I)
########################################################################
import pandas as pd
import itertools

# define file path
fname = "/Users/dlee/ds/metis/prework/dsp/python/faculty.csv"

# read csv into data frame using pandas
df = pd.read_csv(fname)
# remove spaces in column names
df.rename(columns=lambda x: x.replace(" ", ""), inplace=True)

# put emails into a list
email_list = []
email_list.append(df['email'])
email_list = list(itertools.chain(*email_list))

# print all emails
for item in email_list:
    print(item)


########################################################################
## Q4 (Part I)
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

# create list of email domains
# set(['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu'])
email_domains = []
email_domains.append(df['email'].apply(lambda x: re.sub("^.*@", "", x)))
email_domains = set(list(itertools.chain(*email_domains)))

# results
print(email_domains)
print(len(email_domains))
