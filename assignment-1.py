# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 13:06:53 2026

@author: chait
"""

##################################################################

import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 


titanic = sns.load_dataset("titanic")
titanic

# How many rows and columns 
titanic.shape
titanic.size


# First 5 rows of dataset 
titanic.head()

# What are the differnt name of columns 

titanic.columns

# what is the datatypes of the columns 

titanic.dtypes


"""Key columns

survived → 0 = No, 1 = Yes

sex → male / female

pclass → Passenger class (1, 2, 3)

age → Age

fare → Ticket fare

embarked → Port of embarkation"""
##################################################################
# What is the distrubution of the fares 

sns.displot(titanic['fare'])

# what is the average fare of the titanic 
avg_fare = titanic['fare'].mean()
avg_fare
# Most of the fares are between 20 - 35 dollers 

sns.displot(titanic.sex) # Most of passengers were male 

sns.displot(titanic.alive)  # about 330 to 350 passsengers survived 
###############################################################

sns.heatmap(titanic)
#################################################################
# Joint plot.

#################################################################

sns.pairplot(titanic,kind = 'reg')

##########################################################

# Code for the survival distribution 
sns.countplot(x="survived", data=titanic)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passenger Count")
plt.show()

"""Interpretation

Majority of passengers did not survive

Indicates a class-imbalanced dataset

Important for modeling decisions (accuracy alone is misleading)

Use case: Target variable understanding."""


############################################################


# SSurvival by gender 

sns.countplot(x="sex", hue="survived", data=titanic)
plt.title("Survival by Gender")
plt.show()

"""Interpretation

Females had a much higher survival rate

Strong evidence of the “women first” policy

sex is a highly predictive feature

Use case: Feature importance intuition."""

#########################################################


# Survival by Passenger Class

sns.countplot(x="pclass", hue="survived", data=titanic)
plt.title("Survival by Passenger Class")
plt.show()
"""
Interpretation

1st class passengers had highest survival

3rd class had very low survival

Indicates socioeconomic bias in survival

Use case: Ordinal categorical analysis.
"""

###############################################################

# 5. Histogram – Age Distribution

sns.histplot(titanic["age"], bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.show()

"""Interpretation

Most passengers were young adults

Right-skewed distribution

Presence of children and elderly

Use case: Detect skewness, missing values, age groups."""

####################################################################