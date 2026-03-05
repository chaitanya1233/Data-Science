# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:14:01 2026

@author: chait
"""

#############################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report



#-----------------------------------
# Exploratory Data Analysis(EDA)
#-----------------------------------

df = pd.read_csv("../../3-Python for Data Science/Company_Data.csv")
df

# First moment decision : Mean
df.mean(numeric_only = True)
"""
Inferance :
"""

# Second moment decision : Variance and SD

df.var(numeric_only = True)
df.std(numeric_only = True)

"""
Inferance :
- High variance observed in :
    compPrice 
    Income  
    Polulation 
    Price and Age 
"""    


# First moment decision : Skewness 

df.skew(numeric_only = True)

"""
sales -  Right skewed - Very few stores genrates high sales 
Advertizing - Right skewed - Very few stores spend on marketing  
price - slight skewed - 
Income - Near Symmetric 
Polullation - Mild sewed

Right skew indicates :
    - High sales and heavy advertising are concentrated in very few stores 
    - Tree based models are suitable for such distributions 

"""

# Fourth moment buisness decision 

df.kurtosis(numeric_only = True) 


df.hist(figsize = (14,10),edgecolor = 'black')
plt.suptitle("Histogram of all numerical features")
plt.show()


"""
Sales show slight right skewed , indicating most stores have 
moderate sales , with few high performing outliers 

CompPrice :
    - CompPrice are approx modrately distributred ,
    suggetsing stable andd competitive market priceing 

Income:
    -Income is farely evenly sprade across regions ,
    reflecting diverse coustomer purchasing power 

Advertising :
    - right skewed
    - means most stores spend less , few invests heavy in promotions 

Population:
    - Population is unifirmly distributed 
    - indicates , stores are across small and large market
    
Price:
    - Product prices follws normal distribution , 
    suggesting consistent pricing strategy with limitted 
    extrems
    
Age:
    - Age is evenly distributed , implying demand across 
    multiple age group.

education:
    -  Education levels shows discrate clusters
    - reflecting structured eduction categories 
"""
plt.figure(figsize=(14,6))
plt.boxplot(data = df.select_dtypes(include = np.number),orient='h')
plt.title("Boxplot of all numerical features.")
plt.show()


"""
Inference:
Sales:
Few high-value outliers indicate exceptionally high-performing stores,
which can heavily influence average sales.
CompPrice:
Presence of outliers suggests price variation among competitors,
reflecting competitive market conditions.
Income :
Moderate spread with Limited outliers indicates stable income
distribution across regions.

Advertising:
Strong right-side outliers show that only a few stores
invest heavily in advertising, while most spend modestly.

Population:
Very wide range and Large IQR indicate stores operate in
both small towns and Large cities, explaining demand variability.

Price:
Some outliers exist, implying premium and discounted pricing
strategies in certain markets.

Age :
Narrow IQR with minimal outliers suggests customer age
is relatively consistent across regions.

Education:
Very small spread indicates education Levels are fairly uniform,
contributing less variability compared to other features.

"""

# Target Variable Distribution (Sales Category)
# Create Sales Category (if not already created)
bins = [0, 5, 10, 15, 20]
labels = ['Low', 'Average', 'Good', 'Better ' ]
df[ 'Sales_cat'] = pd. cut(df[ 'Sales'], bins=bins, labels=labels)
sns. countplot(x='Sales_cat', data=df)
plt. title ( "Sales Category Distribution")
plt. show()


"""
Inference :
    - Slaes categories are reasonable balanced ,
    - No severe class imbalaced 
    - SMOTE is not rewquired 
    - Why SMOTE is not required (Based on the graph.)
    

From the Sales Category Distribution:

Average > majority class

Low and Good > reasonably represented

Better > very small class

This is mild to moderate imbalance, not 'severe imbalance.

When SMOTE is required

SMOTE is recommended when:
- there is high Class imbalance is there.

* Why SMOTE is a bad idea here

Your models are Decision Tree / Random Forest

Tree-based models :
Handle imbalance better than linear models
Learn from class boundaries, not distance

SMOTE can:
- Create synthetic, unrealistic sales patterns
- Increase overfitting
- Distort genuine business distributions
- Best practice for this dataset     
"""

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns . heatmap(df. corr(numeric_only=True), annot=True, cmap='coolwarm' )
plt. title ( "Feature Correlation Heatmap")
plt. show()


"""
Sales vs Price (-0.44)
Moderate negative correlation indicates that higher
prices reduce sales, confirming price sensitivity.

Sales vs Advertising (0.27)
Positive correlation shows advertising increases sales,
though the impact is moderate.

Sales vs Income (0.15)
Weak positive correlation suggests higher-income regions
tend to generate slightly higher sales.

Sales vs Age (-0.23)
Negative correlation indicates sales are relatively higher
in younger markets

Sales vs CompPrice (0.06)
Very weak correlation shows competitor pricing has Limited
direct impact on sales.

CompPrice vs Price (0.58)
Strong positive correlation indicates pricing strategies
closely follow competitors.

Advertising vs Population (0.27)
Moderate positive correlation suggests higher advertising
spend in densely populated markets.
Other Feature Pairs

Most correlations are weak, indicating Low multicollinearity

"""


# Scatter Plot (Business Relationship)
sns . scatterplot(x='Price', y='Sales', data=df)
plt. title( "Price vs Sales")
plt. show()

"""
Inference:
Higher prices generally lead to Lower sales.
Confirms price sensitivity in the market.
"""


# PDF & CDF Analysis
for col in df. select_dtypes(include=np.number). columns:
    plt.figure(figsize=(12,4))
    # PDF
    plt.subplot(1,2,1)
    sns.kdeplot(df[col], fill=True)
    plt.title(f'PDF of {col}')
    # CDF
    plt.subplot(1,2,2)
    sorted_vals = np. sort(df[col])
    y = np. arange(len(sorted_vals)) / len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of {col}')
    plt.show()


"""
Inference:
    
PDF shows sales concentration around mid-range values.
CDF helps identify thresholds, e.g.,
80% of stores have sales below a certain Level.
Useful for inventory planning.
"""

# Pairplot (Feature Interaction)
sns.pairplot(df[['Sales','Price','Advertising','Income','Population']])
plt.show()

"""
Inference:

Advertising shows positive association with Sales.
Price shows inverse relationship with Sales.
Population amplifies sales potential.

"""

