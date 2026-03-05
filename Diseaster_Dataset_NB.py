# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 21:59:32 2026

@author: chait
"""

#############################################################

# Buisness and Data Understanding 



"""
 1️⃣ Business Problem Statement
 
In emergency situations such as floods, earthquakes, fires, and explosions, people post real-time updates on social media platforms like Twitter.
However:
Not all tweets mentioning words like “fire”, “storm”, or “explosion” indicate real disasters.
Many tweets use such words metaphorically.
The challenge is:
Automatically classify whether a tweet refers to a real disaster event or not.

2️⃣ Business Objective
The main objective is to:
Build a machine learning model that can classify tweets as:
1 → Real Disaster
0 → Not a Disaster
Enable faster disaster detection from social media data.
Support emergency response systems with real-time alerts.
3️⃣ Business Motivation
Why is this important?
Early disaster detection saves lives.
Governments can respond quickly.
News agencies can verify events faster.
Disaster management authorities can prioritize rescue operations.
Real-time tweet classification helps reduce manual monitoring efforts.
4️⃣ Stakeholders
Government disaster management authorities
Emergency response teams
NGOs
News agencies
Social media monitoring teams
5️⃣ Constraints
Tweets are short and unstructured text.
Many tweets use sarcasm or figurative language.
Class imbalance (usually fewer disaster tweets).
High dimensional text data.
Need for fast prediction in real-time systems.
6️⃣ Success Criteria
🔹 Business Success Criteria
Correctly detect real disaster tweets.
Minimize false negatives (missing real disasters).
Provide near real-time classification.
🔹 Machine Learning Success Criteria
Good Accuracy (>75%)
High Recall for Disaster class
Balanced Precision & Recall
Good F1-Score
7️⃣ Type of Problem
Supervised Machine Learning
Binary Classification Problem
Text Classification Task
NLP (Natural Language Processing) domain
8️⃣ Expected Business Impact
Faster disaster response
Improved emergency planning
Reduced manual tweet monitoring cost
Better public safety management"""



# ------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sns 

# ------------------------------------------------------------
# STEP 2: LOAD TRAIN AND TEST DATASETS
# ------------------------------------------------------------

df = pd.read_csv("../../3-Python for Data Science/Disaster_tweets_NB.csv")
df

# ------------------------------------------------------------
# STEP 3: BASIC EDA
# ------------------------------------------------------------

# Checking the data types of the columns 
print("Data types of the columns:\n",df.dtypes)
print("Summary statistics:\n",df.describe())

"""
Inference:
Most of the columns are the string , 
so summary statistics is irrelevant.
"""

# Finding the missing values in each column

print("Missing values per column:\n",df.isna().sum())

"""
Inference:
    - There are missing values in 'Keyword' and 'location'
    columns , so need to impute the missing values by mode.
"""


#--------------------------------------------------------
# BUSINESS MOMENT DECISIONS
# ------------------------------------------------------------

"""\
Inference :
 As the datset contains categorical columns 
 We cannot perform the buisness moment decisions on the 
 Text dataset.
"""


# -------------------------------
# Overall EDA Conclusion
# -------------------------------
"""
Inferece:
-The Disester Dataset exhibits missing values.

-Appropriate preprocessing step such as cleaning and filling
 is recommended before applying machine learning models.

-Need to apply the transformation techniques before applying the 
 machine learning model on the dataset.
"""

# ============================================================
# Exploratory Data Analysis (EDA) with Inline Inference
# ============================================================

# Basic understading of the data 

df.head() # Initial 5 rows 
df.tail() # Last 5 rows
df.size # rows * columns 
df.columns # Names of the columns
print("(Rows,columns):",df.shape)

"""
Inference:
    - Diseaster dataset contains most of the categorical columns ,
    - only Id and Target column is numeric
    having the binary class classification problem ;
    0 --> Diseaster at realtime 
    1 --> Diseaster not at realtime
"""

# ------------------------------------------------------------
# Target Variable Distribution
# ------------------------------------------------------------

df['target'].value_counts()
sns.countplot(x = 'target',data = df)
plt.show()

"""
Inference:
    -  Data is slight imbalance 
    - This imbalance need to be considered while model evaluation
"""

# ------------------------------------------
# Data cleaning 
#-------------------------------------------


# Indetify the missing columns 

print("Following are the missing columns:\n",df.isna().sum())

"""Inference:
    - Missing columns are: keyword , location 
    - They are categorical columns 
    - Strategy to be applied is : Replace the missing 
        values by mode of first occurance for 'location' column.
        and drop the missing cells for the 'keyword' column.
        Why to replace by mode only: Because most of the columns 
        are text columns.
"""

# Data cleaning for the 'keyword' column.
df = df.dropna(subset = ['keyword'])

df['location'] = df['location'].fillna(df['location'].mode()[0])

"""
# Alternate solution : SimpleImputer()

from sklearn.impute import SimpleImputer

si = SimpleImputer(strategy='most_frequent')
df[['location']] = si.fit_transform(df[['location']])
"""

# Checking the missing values.
print("Follwing are the missing values:\n",df.isna().sum())

######################################################################

#-------------------------------------------------
# One-Hot Encoding Categorical Features
# ------------------------------------------------------------

df_encoded = pd.get_dummies(df, drop_first=True)
print("Shape after encoding:", df_encoded.shape)

# Inference:
# Converts categorical variables into numeric format.
# drop_first=True avoids dummy variable trap.

#########################################################

# ------------------------------------------------------------
# Train-Test Split
# ------------------------------------------------------------

from sklearn.model_selection import train_test_split

X = df_encoded.drop('target', axis=1)
y = df_encoded['target']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

"""
Inference:
- Stratified split maintains class distribution.
"""



# ------------------------------------------------------------
# Final Preprocessing Summary
# ------------------------------------------------------------
"""
Inference:
1. Missing values handled appropriately.
2. Categorical column data is encoded successfully.
3. Dataset is now ML-ready.
"""


# ============================================================
# Naive Bayes Model Development (Two Separate Datasets)
# ============================================================

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE


# ------------------------------------------------------------
# GAUSSIAN NAIVE BAYES MODEL
# ------------------------------------------------------------
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# ------------------------------------------------------------
# PREDICTION
# ------------------------------------------------------------
y_test_pred  = nb_model.predict(X_test)
y_train_pred = nb_model.predict(X_train)

# ------------------------------------------------------------
# STEP 10: MODEL EVALUATION – TEST DATA
# ------------------------------------------------------------
print("\nTest Accuracy:", accuracy_score(y_test, y_test_pred))
print("\nConfusion Matrix (Test):\n", confusion_matrix(y_test, y_test_pred))
print("\nClassification Report (Test):\n", classification_report(y_test, y_test_pred))

# ------------------------------------------------------------
# STEP 11: MODEL EVALUATION – TRAIN DATA
# ------------------------------------------------------------
print("\nTrain Accuracy:", accuracy_score(y_train, y_train_pred))
print("\nConfusion Matrix (Train):\n",confusion_matrix(y_train, y_train_pred))

#############################################################    
"""
📌 Model Conclusion
🎯 Model Used

Gaussian Naive Bayes

📊 Performance Results

Training Accuracy: 79.98%

Testing Accuracy: 71.74%

🔎 Interpretation of Results
1️⃣ Generalization Performance

The model performs reasonably well but shows a noticeable gap between training and testing accuracy:

Training Accuracy  = 79.98%
Testing Accuracy   = 71.74%
Difference         ≈ 8%


This indicates mild overfitting — the model performs better on training data than unseen test data.

2️⃣ Model Quality Assessment

Accuracy is above 70%, which is acceptable for a basic baseline model.

However, for disaster detection systems, recall is more critical than accuracy, because:

Missing a real disaster tweet (False Negative) is costly.

It may delay emergency response.

You should check:

Recall for class 1 (Disaster)

F1-score for balanced performance

3️⃣ Technical Limitation of Current Approach

The current pipeline:

Uses one-hot encoding for text

Does not use proper NLP vectorization (TF-IDF / CountVectorizer)

Uses GaussianNB (better for continuous data)

For text classification, better choices are:

Multinomial Naive Bayes

TF-IDF + Logistic Regression

TF-IDF + Linear SVM

📈 Business Conclusion

The model provides a reasonable baseline performance (71.74%) and demonstrates feasibility of automated disaster tweet classification.

However:

Performance is not yet strong enough for real-world emergency deployment.

Further improvements are required to increase recall and reduce false negatives.
"""

