# PROBLEM
# Mercury makes a 2.4 lt V-6 engine, The Laser XRi, used in speedboats. 
# The company's engineer believe that the engine delivers an average power of 220 horsepower
# and that the standard deviation of power delivered is 15 horsepower. 
# A potential buyer intends to sample 100 engines(each engine to be run a single time). 
# What is the probability that the sample mean will be less than 217 horsepower?

# SOLUTION

# applying the Central Limit Theorem for the sample with size of 100,
# if sample size is adequate (n > 30) the distribution of sample means is normal

# VARIABLES
# Population Mean, µ = 220
# Population Standard Deviation, σ = 15
# Sample size, n = 100

# FORMULA
# Sample Standard Deviation, sample_std = σ/√n

# CODE

import scipy.stats as sp
import math as m

pop_mean_mu = 220
pop_std_sigma = 15
n = 100              # sample_size
x = 217              # sample_mean_whose_probability_to_be_found

sample_std = pop_std_sigma / m.sqrt(n)

# sample_std = 15/√100 = 1.5

# cdf - cumulative density function
# gives the probability that the variate has a value less than or equal to the given value.
# prob_sample_std = sp.norm(loc=x-bar, scale=sample_std).cdf(x)
# prob_sample_std = sp.norm(220, 1.5).cdf(217)

prob_sample_std = sp.norm(pop_mean_mu, sample_std).cdf(x)

# OUTPUT
# 0.022750131948179195
