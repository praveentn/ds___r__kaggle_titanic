# PROBLEM
Comcast, the computer services company, is planning to invest heavily in 
online television services. As part of the decision, the company wants to 
estimate the average number of online shows a family of four would watch 
per day. A random sample of n=100 families is obtained, and in this sample 
the average no of shows viewed per day is 6.5 and the population standard 
deviation is known to be 3.2. Construct a 95% confidence interval for the 
average number of online television shows watched by the entire population 
of families of four. 

# SOLUTION

# Population Standard Deviation, σ = 3.2
# Sample Mean, xbar = 6.5
# Sample Size, n = 100
# Confidence Interval is 95%
# z is 2.5% on either side of the normal distribution curve
# i.e. z = scipy.stats.norm.ppf(0.025)
# ppf is the inverse of the cdf. i.e, ppf gives the value of the variate
# for which the cumulative probability has the given value.

# Since sample size is adequate (n > 30)
# applying Central Limit Theorem
# mean of the distribution of sample means = population mean (µ)

# µ = xbar +/– z(σ /√n)
# we'll get two values for population mean (pop_mean_mu1, pop_mean_mu2)

# CODE

import scipy.stats as sp
import math as m

xbar = 6.5
pop_std_sigma = 3.2
n = 100                           # sample_size
z = sp.norm.ppf(0.025)   # z-score 

pop_mean_mu1 = xbar + z*(pop_std_sigma / m.sqrt(n))

pop_mean_mu2 = xbar - z*(pop_std_sigma / m.sqrt(n))


# OUTPUT

# >>> pop_mean_mu1
# 5.872811524947182

# >>> pop_mean_mu2
# 7.127188475052818

# Conclusion: Number of online television shows watched by the entire population
# of families of four is between 6 and 7 with 95% confidence


# ALTERNATE SOLUTION

# >>> sp.norm.interval(alpha=0.95, loc=xbar, scale=pop_std_sigma/m.sqrt(n))
# (5.872811524947183, 7.127188475052817)


