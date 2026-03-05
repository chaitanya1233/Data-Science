# ============================================================
# GLASS TYPE CLASSIFICATION USING KNN
# ============================================================
"""
A glass manufacturing plant uses different earth elements
to design new glass materials based on customer requirements.
Manual classification of glass type is tedious and error-prone.

Objective:
Automate the classification of glass type using KNN algorithm.

@author: chait
"""
# Step 1 : BUSINESS UNDERSTANDING

# 1. Business Problem Statement:
# Glass production involves different chemical compositions.
# Manually classifying glass types based on composition
# is time-consuming and inconsistent.

# 2. Simplified Context of the Problem:
# Different glass types are produced using varying proportions
# of elements such as Na, Mg, Al, Si, Ca, etc.
# These compositions determine the glass type.

# 3. Problem Identification:
# - Manual classification is inefficient
# - Chemical composition varies continuously
# - Misclassification leads to quality and compliance issues

# 4. Business Objective:
# Maximize: Accuracy of glass type classification
# Minimize: Manual intervention and classification errors
# Enable: Automated, data-driven decision-making

# 5. Stakeholder Expectations:
# - Manufacturing team: consistent quality
# - Compliance team: reduced hazardous substances
# - Management: reduced cost and emissions

# 6. Constraints & Limitations:
# - Climate change regulations
# - Energy consumption constraints
# - Presence of outliers in chemical composition data

# 7. Feasibility Check:
# - Historical labeled data is available
# - KNN is suitable for multivariate numeric data

# 8. Success Criteria:
# Business Success Criteria:
# - Correct glass type identification
# - Reduced manual effort
#
# ML Success Criteria:
# - Improved classification accuracy
# - Stable performance on unseen data


# ------------------------------------------------------------
# DATA UNDERSTANDING
# ------------------------------------------------------------
"""
(Feature , Longform,type ,description)
RI    -Refractive index  - Quantitative, Continuous - Highly relevant; differentiates glass types
Na     - Sodium content - Quantitative, Continuous - Highly relevant; affects glass composition  
Mg     - Magnesium content - Quantitative, Continuous - Relevant; influences strength and clarity
Al     - Aluminum content - Quantitative, Continuous - Relevant; improves durability               
Si     - Silicon content - Quantitative, Continuous - Highly relevant; main glass-forming element 
K      - Potassium content- Quantitative, Continuous - Relevant; impacts thermal properties        
Ca     - Calcium content - Quantitative, Continuous - Highly relevant; affects stability          
Ba     - Barium content - Quantitative, Continuous - Relevant; used in specialty glasses         
Fe     - Iron content - Quantitative, Continuous - Relevant; affects color and absorption      

Type   - Glass category - Categorical (Target Variable)| Target variable for classification

'''
# Key Data Insights:
# - Multivariate numeric dataset
# - Presence of outliers
# - Features are on different scales
# - Supervised classification problem
"""


# ------------------------------------------------------------
# STEP 1: Import Required Libraries
# ------------------------------------------------------------

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

# ------------------------------------------------------------
# STEP 2: Load the Dataset
# ------------------------------------------------------------
glass = pd.read_csv("../../8-KNN/glass.csv")


# ------------------------------------------------------------
# STEP 3: Data Understanding
# ------------------------------------------------------------
glass.dtypes  # Datatype of the each feature 
glass.shape # Rows and columns in dataset
glass.columns # Names of the features
glass.describe()

# Inference:
# All input features are numeric.
# Target column "Type" is categorical encoded as integers.


# ------------------------------------------------------------
# EDA
# ------------------------------------------------------------

# Rename columns for consistency.
glass.columns = ['ri','na','mg','al','si','k','ca','ba','fe','type']

# Check data types
glass.dtypes
# Inference:
# All input features are numeric (float).
# Target column 'type' is integer.

# ------------------------------------------------------------
# Shape and Size
# ------------------------------------------------------------
print("Shape of dataset:", glass.shape)
print("Size of dataset:", glass.size)

# Inference:
# Dataset has 214 rows and 11 columns
# (1 ID, 9 numerical features, 1 target variable).
# Dataset size is moderate and suitable for EDA and KNN.

# ------------------------------------------------------------
# Summary Statistics
# ------------------------------------------------------------
glass.describe()

'''
| Element | Meaning | Business / Manufacturing Use Case |
|--------|---------|-----------------------------------|
| Min / Max | Range of chemical composition | Helps define safe and usable glass composition limits |
| Mean | Average concentration | Typical composition used in production |
| Q1–Q3 | Middle 50% spread | Indicates consistency in raw material mix |
| Median | Central tendency | Robust benchmark against extreme batches |
| IQR | Q3 - Q1 | Detects stability of production process |
'''

# ------------------------------------------------------------
#  Buisness moment decisions.
# ------------------------------------------------------------

# 1️ First Moment: Mean (Central Tendency)
mean_values = glass.mean(numeric_only=True)
print("\nMean:\n", mean_values)

# Inference:
# Mean shows the typical chemical composition.
# Useful for defining standard glass formulations.

# 2️ Second Moment: Variance & Standard Deviation (Dispersion)
var_values = glass.var(numeric_only=True)
std_values = glass.std(numeric_only=True)

print("\nVariance (Second Moment):\n", var_values)
print("\nStandard Deviation (Second Moment):\n", std_values)

# Inference:
# High variance in Na, Ca, Si indicates strong influence
# on glass type differentiation.
# Low variance features are less discriminative , meaning features are 
# more or less similar.

# 3️ Third Moment: Skewness (Symmetry)
skew_values = glass.skew(numeric_only=True)
print("\nSkewness (Third Moment):\n", skew_values)

# Inference:
# Positive skew → few samples with high concentration
# Negative skew → few samples with very low concentration
# Indicates non-normal chemical distributions.

# 4️ Fourth Moment: Kurtosis (Peakedness)
kurt_values = glass.kurtosis(numeric_only=True)
print("\nKurtosis (Fourth Moment):\n", kurt_values)

# Inference:
# Platykurtic (<0): flatter distribution → uniform composition
# Leptokurtic (>0): sharp peak → extreme compositions present

# ------------------------------------------------------------
# UNIVARIATE ANALYSIS – Histograms 
# ------------------------------------------------------------
glass.drop(columns=['type']).hist(
    figsize=(12,10),
    edgecolor='black'
)
plt.suptitle("Histograms of Glass Chemical Features")
plt.tight_layout()
plt.show()

# Inference:
# - RI and Na are near normally distributed
# - Mg and K show skewness
# - Si has tight concentration range
# - Chemical composition differs across glass types

# ------------------------------------------------------------
# BOXPLOTS – OUTLIER DETECTION
# ------------------------------------------------------------
plt.figure(figsize=(12,6))
sns.boxplot(data=glass.drop(columns=['type']), orient='h')
plt.title("Boxplot of Glass Chemical Features")
plt.show()

# Inference:
# Outliers observed in Na, al, Ca,ba and k
# These may represent special-purpose or industrial glass types

# ------------------------------------------------------------
# CORRELATION HEATMAP
# ------------------------------------------------------------
plt.figure(figsize=(8,8))
sns.heatmap(
    glass.drop(columns=['type']).corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap – Glass Dataset")
plt.show()

'''
RI (Refractive Index): Strongly increases with Ca and decreases with Si, indicating calcium-rich glass has higher refractive index.
Na (Sodium): Shows weak to moderate correlations, slightly positive with Ba and negative with Mg and Ca.
Mg (Magnesium): Negatively correlated with Al, Ca, and Ba, suggesting magnesium content reduces these components.
Al (Aluminium): Moderately positively related to Ba and K, but negatively related to Mg and RI.
Si (Silicon): Strongly negatively correlated with RI, implying silica-rich glass lowers refractive index.
K (Potassium): Mild positive correlation with Al and weak negative correlation with Ca, showing limited influence overall.
Ca (Calcium): Strongly positively correlated with RI and negatively with Mg and K, highlighting its key role in glass properties.
Ba (Barium): Moderately positively correlated with Al and Na, but negatively with Mg.
Fe (Iron): Very weak correlations with all features, indicating minimal interaction with other elements.
'''
# ------------------------------------------------------------
# PDF & CDF ANALYSIS
# ------------------------------------------------------------
num_cols = glass.select_dtypes(include=np.number).columns.drop(['type'])

for col in num_cols:
    plt.figure(figsize=(12,5))

    # PDF
    plt.subplot(1,2,1)
    sns.kdeplot(glass[col], fill=True)
    plt.title(f"PDF of {col}")

    # CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(glass[col])
    y_vals = np.arange(len(sorted_vals)) / float(len(sorted_vals))
    plt.plot(sorted_vals, y_vals, marker='.', linestyle='none')
    plt.title(f"CDF of {col}")

    plt.tight_layout()
    plt.show()

# Inference:
'''
The PDF of RI shows that most values lie in the range ≈ 1.515 to 1.520,
 with a clear peak around 1.517–1.518, while the CDF indicates that 
 about 50% of the samples have RI ≤ 1.518.

The PDF of Na shows most values concentrated in the range ≈ 12.5 to 14.5, 
with a peak around 13–13.5, while the CDF indicates 
that about 50% of the observations lie below Na ≈ 13.5.
    

'''
# PDF → shows distribution shape of each chemical
# CDF → helps decide percentile-based thresholds
# Useful for quality control and segmentation

# ------------------------------------------------------------
# CLASS DISTRIBUTION (TARGET ANALYSIS)
# ------------------------------------------------------------
sns.countplot(x=glass['type'])
plt.title("Distribution of Glass Types")
plt.show()

# Inference:
#The dataset is imbalanced, with glass types 1 and 2 having the 
#highest number of samples, while types 3, 5, and 6 are 
#underrepresented and type 7 has a moderate presence.
# Class imbalance exists.
# Some glass types are under-represented,
# which may affect KNN performance.

# ------------------------------------------------------------
# FINAL EDA INSIGHTS
# ------------------------------------------------------------
# - Dataset is multivariate and numeric
# - Outliers are present → need treatment
# - Features are on different scales → normalization required
# - Chemical composition strongly influences glass type

# ------------------------------------------------------------
# STEP 6: DATA PREPROCESSING 
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# STEP 2: Load the Dataset
# ------------------------------------------------------------
glass = pd.read_csv("../../8-KNN/glass.csv")

print("Initial Shape:", glass.shape)
glass.head()


# ------------------------------------------------------------
# STEP 3: BASIC DATA QUALITY CHECK
# ------------------------------------------------------------
glass.info()
print("\nMissing Values:\n", glass.isnull().sum())

# Inference:
# - Dataset has no missing values
# - All input features are numeric
# - Target column 'Type' is integer encoded




# ------------------------------------------------------------
# STEP 4: OUTLIER DETECTION (FROM EDA)
# ------------------------------------------------------------
# Based on EDA, outliers were detected in:
# RI, Na, Al, Si, K, Ca, Fe
# Mg does not have significant outliers


# ------------------------------------------------------------
# STEP 5: OUTLIER TREATMENT USING WINSORIZATION
# ------------------------------------------------------------
# Why Winsorization?
# - Prevents extreme values from distorting distance-based models
# - Preserves dataset size
# - Suitable for manufacturing datasets

def winsorize_column(df, col):
    """
    Caps extreme values using IQR method.
    Lower cap = Q1 - 1.5 * IQR
    Upper cap = Q3 + 1.5 * IQR
    """
    winsor = Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=[col]
    )
    return winsor.fit_transform(df[[col]])

# Apply winsorization
for col in ['RI','Na','Al','Si','K','Ca','Fe']:
    glass[col] = winsorize_column(glass, col)

# Mg is excluded as it has no significant outliers

print("Outlier treatment completed")


# ------------------------------------------------------------
# STEP 7: TARGET VARIABLE LABEL ENCODING
# ------------------------------------------------------------
# Convert numeric class labels into meaningful glass types

glass['Type'] = np.where(glass['Type'] == 1, 'build_win_fl', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 2, 'build_win_nfl', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 3, 'veh_win_fl', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 4, 'veh_win_nfl', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 5, 'containers', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 6, 'tableware', glass['Type'])
glass['Type'] = np.where(glass['Type'] == 7, 'headlamps', glass['Type'])

glass['Type'].value_counts()


# ------------------------------------------------------------
# STEP 8: FEATURE SCALING – MIN-MAX NORMALIZATION
# ------------------------------------------------------------
# Why scaling is mandatory?
# - KNN is distance-based
# - Chemical features are on different scales
# - Prevents dominance of large-magnitude features

X_features = glass.drop(columns=['Type'])

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_features)

X_scaled = pd.DataFrame(X_scaled, columns=X_features.columns)

X_scaled.describe()


# ------------------------------------------------------------
# STEP 9: SPLIT INPUT AND OUTPUT
# ------------------------------------------------------------
X = np.array(X_scaled)
y = np.array(glass['Type'])


# ------------------------------------------------------------
# STEP 10: TRAIN–TEST SPLIT
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)


# ------------------------------------------------------------
# FINAL PREPROCESSING SUMMARY
# ------------------------------------------------------------
# Identifier removed
#  Outliers treated using Winsorization
#  Target labels made interpretable
#  Features normalized (0–1 range)
#  Data split into train and test sets

print("Glass Dataset Preprocessing Completed Successfully")


# ------------------------------------------------------------
# STEP 10: KNN MODEL TRAINING
# ------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train, y_train)


# ------------------------------------------------------------
# STEP 11: MODEL EVALUATION
# ------------------------------------------------------------
from sklearn.metrics import accuracy_score

pred_test = knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train, y_train)


# ------------------------------------------------------------
# STEP 12: HYPERPARAMETER TUNING (K VALUE)
# ------------------------------------------------------------
acc = []

for i in range(3, 50, 2):
    knn1 = KNeighborsClassifier(n_neighbors=i)
    knn1.fit(X_train, y_train)
    acc.append([
        np.mean(knn1.predict(X_train) == y_train),
        np.mean(knn1.predict(X_test) == y_test)
    ])

plt.plot(range(3,50,2), [i[0] for i in acc], 'ro-')
plt.plot(range(3,50,2), [i[1] for i in acc], 'bo-')
plt.xlabel("K value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Tuning")
plt.show()

'''
What the Graph Shows
X-axis: K value (number of neighbors)
Y-axis: Accuracy
Red line: Training accuracy
Blue line: Testing accuracy
This plot is used to select the optimal K by balancing bias–variance tradeoff.
 Key Observations
1 Small K values (K = 3–7)
Training accuracy: Very high (~0.82)
Testing accuracy: Much lower (~0.62)
Indicates overfitting
Model is too sensitive to noise

2.Medium K values (K = 11–15) 
Training accuracy: ~0.70
Testing accuracy: Peak ~0.69–0.70
 Best generalization
 Bias–variance balance achieved
 Training and testing curves are close
 This is the OPTIMAL REGION

Best K Value (Final Answer)
Optimal K ≈ 13 to 15
Highest testing accuracy
Minimal gap between training and testing
Best real-world performance
'''

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train, y_train)

# ------------------------------------------------------------
# STEP 13: MODEL EVALUATION
# ------------------------------------------------------------
from sklearn.metrics import accuracy_score
pred_test = knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train, y_train)
#k=15
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=19)
knn.fit(X_train, y_train)

# ------------------------------------------------------------
# STEP 14: MODEL EVALUATION
# ------------------------------------------------------------
from sklearn.metrics import accuracy_score

pred_test = knn.predict(X_test)
accuracy_score(pred_test, y_test)

pred_train = knn.predict(X_train)
accuracy_score(pred_train, y_train)


# ------------------------------------------------------------
# FINAL BUSINESS INTERPRETATION
# ------------------------------------------------------------
# - KNN can classify glass types based on chemical composition
# - Proper scaling and outlier treatment are critical
# - Overfitting observed → needs careful K selection
# - Model supports automated glass classification

print("Glass Type Classification using KNN Completed")
