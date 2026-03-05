# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:31:31 2026

@author: chait
"""

#############################################################

# ============================================================
# DIABETES PREDICTION USING ENSEMBLE LEARNING
# (Bagging, Boosting, Stacking, Voting + GridSearchCV)
# ============================================================

# ------------------------------------------------------------
# BUSINESS UNDERSTANDING
# ------------------------------------------------------------
# 1. Business Problem Statement:
# Diabetes is a chronic disease that is becoming increasingly
# common due to changes in lifestyle and living standards.
# Early diagnosis helps prevent severe complications.

# 2. Business Objective:
# - Predict whether a patient has diabetes
# - Assist doctors with preliminary diagnosis
# - Improve prediction accuracy using ensemble models

# 3. Motivation:
# Medical diagnosis is often complex and uncertain.
# Machine learning models can analyze patient health indicators
# to support clinical decision-making.

# 4. Constraints:
# - Feature selection is critical
# - Model selection impacts accuracy
# - Dataset contains only Pima Indian women aged ≥21

# 5. Success Criteria:
# Business Success:
# - Early and reliable diabetes detection
# ML Success:
# - Improved accuracy using ensemble methods
# - Robust generalization on unseen data


# ------------------------------------------------------------
# DATA UNDERSTANDING
# ------------------------------------------------------------
'''
| Feature Name              | Description                                   | Type    |
|---------------------------|-----------------------------------------------|---------|
| Pregnancies               | Number of times pregnant                      | Numeric |
| Glucose                   | Plasma glucose concentration                  | Numeric |
| BloodPressure (BP)        | Diastolic blood pressure                      | Numeric |
| Skin_thickness            | Triceps skin fold thickness                   | Numeric |
| Insulin                   | 2-hour serum insulin                          | Numeric |
| BMI                       | Body mass index                               | Numeric |
| D_pedigree                | Diabetes pedigree function                    | Numeric |
| Age                       | Age in years                                  | Numeric |
| Outcome                   | 1 = Diabetic, 0 = Non-diabetic (Target)       | Binary  |
'''

# Key Insights:
# - All features are numerical
# - Binary classification problem
# - Medical data contains outliers
# - Ensemble models are suitable




# ------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    VotingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from feature_engine.outliers import Winsorizer


# ------------------------------------------------------------
# STEP 2: LOAD THE DATASET
# ------------------------------------------------------------
df = pd.read_csv("../../3-Python for Data Science/Diabeted_Ensemble.csv")

df.columns
# Rename columns for clarity
df.columns = [
    "Pregnancies", "Glucose", "BP", "Skin_thickness",
    "Insulin", "BMI", "D_pedigree", "Age", "Outcome"
]

print(df.head())


# ------------------------------------------------------------
# STEP 3: BASIC EDA
# ------------------------------------------------------------
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())

# ------------------------------------------------------------
# BUSINESS MOMENT DECISIONS
# ------------------------------------------------------------

print("\nMean:\n", df.mean(numeric_only = True))
print("\nVariance:\n", df.var(numeric_only = True))
print("\nStd Dev:\n", df.std(numeric_only = True))
print("\nSkewness:\n", df.skew(numeric_only = True))
print("\nKurtosis:\n", df.kurtosis(numeric_only = True))


# ------------------------------------------------------------
# STEP 4: UNIVARIATE ANALYSIS
# ------------------------------------------------------------
df.hist(figsize=(12, 10))
plt.suptitle("Histograms of Diabetes Features")
plt.show()


# ------------------------------------------------------------
# STEP 5: OUTLIER TREATMENT (WINSORIZATION)
# ------------------------------------------------------------
winsor = Winsorizer(
    capping_method="iqr",
    tail="both",
    fold=1.5,
    variables=[ 'BP', 'Insulin', 'Skin_thickness', 'BMI' , 'Age']
)

df[['BP','Insulin','Skin_thickness','BMI', 'AGE']] =winsor.fit_transform(df[[ 'BP' , 'Insulin', 'Skin_thickness' , 'BMI', 'Age']]
)

sns. boxplot(data=df[ [ 'BP', 'Insulin', 'Skin_thickness', 'BMI']])
plt. title( "Boxplot After Winsorization")
plt. show()

"""Inference:
Outliers capped
T
Selecting_best_threshold_AUC_ROC_2025.py X
Medical extremes preserved
Model stability improved
"""

# Step 10: Skewness Detection & Transformation
skew_values = df[num_cols].apply(lambda x: skew(x))
skew_values


df['Insulin_log'] = np. log1p(df['Insulin'])
df[ 'D_pedigree_log' ] = np. log1p(df['D_pedigree'])
df [ 'Age_Log' ] = np. log1p(df[ 'Age'])


sns. histplot(df['Insulin'], kde=True)
sns. histplot(df['Insulin_log'], kde=True) .set_title("Insulin After Log Transform")
sns. histplot(df[ 'Age'], kde=True)



"""
Log transformation:
Reduces skew
Improves Linear model performance
"""

# Inference:

"""
If Winsorization Is Done, Do We Still Need Log Transformation?
 Short, Correct Answer
Not necessarily.
Winsorization and log transformation solve different problems.
Whether you need both depends on why you’re transforming the data.
 What Each Technique Actually Fixes
 Winsorization
Purpose:
Handles outliers (extreme values)
How it works:
Caps extreme values at IQR-based limits
Does not change the shape of the distribution much
Fixes:
 Extreme tails
 Skewness (mostly remains)
 Log Transformation
Purpose:
Handles skewness (asymmetry)
How it works:
Compresses large values
Pulls right tail closer to the center
Fixes:
 Right skew
 Extreme outliers (if they exist)
 So, Do We Need Log After Winsorization?
 Case 1: Tree-Based Models (DT, Bagging, RF, Boosting)
 NO — Log transformation is NOT required
Why?
Trees split on order, not distribution
They handle skewness naturally
Winsorization alone is enough (sometimes even that is optional)

 Recommended:
Winsorization → optional
Log transform → unnecessary
Case 2: Linear / Distance-Based Models
(Logistic Regression, SVM, KNN)
 YES — Often required
Why?
These models assume:
linear relationships
symmetric distributions
Even after winsorization, skewness may remain
Recommended:
Winsorization → Log Transformation → Scaling
"""


# Feature Scaling
# Standardization

'''Standardization or normalization is NOT required for
Decision Tree-based models such as Decision Trees,
Bagging, Random Forest, and Gradient Boosting.'''

# Step 11: Feature & Target Split
X = df.drop(columns='Outcome')
y = df[ 'Outcome']

#STEP 12: Train-Test Split (Before SMOTE)

from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y)


# Why stratify?
# It perserves original class ratio in test sets 


# Step 13:Handels NaN's  (SMOTE is required.)
from sklearn.impute import SimpleImputer

si = SimpleImputer(strategy='median')

X_train_imputed = si.fit_transform(X_train) 
X_test_imputed = si.transform(X_test)


# Why fit only on training data ?
# To avoid data leakage 

# Step 14: Apply SMOTE (ONLY on training data)
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_smote,y_train_smote = smote.fit_resample(
    X_train_imputed,y_train)


print("Before SMOTE: \n", y_train.value_counts())
print("After SMOTE: \n", pd.Series(y_train_smote).value_counts())

# Inference
"""
Training data is now balanced
Minority (Diabetic) class strengthened
Test data remains real-world
"""
# STEP 15: BAGGING MODEL (Using SMOTE Data)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report

dt = DecisionTreeClassifier(
random_state=42
)

bag_model = BaggingClassifier(
    estimator=dt,
    n_estimators=500,
    bootstrap=True,
    random_state=42,
    n_jobs =- 1
)

bag_model.fit(X_train_smote, y_train_smote)

# STEP 5: Predictions
y_pred_train = bag_model.predict(X_train_smote)
y_pred_test = bag_model.predict(X_test_imputed)
print("Bagging Train Accuracy:",
      accuracy_score(y_train_smote, y_pred_train))

print("Bagging Test Accuracy: ",
accuracy_score(y_test, y_pred_test))

# STEP 6: Better Evaluation (Medical ML)
print ("InClassification Report (Test Data) : \n")
print(classification_report(y_test, y_pred_test))

###############################################
# Optimization
###############################################

"""
WHY your current model is overfitting , 
what is happening now ?,
