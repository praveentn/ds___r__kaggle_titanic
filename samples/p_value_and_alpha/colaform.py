# PROBLEM

# An automatic bottling machine fills cola into 2 lt (2000 cm3) bottles. 
# A consumer advocate wants to test the null hypothesis that the average 
# amount filed by the machine into the bottle is at least 2,000 cm3. 
# A random sample of 40 bottles coming out of the machine was selected 
# and the exact content of the selected bottles are recorded. 
# The sample mean was 1,999.6 cm3. The population standard deviation is 
# known from the past experience to be 1.30 cm3. 
 
# 1. Test the null hypothesis at an alpha of 5%

# SOLUTION

# applying the Central Limit Theorem for the sample with size of 40,
# if sample size is adequate (n > 30) the distribution of sample means is normal

# VARIABLES
# Population Mean (µ), pop_mean_mu = ''
# Sample Mean, xbar = 1999.6
# Population Standard Deviation, σ = 1.30
# Sample size, n = 40

# FORMULA
# Sample Standard Deviation, sample_std = σ/√n

# CODE

import scipy.stats as st
import math as m

xbar = 1999.6
pop_std_sigma = 1.30
n = 40                # sample_size
x = 2000

sample_std = pop_std_sigma / m.sqrt(n)

# sample_std = 1.3/√40
# >>> sample_std
# 0.20554804791094466

# cdf - cumulative density function
# gives the probability that the variate has a value less than or equal to the given value.

# p_value = sp.norm.cdf(1999.6, loc=2000, scale=1.30/m.sqrt(40))
# Had a doubt on this part; whether loc equals to x or xbar in the function
# p_value = sp.norm(loc = xbar, scale=1.30/m.sqrt(40)).cdf(2000)
# >>> p_value
# 0.9741736525121241  # wrong!!!

# Here we're finding the probability of getting a sample mean of 1999.6
# in a normally distributed population, with mean of 2000 and pop std of 1.3
# p_value = sp.norm(loc = 2000, scale=1.30/m.sqrt(40)).cdf(1999.6)
# So, the normal distribution has a mean of 'x' and 'scale' as shown below.
# And we need to calculated the 'cdf' of 'xbar' in this case
# The location (loc) keyword specifies the mean.
# The scale (scale) keyword specifies the standard deviation.
# scipy.stats.norm(loc=mean, scale=standard deviation)

p_value = sp.norm(loc = x, scale=1.30/m.sqrt(40)).cdf(xbar)

# OUTPUT

# >>> p_value
# 0.025826347487875892

# CONCLUSION

# P-value is 0.0258 (2.58%) which is less than the significance level (α = 5%)
# Hence we can reject the Null Hypothesis

# SIGNIFICANCE
# Company is not filling upto 2lts in its bottles
