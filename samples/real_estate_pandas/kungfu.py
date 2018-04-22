# basic statistical operations using python
# and built-in functions in pandas

import pandas as pd
import os

# Ensure that 'RealEstate.csv' is in the same directory as 
# the current working directory (cwd)
os.getcwd()
# 'E:\\Python'

# set cwd to the required directory by running
# os.chdir('E:\\RequiredDirectory') 

# load 'RealEstate.csv' to 'data'
data = pd.read_csv('RealEstate.csv')

# describe() the count, mean, std, min, 25/50/75 %iles, max
data.describe()

# calculates the mean of all columns
data.mean()

# >>> data.mean()
# Price         163862.125119
# LivingArea      1807.302770
# Bathrooms          1.918338
# Bedrooms           3.183381
# LotSize            0.569580
# Age               28.061127
# Fireplace          0.593123
# dtype: float64

# finding the mean of individual columns
data.Price.mean()

# using axis
data.mean(axis=1)

# skipping values
data.mean(axis=0, skipna=True)

# >>> data.Price.mean()
# 163862.12511938874

# find standard deviation of 'Age'
data.Age.std()

# >>> data.Age.std()
# 34.900898867359025

# find skew of LotSize
data.LotSize.skew()

# >>> data.LotSize.skew()
# 5.2023913507949375

# First Quartile or 25th percentile
data.Bedrooms.quantile(0.25)

# >>> data.Bedrooms.quantile(0.25)
# 3.0
