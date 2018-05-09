# PROBLEM

# Given the list of prices of houses in New York suburb (NY_house.csv).
# Come up with an interval estimate of prices with 95% confidence level.

# SOLUTION

# Since the number of samples, n = 1047,
# distribution of sample means is considered/assumed normal
# 

# CODE

import os
import math as m
import pandas as pd
import scipy.stats as st

data = pd.read_csv("NY_house.csv")

n = 1047

mean = data["Price"].mean()
# 163862.12511938874

std = data["Price"].std()
# 67651.55891678006

sigma = std / m.sqrt(n)
# 2090.761372647506


# st.norm.interval(confidence, loc=mean, scale=sigma)
st.norm.interval(0.95, loc=mean, scale=sigma)
(159764.3081287321, 167959.94211004538)

# CONCLUSION
# The price interval of the houses are between 159764 and 167959,
# with a confidence level of 95%
