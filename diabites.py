# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 21:49:22 2026

@author: chait
"""

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
df = pd.read_csv("C:/Data  Set/Diabeted_Ensemble.csv")

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

print("\nMean:\n", df.mean())
print("\nVariance:\n", df.var())
print("\nStd Dev:\n", df.std())
print("\nSkewness:\n", df.skew())
print("\nKurtosis:\n", df.kurtosis())

#chatgpt code
num_df = df.select_dtypes(include=['int64', 'float64'])

print("\nMean:\n", num_df.mean())
print("\nVariance:\n", num_df.var())
print("\nStd Dev:\n", num_df.std())
print("\nSkewness:\n", num_df.skew())
print("\nKurtosis:\n", num_df.kurtosis())

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
    variables=list(df.columns[:-1])
)

df[df.columns[:-1]] = winsor.fit_transform(df[df.columns[:-1]])


# ------------------------------------------------------------
# STEP 6: FEATURE SCALING (NORMALIZATION)
# ------------------------------------------------------------
def norm_func(i):
    return (i - i.min()) / (i.max() - i.min())

df_norm = norm_func(df.iloc[:, :-1])


# ------------------------------------------------------------
# STEP 7: DEFINE PREDICTORS & TARGET
# ------------------------------------------------------------
X = df_norm
y = df["Outcome"]

print("\nTarget Distribution:\n", y.value_counts())


# ------------------------------------------------------------
# STEP 8: TRAIN–TEST SPLIT
# ------------------------------------------------------------
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ------------------------------------------------------------
# MODEL DEVELOPMENT – BAGGING
# ------------------------------------------------------------
dt = DecisionTreeClassifier(random_state=42)

bag_model = BaggingClassifier(
    estimator=dt,
    n_estimators=500,
    bootstrap=True,
    random_state=42
)




bag_model.fit(x_train, y_train)

bag_pred_test = bag_model.predict(x_test)
bag_pred_train = bag_model.predict(x_train)

print("\nBagging Test Accuracy:", accuracy_score(y_test, bag_pred_test))
print("Bagging Train Accuracy:", accuracy_score(y_train, bag_pred_train))


# ------------------------------------------------------------
# MODEL DEVELOPMENT – ADABOOST
# ------------------------------------------------------------
ada_model = AdaBoostClassifier(
    n_estimators=500,
    learning_rate=0.02,
    random_state=42
)

ada_model.fit(x_train, y_train)

ada_pred_test = ada_model.predict(x_test)
ada_pred_train = ada_model.predict(x_train)

print("\nAdaBoost Test Accuracy:", accuracy_score(y_test, ada_pred_test))
print("AdaBoost Train Accuracy:", accuracy_score(y_train, ada_pred_train))


# ------------------------------------------------------------
# MODEL DEVELOPMENT – GRADIENT BOOSTING
# ------------------------------------------------------------
gb_model = GradientBoostingClassifier(random_state=42)
gb_model.fit(x_train, y_train)

gb_pred_test = gb_model.predict(x_test)
gb_pred_train = gb_model.predict(x_train)

print("\nGradient Boosting Test Accuracy:", accuracy_score(y_test, gb_pred_test))
print("Gradient Boosting Train Accuracy:", accuracy_score(y_train, gb_pred_train))


# ------------------------------------------------------------
# MODEL DEVELOPMENT – STACKING
# ------------------------------------------------------------
base_learners = [
    ('knn', KNeighborsClassifier(n_neighbors=5)),
    ('dt', DecisionTreeClassifier(max_depth=4, random_state=42)),
    ('nb', GaussianNB())
]

meta_learner = LogisticRegression()

from sklearn.ensemble import StackingClassifier

stack_model = StackingClassifier(
    estimators=base_learners,
    final_estimator=meta_learner
)

stack_model.fit(x_train, y_train)

stack_pred_test = stack_model.predict(x_test)
stack_pred_train = stack_model.predict(x_train)

print("\nStacking Test Accuracy:", accuracy_score(y_test, stack_pred_test))
print("Stacking Train Accuracy:", accuracy_score(y_train, stack_pred_train))


# ------------------------------------------------------------
# MODEL DEVELOPMENT – VOTING
# ------------------------------------------------------------
voting_hard = VotingClassifier(
    estimators=[
        ('knn', KNeighborsClassifier(n_neighbors=5)),
        ('svc', SVC(gamma=0.01)),
        ('lr', LogisticRegression())
    ],
    voting='hard'
)

voting_hard.fit(x_train, y_train)
hard_pred = voting_hard.predict(x_test)

print("\nHard Voting Accuracy:", accuracy_score(y_test, hard_pred))


voting_soft = VotingClassifier(
    estimators=[
        ('knn', KNeighborsClassifier(n_neighbors=5)),
        ('nb', GaussianNB()),
        ('svc', SVC(gamma=0.01, probability=True))
    ],
    voting='soft'
)

voting_soft.fit(x_train, y_train)
soft_pred = voting_soft.predict(x_test)

print("Soft Voting Accuracy:", accuracy_score(y_test, soft_pred))


# ------------------------------------------------------------
# MODEL TUNING – GRID SEARCH (EXAMPLE: RANDOM FOREST STYLE)
# ------------------------------------------------------------

param_grid = {
    'n_estimators': [100, 300],

    'learning_rate': [0.01, 0.05, 0.1]
}

grid_ada = GridSearchCV(
    AdaBoostClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid_ada.fit(x_train, y_train)

print("\nBest AdaBoost Parameters:", grid_ada.best_params_)
print("Best CV Accuracy:", grid_ada.best_score_)


# ------------------------------------------------------------
# FINAL BUSINESS IMPACT
# ------------------------------------------------------------
'''
• Ensemble models significantly improve diabetes prediction accuracy
• Bagging reduces variance and overfitting
• Boosting improves weak learners
• Stacking combines strengths of multiple models
• Voting provides stable predictions

Business Benefits:
• Early diabetes detection
• Better clinical decision support
• Reduced diagnostic errors
• Scalable ML-assisted healthcare analytics
'''

print("Diabetes Ensemble Modeling Completed Successfully ")



#data preprocessing
#step1 : import required libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer
from imblearn.over_sampling import SMOTE

#step2 : Load DataSet
df= pd.read_csv("C:/Data  Set/Diabeted_Ensemble.csv")


df.columns=[
    "pregnancies", "glucose","BP","skin_thickness",
    "Insulin","BMI","D_pedgree","Age","Outcome"]

print("Initial Shape:",df.shape)
df.head()

#step3
print("Missing values:\n",df.isnull().sum())

'''
there is no NoNs,
'''
#step6: 
num_cols= df.columns.drop("Outcome")

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

#step7 duplicate removal
df.drop_duplicates(inplace=True)
print("After removing duplicates:",df.shape)


#step8 :outlier Detection (Boxplots)

plt.figure(figsize=(10,6))
sns.boxplot(data=df.drop(columns='Outcome'))
plt.title("Boxplot Before outlier Treatment")
plt.show()

#step9:Outlier Treatment using Winsorization
winsor = Winsorizer(
    capping_method='iqr',
    tail='both',
    fold=1.5,
    variables=['BP','Insulin','skin_thickness','BMI','Age'])
      
df[['BP','Insulin','skin_thickness','BMI','Age']] = winsor.fit_transform(
    df[['BP','Insulin','skin_thickness','BMI','Age']])
  
    
sns.boxplot(data=df[['BP','Insulin','skin_thickness','BMI']])   
plt.title('Boxplot After Winsorization')    
plt.show()   
    
#step:10 using    
skew_values =df[num_cols].apply(lambda x: skew(x))    
skew_values    
    
df["Insulin_log"]  = np.log1p(df['Insulin']) 
df["D_pedgree_log"]  = np.log1p(df['D_pedgree'])  
df['Age_log']  =np.log1p(df['Age'])  
    
sns.histplot(df['Insulin'], kde=True)    
sns.histplot(df['Insulin_log'], kde=True).set_title("Insulin after Log Transform")    
sns.histplot(df['Age'], kde=True)  
'''
Standardization  or Normalization is NOT required for
Decision Tree-based models such as Decision Trees,
Bagging ,Random Forest ,and Gradient  Boosting.
 
'''
#step11: Featured & Target Split 
X = df.drop(columns='Outcome') 
y = df['Outcome']


#step12: Train-test Split (Before SMOTE)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#step13 :Handled NaNs (SMOTE requirment)
 
from sklearn.impute import SimpleImputer

imputer =SimpleImputer(strategy='median')    
 
X_train_imputed = imputer.fit_transform(X_train)   
X_test_imputed = imputer.transform(X_test) 
    
#step14: apply SMOTE (only on training data)
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train_imputed, y_train
)

print("Before SMOTE:\n", y_train.value_counts())
print("After SMOTE:\n", pd.Series(y_train_smote).value_counts())

#Inference

#Training data is now balanced

#Mintory (Diabetic) class strengthened

#Test data remains real-world

#step15: Bagging_model(using smote data)
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier 
from sklearn.metrics import accuracy_score, classification_report 
 
dt = DecisionTreeClassifier(
    random_state=42)   
 
bag_model = BaggingClassifier(
    estimator=dt,
    n_estimators=500,
    bootstrap=True,
    random_state=42,
    n_jobs=-1
)

bag_model.fit(X_train_smote,y_train_smote)

 
#step 5
y_pred_train = bag_model.predict(X_train_smote)    
y_pred_test = bag_model.predict(X_test_imputed)
    
print("Bagging Train Accurracy:",
      accuracy_score(y_train_smote, y_pred_train))
    
print("Bagging Test Accuracy:",
      accuracy_score(y_test,y_pred_test)) 
    
#step6:
print("\nClassification Report (Test Data):\n")
print(classification_report(y_test, y_pred_test))    
 
#------------------------------------------ 
#Optimization
#---------------------------------------
'''
Why you are current Model IS overfitting
whta's happning now
Train Acurracy - Very High(~100%)
Test Acurracy - Much Lower
Root causes
Decision Tree is unrestricted 
max_depth=None
min_samples_Leaf=1
Bagging amplifies complex trees
SMOTE introduces synthetic points
Deep trees memorize SMOTE samples
Bagging reduces variance,
but only if base trees are weak learners 

Golden rule for Bagging (very important)

'''
#  Feature Scaling
#step2: Bagging with Controlled Trees 
from sklearn.ensemble import BaggingClassifier

bag_model = BaggingClassifier(
    estimator =dt,
    n_estimators=200,     #500 is often necessary
    bootstrap=True,
    max_samples=0.8,       #row sampling 
    )                      #featured sampling


#basic eda
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df.head()

df.shape

df.columns

df.dtypes

df.describe()

df.isnull().sum()

df.duplicated().sum()










