# PROBLEM

# In "Student_marks.csv" there're columns for Gender and Race.
# We've gender and race with the following values. 
# Gender - [0,1] Race - [1,2,3,4]
# Conduct suitable test to determine the relation between Gender and Race.


# SOLUTION

# Since these are categorical variables, we can use Chi squared test

# HYPOTHESIS

# ho: The data are consistent with a specified distribution.
# ha: The data are not consistent with a specified distribution.

# We mean the distribution of gender [0,1] across different races [1,2,3,4]

# CODE

import pandas as pd
import scipy.stats as st

hyp = pd.read_csv('Student_marks.csv', index_col=0)

# contingency table
cont_table = pd.crosstab(hyp['Gender'], hyp['Race'])

# output
# >>> cont_table
# Race |     1   2   3   4
# --------------------------
# Gender  
# --------------------------
# 0    |    13   3   7  68
# 1    |    11   8  13  77

chisq, pvalue, df, ex = st.chi2_contingency(cont_table)

# pvalue = 0.36123387290989273


# CONCLUSION

# P-value is larger than significance level (0.05 or 5%)
# Hence we cannot reject the null hypothesis (ho)
