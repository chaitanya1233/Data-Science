# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 11:15:38 2026

@author: chait
"""

############################################################

#-----------------------------------------
#Step 1:Import the libraries 
#-----------------------------------------

import pandas as pd
import numpy as np
import matplotlib. pyplot as plt
import seaborn as sns

from sklearn. model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer
from scipy. stats import skew
from feature_engine. outliers import Winsorizer
from imblearn.over_sampling import SMOTE

#---------------------------------------------------
#Step 2: Load the dataset 
#---------------------------------------------------

df =  pd.read_excel("C:\\12-Ensemble_techniques- Boosting\\Coca_Rating_Ensemble.xlsx")
df

print(f"Initial shape:\n{df.shape}")
print(df.head())

##############################################################

#--------------------------------------------------
# Step 3 : Basic EDA
#--------------------------------------------------


##############################################################
#--------------------------------------
# Step 3:Basic cleaning 
#--------------------------------------

# Drop the REF column (indentifier - no predictive value)

df.drop(columns = ['REF'],inplace = True)

"""
Inferance :
    REF does not contains any relevent information 
    it only contains the ids.
"""
##############################################################

#------------------------------------------------
# Step 4 : Missing values analysis
#------------------------------------------------

# Separate the numeric and categorical columns 
num_cols = df.select_dtypes(include = ['int64','float64']).columns
cat_cols = df.select_dtypes(include = ['object']).columns

# Median imputation for numeric

for col in num_cols:
    df[col].fillna(df[col].median(),inplace = True)

# Mode imputation for categorical columns 

for col in cat_cols:
    df[col].fillna(df[col].mode()[0],inplace = True)


print("Missing values after imputation:\n",df.isna().sum())


"""
Infereance :
Median used because cocoa % and rating may be skewed.
Prevent distortion due to extreme values
"""

#--------------------------------
# Step 5: Duplicate Removal
#--------------------------------

df.drop_duplicates(inplace=True)
print("After removing duplicates:", df.shape)

'''
Inference:
Ensures model does not Learn repeated patterns.
Improves generalization
'''

#-------------------------------
# step 6:Outlier detection 
#----------------------------------

plt.figure(figsize=(8,5))
sns. boxplot(data=df)
plt. title( "Boxplot Before Winsorization AQ")
plt. show()

'''
Observation:
Outliers visible in Cocoa_Percent (high 90-100% values)
Mild rating extreme
'''


# Step 7: winsorization 

winsor = Winsorizer(
    capping_method='iqr',
    tail = 'both',
    fold = 1.5,
    variables=['Cocoa_Percent','Rating'])

df[['Cocoa_Percent','Rating']] = winsor.fit_transform(df[['Cocoa_Percent','Rating']])
df.columns

sns.boxplot(data = df[['Cocoa_Percent','Rating']])
plt.title("After winsorization")
plt.show()

'''
Inference:
Extreme cocoa values capped.
Distribution preserved.
Improves stability slightly.
Optional for tree based models.
'''


# Step 8 : skewness check 

"""
Tree based models like ADABoosts :
    - DO not requries a LOG transformation
    - They spplit on threshold , not distribution shape 
    - so no transformation is required .
"""
#------------------------------------------------------
# Step 9: Convert Rating to classification Target
#------------------------------------------------------

# High Rated (1) if Rating >= 3.5 else 0

df['High_Rating'] = np.where(df['Rating']>=3.5,1,0)
    
df.drop(columns = ['Rating'],inplace= True)


"""
INferance:
Why convert?
SMOTE works only for classification.
Now target = High_Rating
"""

#----------------------------------------
# Step 10 : Feature and Target split 
#----------------------------------------

X = df.drop(columns ="High_Rating")
y = df['High_Rating']

# -----------------------------------------
# Step 11:Train-Test split 
#-------------------------------------------

X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y)


#----------------------------------------
# Step 12: check if SMOTE is requried.
#----------------------------------------

class_ratio = y_train.value_counts(normalize = True)
print("Class Ratio:\n",class_ratio)

"""
NO need of SMOTE
Class imbalace is mild 
Ex: 
    - 60 % vs 40%
    - 65% vs 35%

"""


# Indntify the categorical columns 

cat_cols = df.select_dtypes(include = ['object']).columns

# One Hot Encoding 

X_train = pd.get_dummies(X_train,columns=cat_cols,drop_first=True)
X_test = pd.get_dummies(X_test,columns=cat_cols,drop_first=True)

# Allign train and test columns 
X_train,X_test = X_train.align(X_test,join='left',axis=1,fill_value = 0)

# Adaboosting model

base_model = DecisionTreeClassifier(max_depth=2)

ada_model = AdaBoostClassifier(
    estimator=base_model,
    n_estimators=100,
    learning_rate = 0.5,
    random_state = 42
    )

ada_model.fit(X_train,y_train)

# Model Evaluations

y_pred = ada_model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))
print("\nConfusion matrix:\n",confusion_matrix(y_test,y_pred))
print("Classification report:\n",classification_report(y_test, y_pred))



