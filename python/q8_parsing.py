# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an 
# approach of your choice.

file = "/Users/dlee/ds/metis/prework/dsp/python/football.csv"

def get_team(file):
  import csv
  data = csv.reader(open(file,"rb"))
  header = next(data)
  dict = {}
  for item in data:
    dict[abs(int(item[5]) - int(item[6]))] = item[0]
  return dict[min(dict)]

## Name of team with the smallest difference 'Aston_Villa'
