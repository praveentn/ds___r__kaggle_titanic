################################################################

# Author: Praveen T N
# Date: 20-04-2018
# Version: 1.0
# 

# Hypothesis - Men in 3rd class have the least survival rate

################################################################

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

# to compactly display the structure of an arbitrary R object 

str(data.combined)

# output: displays the structure of the object 

# 'data.frame':	1309 obs. of 12 variables: 
# $ PassengerId: int 1 2 3 4 5 6 7 8 9 10 ... 
# $ Survived : chr "0" "1" "1" "1" ... 
# $ Pclass : int 3 1 3 1 3 3 1 3 3 2 ... 

#turns the variables Pclass and Survived into type factors 

data.combined$Survived <- as.factor(data.combined$Survived) 
data.combined$Pclass <- as.factor(data.combined$Pclass)

# output 

# $ Survived : Factor w/ 3 levels "0","1","None": 1 2 2 2 1 1 1 1 2 2 ... 
# $ Pclass : Factor w/ 3 levels "1","2","3": 3 1 3 1 3 3 1 3 3 2 ... 

# table uses the cross-classifying factors to build a contingency table 
# with the counts at each combination of factor levels 

table(data.combined$Survived)

# output 

#    0   1 None 
#  549 342 418 

# load ggplot2 library for visualizations
library(ggplot2)

# load stringr - deals with "NA"'s and zero length vectors
library(stringr)

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


# Since we only have survived labels for the train set, 
# only use the first 891 rows
ggplot(data.combined[1:891,], aes(x = Title, fill = Survived)) +
  stat_count(width = 0.2) + 
  facet_wrap(~Pclass) + 
  ggtitle("Pclass") +
  xlab("Title") +
  ylab("Total Count") +
  labs(fill = "Survived")

# output: refer image
