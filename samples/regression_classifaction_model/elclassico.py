# PROBLEM

# Given 'Classification.csv', build a suitable model to predict loan defaults.

# SOLUTION

# split data [train:test::70:30]
# build model
# find out accuracy

# CODE

import os
import pandas as pd

os.chdir(<required_directory>)

gc = pd.read_csv('Classification.csv')

# Logistic Regression

from sklearn.model_selection import train_test_split
import statsmodels.formula.api as sm

# random_state=123 - acts a seed for multiple iterations
# to have same data for train and test
train, test = train_test_split(gc, test_size=0.30, random_state=123)

model_log = sm.glm(formula='Default~duration', data=train)
model_fit_log = model_log.fit()

model_fit_log.summary()

# output: classification_model_summary.png
# Generalized Linear Model Regression Results


# Prediction

def_pred = model_fit_log.predict(test["duration"])

# >>> def_pred
# 131    0.426019
# 203    0.211364
# 50     0.318692
# Length: 300, dtype: float64

# function to segregate probabilities 

def isPro(i):
    # 0.5 depends on requirement
    if (i>=0.5):
        return 1
    else:
        return 0
        
test["def_pred_class"] = def_pred.apply(isPro)

# >>> test["def_pred_class"]
# 709    0
# 294    1
# 995    0
# Name: def_pred_class, Length: 300, dtype: int64

pd.crosstab(test["def_pred_class"],test["Default"])

Default	        0   1
def_pred_class		
            0  187  85
            1   13  15

# Accuracy = correct predictions/total
# diagonal elements are accurate predictions
# correct predictions = 187+15 = 202
# total = 187+85+13+15 = 300

# CONCLUSION

# Model has an accuracy of 73% to predict loan defaulters.
