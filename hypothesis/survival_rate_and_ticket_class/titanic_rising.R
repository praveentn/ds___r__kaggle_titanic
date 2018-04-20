################################################################

# Author: Praveen T N
# Date: 20-04-2018
# Version: 1.0
# 

# Hypothesis - First class ticket holders had a survival rate 
# higher than that of second and third class

################################################################

#set working directory 

setwd("<path_to_code_and_files>") 

#eg. setwd("/home/vanpeer/ds___r__kaggle_titanic/") 

#load raw data from the inputs train.csv and test.csv 

train <- read.csv("train.csv", header = TRUE) 
test <- read.csv("test.csv", header = TRUE)

#output: train and test objects with data loaded from the corresponding csv files

#train.csv has the column Survived. 
#we're adding this column with the same name to test.csv as shown below. 

test.Survived <- data.frame(Survived = rep("None", nrow(test)), test[,])

#output: adds a new column by the name Survived to test

#combine data sets 

data.combined <- rbind(train, test.Survived)

#output: data.combined object with combination of test and train data

#to compactly display the structure of an arbitrary R object 

str(data.combined)

#output: displays the structure of the object 

# 'data.frame':	1309 obs. of 12 variables: 
# $ PassengerId: int 1 2 3 4 5 6 7 8 9 10 ... 
# $ Survived : chr "0" "1" "1" "1" ... 
# $ Pclass : int 3 1 3 1 3 3 1 3 3 2 ... 

#turns the variables Pclass and Survived into type factors 

data.combined$Survived <- as.factor(data.combined$Survived) 
data.combined$Pclass <- as.factor(data.combined$Pclass)

#output 

# $ Survived : Factor w/ 3 levels "0","1","None": 1 2 2 2 1 1 1 1 2 2 ... 
# $ Pclass : Factor w/ 3 levels "1","2","3": 3 1 3 1 3 3 1 3 3 2 ... 

#table uses the cross-classifying factors to build a contingency table of the counts at each combination of factor levels 

table(data.combined$Survived)

# output 

#    0   1 None 
#  549 342 418 

# load ggplot2 library for visualizations
library(ggplot2)

# plotting ticket class and survival data

train$Pclass <- as.factor(train$Pclass)
ggplot(train, aes(x = Pclass, fill = factor(Survived))) + 
  stat_count(width = 0.5) + 
  xlab("Pclass") + 
  ylab("Total Count") + 
  labs(fill = "Survived")

# refer image for the output
