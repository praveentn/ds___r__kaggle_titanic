# pre-requisites
import numpy.stats

# create a normally distributed sample of size = 5000
# with mean = 777 and standard deviation = 100
# random sample rounded to two decimals
sample = np.round(np.random.normal(777,100,5000),2)

# output: array([876.5 , 821.85, 853.16, ..., 794.08, 540.23, 858.  ])

# we can find the probability of the mean (777) using the cdf()
# theoretically, probability of the mean is 0.5
scipy.stats.norm(777, 100).cdf(777)

# output: 0.5

# to calculate the probability of getting a value > 1000
# first, we've to find the probability of getting the value = 1000
# which is equal to the area under the normal distribution curve
# then deduct that from the total area (which is 1)
scipy.stats.norm(777, 100).cdf(1000)

# output: 0.987126278561398

# probability of getting a value greater than 1000
1 - scipy.stats.norm(777, 100).cdf(1000)

# output: 0.012873721438601993

# note 1- floating point precision will vary between systems

# note 2- cdf is a function whose value is the probability that 
# a corresponding continuous random variable has a value less than 
# or equal to the argument of the function
