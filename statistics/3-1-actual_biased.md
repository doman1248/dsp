[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

###Analysis - Python Code Chunks

Exercise 3.1 Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribu- tion for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the chil- dren and asked them how many children under 18 (including themselves) are in their household.
Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

####Prepare the dataframe

```python
import thinkstats2
dct_file='2002FemResp.dct'
dat_file='2002FemResp.dat.gz'
dct = thinkstats2.ReadStataDct(dct_file)
resp = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=None)
```

####Create actual PMF data
```python
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual')
```

####Create biased PMF data
```python
# biased_pmf - raw calculation
biased_pmf = pmf.Copy(label = 'biased')

for x, p in pmf.Items():
  biased_pmf.Mult(x, x)

biased_pmf.Normalize()
```

####Plot both actual and biased pmf's
```python
# plot actual vs observed (biased)
import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='Number of Children', ylabel='PMF')
```

![image](../img/3-1-actual_biased.png?raw=true)

####Calculate actual and biased means
```python
# actual mean
pmf.Mean()

# biased mean
biased_pmf.Mean()
```

###Results
| PMF    |  Mean  |
|--------|--------|
| Actual | 1.0242051550438309 |
| Biased | 2.4036791006642821 |

