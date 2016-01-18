[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

###Python Code Chunks

**Exercise 5.1** In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters μ = 178 cm and σ = 7.7 cm for men, and μ = 163 cm and σ = 7.3 cm for women. In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

```python
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()
# (178.0, 7.7000000000000002)

dist.cdf(mu-sigma)
# 0.15865525393145741

low = dist.cdf(177.8)  
high = dist.cdf(185.4)
low, high, high-low
# (0.48963902786483265, 0.83173371081078573, 0.34209468294595308)
```


