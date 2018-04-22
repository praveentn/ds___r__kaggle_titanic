# PROBLEM
# A stock market analyst wants to estimate the average return 
# on a certain stock. A random sample of 15 days yields an average 
# (annualized) return of Xbar=10.37% and a standard deviation of s=3.5%. 
# Assuming a normal population of returns, give a 95% confidence 
# interval for the average return on this stock.


# Sample Mean, xbar = 10.37
# Sample Standard Deviation, sam_std = 3.5
# Sample Size, n = 15

# We don't know the Mean (µ) & Standard Deviation (σ) of the Population 
# As the Sample Size (n) is 15 which is less than 30,
# we cannot use Normal Distribution

# Here, we can use t-distribution which is more robust
# Population Mean, µ = xbar +/- zt*(sam_std/√n)
# zt is the z-score for t-distribution
# zt = sp.t.ppf(confidence_interval, degrees_of_freedom)
# confidence_interval = 0.025 # for 95% 
# degrees of freedom = (n - 1) = 14

# CODE

import scipy.stats as sp
import math as m

n = 15
xbar = 10.37
sam_std = 3.5

pop_mean_mu1 = xbar + sp.t.ppf(0.025,df=n-1)*(sam_std/m.sqrt(n))

pop_mean_mu2 = xbar - sp.t.ppf(0.025,df=n-1)*(sam_std/m.sqrt(n))

# OUTPUT

# >>> mu1
# 8.431764604523753
  
# >>> mu2 
# 12.308235395476245

# ALTERNATE SOLUTION

sp.t.interval(alpha=0.95, df = n-1,loc=xbar, scale=sd/m.sqrt(n))

# >>> sp.t.interval(alpha=0.95, df = n-1,loc=xbar, scale=sam_std/m.sqrt(n))
# (8.431764604523753, 12.308235395476245)

# Conclusion: Average return of the stock will be between 8.4 and 12.3 
# with a confidence of 95%
