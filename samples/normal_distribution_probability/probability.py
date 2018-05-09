# (I) For a given Mean 494 and standard deviation = 100

import scipy.stats as sp

# 1. What is the probability that a randomly selected score is between 600 and its mean.

# x1 is the probability of getting a score equal to mean; 0.5 (by default)
x1 = sp.norm(494, 100).cdf(494)

# x2 is the probability of getting a score equal to 600
x2 = sp.norm(494, 100).cdf(600)

# x2 = 0.8554277003360904

# To find the probability of a score between the two values - mean and 600, 
# we need to get the individual values and calculate the difference

required_probability = x2 - x1
# >>> x2 - x1
# 0.3554277003360904


# 2. What is the probability of obtaining a score more than 700.

# x is the probability of getting a value equal to 700
x = sp.norm(494, 100).cdf(700)

# Probability of a score greater than 700 will be the difference between 
# total area and the probability of getting a value equal to 700
# >>> x
# 0.9803007295906231

required_probability = 1 - x
# >>> 1-x
# 0.019699270409376912


3. Score that is less than 550.

x = sp.norm(494, 100).cdf(550)

required_probability = x
# >>> x
# 0.712260281150973


4. Score between 300 and 600.

x1 = sp.norm(494, 100).cdf(300)
x2 = sp.norm(494, 100).cdf(600)

# >>> x2
# 0.8554277003360904

#>>> x1
# 0.026189844940452685

# To find the probability of a score between the two values - 300 and 600, 
# we need to get the individual values and calculate the difference

required_probability = x2 - x1
# >>> x2 - x1
# 0.8292378553956377


# (II) Suppose during any hour in a store, the average number of shoppers is 448,
# with the standard deviation of 21 shoppers. What is the probability that 
# a random sample of 49 different shopping hours will yield a sample mean between 
# 441 and 446 shoppers.

# Solution

# We know the Mean (µ) & Standard Deviation (σ) of the Population, 448 and 21
# Sample size, n = 49 which is greater than 30
# find probability of sample mean between 441 and 446

# CODE

pop_mean_mu = 448
pop_std_sigma = 21

x1 = sp.norm(448, 21).cdf(441)
x2 = sp.norm(448, 21).cdf(446)

# >>> x1 = sp.norm(448, 21).cdf(441)
# >>> x2 = sp.norm(448, 21).cdf(446)
# >>> x2
# 0.46206285593374585
# >>> x1
# 0.36944134018176367

required_probability = x2 - x1

# >>> x2 - x1
# 0.09262151575198219
