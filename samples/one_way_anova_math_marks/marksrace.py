# PROBLEM

# Given the file "Student_marks.csv", formulate and test 
# the hypothesis defining the relation between Math1 marks and Race.

# Math1 and Race are columns in the input file.

# SOLUTION

# There are four different values for the field 'Race'.
# We cannot use t-test for more than 2 samples

# Null Hypothesis (ho)
# There's no significant difference between the marks of different races

# Alternate Hypothesis (ha)
# There's significant difference between the marks of different races

# CODE

import os
import scipy.stats as st
import pandas as pd

# reading the csv into the variable 'hyp'
hyp = pd.read_csv("Student_marks.csv")

# obtain the unique values for 'Race'
races = pd.unique(hyp['Race'])

# output: array([4, 3, 1, 2], dtype=int64)

# Grouping the marks for Math1 based on the value of race in races 
d_data = { grp:hyp['Math1'][hyp['Race'] == race] for race in races }

# To view the value of Math1 marks for the race 1 or race 4 - 
# d_data[1]
# d_data[4]

# Applying f-test - one way anova
st.f_oneway(d_data[1],d_data[2],d_data[3],d_data[4])

# output: F_onewayResult(statistic=7.703265387359707, pvalue=6.840198626500769e-05)

# p-value is less than alpha; reject null hypothesis
# Math marks are significantly different between races
