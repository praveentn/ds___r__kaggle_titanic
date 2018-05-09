# Hypothesis Testing

# We've an input file (Student_marks.csv) with the marks of students for Maths. 
# Formulate a hypothesis and test it to see if there's significant difference 
# between the marks of boys and girls.

# Null Hypothesis (µo)
# µboys = µgirls
# i.e. there's no significant difference between the marks of boys and girls

# Alternate Hypothesis (µa)
# µboys != µgirls
# i.e. there's significant difference between the marks of boys and girls

# CODE

import os
import pandas as pd
import scipy.stats as st

# Check the current working directory and set it appropriately.
# cwd should point to the location where the input csv file resides.
# os.getcwd()
# os.chdir("<specify_required_path>")

# Alternately you can specify the full path to the file.
# Here, I'm giving only the filename.
hyp = pd.read_csv("Student_marks.csv")

# Using the pandas groupby() for grouping the data by gender
grouped = hyp.groupby('Gender')

# output: <pandas.core.groupby.DataFrameGroupBy object at 0x0000024667D87CF8>

# Segregating boys and girls based on Gender
# Value of Gender is 1 for girls and 0 for boys

Girls = grouped.get_group(1)
# 109 rows × 11 columns

Boys = grouped.get_group(0)
# 91 rows × 11 columns

# Here, we've two independent samples
# Two Sample Independent T-Test
# Note: we don't go for T-test for more than two samples

st.ttest_ind(Girls.Math1, Boys.Math1)

# output: Ttest_indResult(statistic=-0.41299864929688507, pvalue=0.6800544974232143)

# P-value gives an idea about the risk associated with the decision 
# of going with null hypothesis
# i.e. if p-value is less than alpha (5%) then we reject the null hypothesis

# Here, we have p-value of 68%. We can reject the alternate hypothesis.

# CONCLUSION

# There's no significant difference between the marks of boys and girls.
