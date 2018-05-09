################################################################

# Author: Praveen T N
# Date: 26-04-2018
# Version: 1.0
# 

# Hypothesis - Women with their families in Titanic have higher 
# survival than men
# Find the titles from the names of passengers
# Create a new field "Family" based on siblings & parents/children

################################################################

# R version 3.4.4 (2018-03-15) -- "Someone to Lean On"
# Copyright (C) 2018 The R Foundation for Statistical Computing
# Platform: x86_64-w64-mingw32/x64 (64-bit)
# 
# R is free software and comes with ABSOLUTELY NO WARRANTY.
# You are welcome to redistribute it under certain conditions.
# Type 'license()' or 'licence()' for distribution details.
# 
# R is a collaborative project with many contributors.
# Type 'contributors()' for more information and
# 'citation()' on how to cite R or R packages in publications.
# 
# Type 'demo()' for some demos, 'help()' for on-line help, or
# 'help.start()' for an HTML browser interface to help.
# Type 'q()' to quit R.
# 
# [Workspace loaded from ~/.RData]

# set working directory 
setwd("<path_to_code_and_files>") 

# eg. setwd("/home/vanpeer/ds___r__kaggle_titanic/") 

# load raw data from the inputs train.csv and test.csv 
train <- read.csv("train.csv", header = TRUE) 
test <- read.csv("test.csv", header = TRUE)

# output: train and test objects with data loaded from the corresponding csv files

# train.csv has the column Survived. 
# we're adding this column with the same name to test.csv as shown below. 

test.Survived <- data.frame(Survived = rep("None", nrow(test)), test[,])

# output: adds a new column by the name Survived to test

# combine data sets 
data.combined <- rbind(train, test.Survived)

# output: data.combined object with combination of test and train data

# turns the variables Pclass and Survived into type factors 
data.combined$Survived <- as.factor(data.combined$Survived) 
data.combined$Pclass <- as.factor(data.combined$Pclass)

# output 

# $ Survived : Factor w/ 3 levels "0","1","None": 1 2 2 2 1 1 1 1 2 2 ... 
# $ Pclass : Factor w/ 3 levels "1","2","3": 3 1 3 1 3 3 1 3 3 2 ... 

# load ggplot2 library for visualizations
library(ggplot2)

# load stringr - deals with "NA"'s and zero length vectors
library(stringr)

# turns the variables Pclass into type factors 
train$Pclass <- as.factor(train$Pclass)

# Expand upon the realtionship between `Survived` and `Pclass` 
# by adding the new `Title` variable to the
# data set and then explore a potential 3D relationship.

# Create a utility function to help with title extraction
# Using grep function here but could've used the str_detect function as well.

extractTitle <- function(Name) {
  name <- as.character(Name)
  if (length(grep("Miss.", Name)) > 0) {
    return ("Miss.")
  } else if (length(grep("Master.", Name)) > 0) {
    return ("Master.")
  } else if (length(grep("Mrs.", Name)) > 0) {
    return ("Mrs.")
  } else if (length(grep("Mr.", Name)) > 0) {
    return ("Mr.")
  } else {
    return ("Other")
  }
}

# output: a function is created

# NOTE - The code below uses a for loop which is not a very R way of
#        doing things
titles <- NULL
for (i in 1:nrow(data.combined)) {
  titles <- c(titles, extractTitle(data.combined[i,"Name"]))
}

# output: titles 
# View(unique(titles)) Mr., Mrs., Miss., Master., Other

# adds titles to data.combined 
# no. of variables gets added by 1 to 13
data.combined$Title <- as.factor(titles)

# output: A new column titled "Title" added to data.combined
# use View(data.combined) to verify the data

summary(data.combined$Age)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
#   0.17   21.00   28.00   29.88   39.00   80.00     263 

summary(data.combined[1:891, "Age"])
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
#   0.42   20.12   28.00   29.70   38.00   80.00     177 

# Creating a family size feature
temp.SibSp <- c(train$SibSp, test$SibSp)
temp.Parch <- c(train$Parch, test$Parch)

data.combined$FamilySize <- as.factor(temp.SibSp + temp.Parch + 1)

# Visualize to see if it is predictive
ggplot(data.combined[1:891,], aes(x = FamilySize, fill = Survived)) +
  stat_count(width = 0.5) + 
  facet_wrap(~Pclass + Title) + 
  ggtitle("Pclass, Title") +
  xlab("FamilySize") +
  ylab("Total Count") +
  ylim(0,300) +
  labs(fill = "Survived")

# output: refer image

# Even though there's value for "Other" in 3rd Class,
# the plot for it is missing in the output

temp.3Other <- table(data.combined$Title, data.combined$Pclass)
temp.3Other
# Number of persons by Title in each Class 
#            1   2   3
#  Master.   5  11  45
#  Miss.    60  50 150
#  Mr.     160 150 448
#  Mrs.     79  55  65
#  Other    19  11   1
# 
