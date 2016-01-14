########################################################################
## Q5 (Part II)
########################################################################
import pandas as pd
import itertools

# define file path
fname = "/Users/dlee/ds/metis/prework/dsp/python/faculty.csv"

# read csv into data frame using pandas
df = pd.read_csv(fname)
# remove spaces in column names
df.rename(columns=lambda x: x.replace(" ", ""), inplace=True)

# approach 1: write emails to emails.csv file
# put emails into a list
email_list = []
email_list.append(df['email'])
email_list = list(itertools.chain(*email_list))

email_fname = "/Users/dlee/ds/metis/prework/dsp/python/emails.csv"
email_output = open(email_fname, 'w') # open file to write
email_output.writelines(["%s\n" % item for item in email_list]) # list comprehension
email_output.close()

# approach 2
df['email'].to_csv(email_fname, index=False)














