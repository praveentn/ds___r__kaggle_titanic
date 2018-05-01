# Hypothesis Testing

# We've an input file (Student_marks.csv) with the marks of students for Maths. 
# Formulate a hypothesis and test it to see if there's significant difference 
# between the marks before and after training.

# Null Hypothesis (µo)
# µbefore = µafter
# i.e. there's no significant difference between the marks before and after training.

# Alternate Hypothesis (µa)
# µbefore != µafter
# i.e. there's significant difference between the marks before and after training.

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

# scipy.stats.ttest_rel(a, b, axis=0)
# Calculates the T-test on TWO RELATED samples of scores, a and b.

# This is a two-sided test for the null hypothesis that 2 related 
# or repeated samples have identical average (expected) values.

st.ttest_rel(hyp.Math1, hyp.Math2)

# output: Ttest_relResult(statistic=1.3555927189268235, pvalue=0.17676525605507354)

# Alternately, you can do the following as well
stat, pvalue = st.ttest_rel(hyp.Math1, hyp.Math2)

# >>> stat
# 1.3555927189268235

# >>> pvalue
# 0.17676525605507354

# Examples for the use are scores of the same set of student in different exams, 
# or repeated sampling from the same units. The test measures whether the average 
# score differs significantly across samples (e.g. exams). If we observe a large 
# p-value, for eg. greater than 0.5 or 0.1 then we can't reject the null hypothesis 
# of identical average scores. If the p-value is smaller than the threshold, 
# e.g. 1%, 5% or 10%, then we reject the null hypothesis of equal averages. 
# Small p-values are associated with large t-statistics.

# Here, we have p-value of 17%. We cannot reject the null hypothesis.

# CONCLUSION

# There's no significant difference between the marks before and after training.
