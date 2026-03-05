# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 23:43:17 2026

@author: chait
"""

#########################################################

#-----------------------------------------
# Step 1: Buisness and data understanding
#-----------------------------------------

# Buisness Understanding.


# Data Understanding 



#################################################

#------------------------------------------
# Step 2: Importing the Libraries 
#------------------------------------------

import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

#------------------------------------------
# Step 3:Load the dataset  
#------------------------------------------

zoo = pd.read_csv("../../8-KNN/Zoo.csv")

#------------------------------------------
# Step 3: Data Understanding   
#------------------------------------------

zoo.dtypes  # Data types of the features. 
zoo.columns # Names of the features. 
zoo.shape # Number of rows and column.
zoo.describe() # Descriptive statistics.


"""
Inference :
     - Most of the features are numerical.(Boolen encoded)
     -  Target varible is integer (boolean encoded).
     - there are 101 rows and 18 columns.
     - dataset is moderate in size, meaning KNN is
         suiable for the classification.
"""

#------------------------------------------
# Step 4: Exploratory Data Analysis (EDA)  
#------------------------------------------

print("Shape of dataset:",zoo.shape)
print("Size of the dataset:",zoo.size)
"""
Inference:
    - There are 101 rows and 18 columns.
    -  "Animal name" is categorical , taget varible is 
    integer(bolean encoded), and rest all features are integer
    (boolean encoded.)
"""

# Summary statistics

zoo.describe()

"""
Inference:
    -  It gives relevant insights about the dataset.
"""

#------------------------------------------
# Step 4: Buisness moment decisions  
#------------------------------------------

# First Moment Buisness Decision

print(zoo.mean(numeric_only = True))

"""
Inference:
    - Mean tells us about the average of the datapoints
    -  Very important summary measure
"""

# Second Moment Bisness Decision - std and variance

print(zoo.std(numeric_only = True))
print(zoo.var(numeric_only = True))

"""
Infernece:
    - There is high variance in 'legs' and 'type' column, meaning
    wide range of animals are there with different legs count
    and animal type, meaning this has greate influence on the animal
    type detection.
"""
# Thrid Moment Bisness Decision -  skewness

zoo.skew(numeric_only = True)

"""
Inference :
    - Skewness tells us about the symmetry of dataset
    - Dataset is not sytmmetrically identical 
    - Positively skewed : 
        # feathers and  fins columns are moderatly 
          positive skewed ,meaning   
        # aitborn venemous,domestic columns are strongly
          positive skewed.
"""

# Fourth Moment Business Decisions - Kurtosis 

kurt_values = zoo.kurtosis(numeric_only = True)
print("Kurtosis:\n",kurt_values)
"""
Inferece:
    - Platokurtic - (<0) meaning  flat distribution 
    - leptokrutic - (>0) meaning peaks are there 
        (extrem values has greate influence on type of animal.)
"""

#------------------------------------------
# Step 5: Univariate Analysis -  Boxplot
#------------------------------------------

zoo.drop(columns = ['type']).hist(
    figsize = (18,9),
    edgecolor = 'black'
    )

plt.suptitle("Histogram of all the traits")
plt.tight_layout()
plt.show()

"""
Inference:
    -  Right skred :  feathres , airborn , aquatic , venemous , fins , domestic and type.
    -  left skewed : eggs , predator , toothed , breadthes , backnone , tail.
    -  noraml distribution (nearly): hair , milk, legs
"""

#------------------------------------------
# Step 6: Box plot  -  outliers detection.
#------------------------------------------

plt.figure(figsize = (12,6))
sns.boxplot(data = zoo.drop(columns = ['type']),orient='h')
plt.title("Boxlot of all the features")
plt.show()

"""
Inference:    
     -  There are some outlies in domestic ,
        legs, fins, venemous , backbone , airborn
        and feathers column 
    -  Though there are outliers in some column,
        but these traits are important.
        so instade of treating them as outliers is conceptually worong , 
        we can convert the oulier containig columns into the cotegorical data type and 
        apply one hot encoding , so they will not loose 
        meaning.
"""

