[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 2.4 Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. 
Compute Cohen’s d to quantify the difference between the groups. 
How does it compare to the difference in pregnancy length?

```python
## data file in '2002FemPreg.dat.gz'
## format of file is documented in 2002FemPreg.dct (Stata dictionary file)

import nsfg
import thinkstats2
import thinkplot
import math

# prepare main dataframe
preg = nsfg.ReadFemPreg()

# transformation - data cleaning
nsfg.CleanFemPreg(preg)

# validation
preg.outcome.value_counts().sort_index() # preg outcome data
preg.birthwgt_lb.value_counts().sort_index() # birthwgt_lb data

# create dataframes for analysis
live = preg[preg.outcome == 1] # live births only
firsts = live[live.birthord == 1] # first borns
others = live[live.birthord != 1] # non-first borns

# compute Cohen's d using variable totalwgt_lb - comparing means of firsts vs others
mean_firsts = firsts['totalwgt_lb'].mean()
mean_others = others['totalwgt_lb'].mean()
diff = mean_firsts - mean_others 
var_firsts = firsts['totalwgt_lb'].var()
var_others = others['totalwgt_lb'].var()
n_firsts, n_others = len(firsts['totalwgt_lb']), len(others['totalwgt_lb'])
pooled_var = (n_firsts * var_firsts + n_others * var_others) / (n_firsts + n_others)
d = diff / math.sqrt(pooled_var)

# outputting results
def results():
    print('mean of firsts: ' + str(mean_firsts))
    print('mean of others: ' + str(mean_others))
    print('variance of firsts: ' + str(var_firsts))
    print('variance of others: ' + str(var_others))
    print("Cohen's d: " + str(d))

# results
results()

```

Results:

| Metrics         |       Values |
------------------|---------------
| mean of firsts: | 7.20109443044 |
| mean of others: | 7.32585561497 |
| variance of firsts:| 2.01802730092 |
| variance of others:| 1.9437810259 |
| Cohen's d:| -0.0886729270726 |


