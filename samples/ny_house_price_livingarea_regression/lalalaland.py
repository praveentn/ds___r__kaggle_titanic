# PROBLEM

# Find the relation between Price and Living Area.
# Analyze the feasibility of the regression model.

# SOLUTION
# Establish a relationship between Price and LivingArea

# Null Hypothesis: there's no relation
# ho: bo = b1 = b2 ... = 0

# Alternate Hypothesis: there's relation
# ha: not all beta(o,1,2...) = 0

# We require beta-zero (bo) and b1

# Price = bo + b1*LivingArea

# CODE

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas.plotting as plt2

os.getcwd()
os.chdir('<required_directory>')

# load the data into 'hp' using pandas
hp = pd.read_csv('NY_house.csv')

# correlation between Price and Living Area
hp.Price.corr(hp.LivingArea)

# plot between Price and Living Area
hp.plot(kind="scatter", 
x="LivingArea", 
y="Price", 
figsize = (4,4), 
color = "green")

# output: ny_house_price_livingarea.png
# there's strong correlation between Price and Living Area
# analyze the model

import statsmodels.formula.api as sm

# ordinary least squares function
# method for estimating the unknown parameters in a linear regression model
model = sm.ols(formula='Price~LivingArea', data=hp)

model_fit = model.fit()

model_fit.summary()

# output: ny_house_regression_model.png

# bo = 1.588e+04
# b1 = 81.8825

# P>|t| = ~0.000
# R-squared = 60%
# F-statistic = 1586
# Prob(F-statistic) = 9.75e-212

# Why t test in regression?
# to check individual relation between variables

# why f-stats in regression?
# to check the overall feasibility of the regression model
# prob (f-statistic)


# CONCLUSION 

# 1. Prob(F-statistic) = 9.75e-212
# P-value is significant ( less than 0.05)
# convincingly reject null hypothesis, ho

# 2. Prob(t test) = 0.000
# Reject null hypothesis, ho; b1 != 0
# relation exists!




