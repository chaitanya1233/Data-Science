# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:03:46 2026

@author: chait
"""

################################################################
# --------------------------------------------------------
# Buisness Understanding and Data Understanding
# --------------------------------------------------------

# --------------------------------------------------------
# Exploratory Data Analysis
# --------------------------------------------------------


#---------------------------------------------------------
# Data Preprocessing
#---------------------------------------------------------

# step 1: Import the libraries 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from feature_engine.outliers import Winsorizer

# Step 2: Import the dataset 
cars = pd.read_csv("../../13-Regression/Cars.csv") # reading the csv
print("Initial Shape:",cars.shape)
print(cars.head())


# Step 3: Basic Cleaning 
print("\nData Types: \n", cars. dtypes)
print("\nMissing Values Before Treatment: \n", cars.isnull().sum())

"""
Inference:
Dataset contains only numerical variables.
No categorical encoding required.
If missing values exist > must be handled.
MPG is target variable.
"""

# Step 4: Missing calues treatment 
for col in cars.columns:
    cars[col].fillna(cars[col].median(),inplace = True)

print("\nMissing values after treatment:\n",cars.isna().sum())

"""
Inference:
Median imputation is used, beacause: 
    - Roburst to outliers
    - Suitable for skewed numeric data
    - prevent distortion of the regression models 
"""

# Step 5: Duplicare removal 
cars.drop_duplicates(inplace = True)
print("Shape after removing duplicates:",cars.shape)


"""
Inference:
    Remove repeted vehical records 
    prevent model bais
    Imporves Genralization capacity.
"""

# Step 6 : Outlier Detection 
plt.figure(figsize=(10,6))
sns.boxplot(data = cars,orient = 'h')
plt.title("Boxplot before Treatment")
plt.show()

"""
Inference:
    HP and SP shows extreme outliers 
    VOL and WT may show strong correlation 
    outliers can distort regreesion coeficients
"""

# Step 7: Outlier treatment (Winsorization)
winsor = Winsorizer(
        capping_method='iqr',
        tail='both',
        fold=1.5,
        variables=list(cars.columns)
)
cars = winsor. fit_transform(cars)

plt. figure(figsize=(8,5))
sns. boxplot(data=cars, orient='h')
plt. title( "Boxplot After Winsorization")
plt. show()  

"""

Inference:
Extreme values capped using IQR method.
Reduces impact of abnormal vehicles.
Improves regression stability.
Recommended before fitting Linear models.
"""

# STEP 8: SKEWNESS CHECK
print("\nSkewness: \n", cars. skew())

"""
Inference:
· Skewness > 1 > Strong skew (Log transformation may help).
· Mild skew > acceptable for regression.
· Helps decide transformation strategy

Slightly above 1
Moderate right skew
Winsorization already reduced extreme values
SP = 0.74
Transformation optional (Log can help, but not mandatory)
Mild skew
No strong need for transformation
VOL, WT
Mild Left skew
Not serious
No transformation required
MPG (Target)
Almost symmetric
No treatment required

Final Conclusion
After winsorization:
Skewness is moderate, not severe
No compulsory Left/right transformation required
Linear regression is robust to mild skewness
Only transform if:
Residuals violate normality badly
Model fit is poo
"""

# Step 9: Train-Test Split

y = cars['MPG']
x = cars.drop(columns=['MPG'])

x_train , x_test, y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("Training data size:",x_train.shape)
print("Testing data shape:",x_test.shape)


"""
Inference:
80% data used for training.
20% data used for testing.
Ensures model generalization.
Why Standardization Is NOT Required in OLS
Linear Regression formula:
Y=BO+B1X1+B2.X2+. ..
OLS estimates coefficients using least squares.
It does NOT depend on:
Distance calculation
Gradient scaling sensitivity (like neural networks)
So model works fine without scaling.
"""

# --------------------------------------------------------
# Model Selection  (Selecting a Best Fit Model)
# --------------------------------------------------------

# STEP 10: BUILD MULTIPLE LINEAR REGRESSION MODEL

import statsmodels. formula.api as smf
import statsmodels.api as sm

# Combine training data into one dataframe for formula API

cars_train = pd.concat([x_train, y_train], axis=1)
cars_test = pd.concat([x_test, y_test], axis=1)

# Initial Model with all predictors
ml1 = smf . ols ('MPG ~ HP + VOL + SP + WT', data=cars_train) .fit()
print(ml1. summary())

"""
Inference:

1. Model Strength
    R-Squared : 0.831
    Model explains 83.1% variation in MPG 
    This is a best fit model 
    Indicates predictors collectively explains fule capacity well.
    
    Adjusted R-Squared = 0.82 
    Very close to R-Squared 
    Means no unnecessory variables inflating model
    
    Model is stable 

2 Overall Model Significance

F-statistic = 72.55
Prob(F-statistic) = 4.23e-22 (< 0.05)
Does the independent variable(s) collectively explain the dependent variable?
Or is the relationship happening just by chance?
Model is statistically significant.
At Least one predictor significantly affects MPG.

3 Coefficient Interpretation

Variable  Coefficient p-value  HP (Horsepower)   Interpretation
  
   . HP       -0.235           0.000              Significant
   . VOL      -0.513            0.230             Not significant
   . SP       0.463             0.07               Significant
   . WT       0.984             0.536             Not significant
 

Highly significant (p < 0.05)
Negative coefficient
Higher horsepower > Lower MPG
Logical: Powerful cars consume more fuel


SP (Speed)
Significant (p = 0.007)
Positive relationship
Higher speed capability slightly improves MPG
Could indicate aerodynamic efficiency.

VOL (Engine Volume)
Not statistically significant
Likely affected by multicollinearity

WT (Weight)
Not significant
Probably highly correlated with VOL
Should consider removing


4 Residual Diagnostics

Durbin-Watson Test (Independence of Errors)
The Durbin-Watson statistic checks whether residuals ang independent.

DW Value       Meaning

= 2         No autocorrelation (Ideal)
< 1.5      Positive autocorrelation
> 2.5       Negative autocorrelation
1.5 - 2.5    Acceptable


Durbin-Watson = 1.721
Value is close to 2.
Lies within acceptable range (1.5-2.5).
No serious autocorrelation problem.
Residuals are reasonably independent

Normality Check : Jarque-Bera p-value

Residuals are approximately normally distributed.
Regression assumption satisfied.
Jarque-Bera p-value = 0.677 (> 0.05)
5 Multicollinearity Warning

Condition Number = 6530 (Very High )
Indicates:
Strong multicollinearity present.
VOL & WT Likely highly correlated.
Coefficients may be unstable

"""


# Multi colinearity check 

# Calculating VIF manually
rsq_hp = smf. ols('HP ~ VOL + SP + WT', data=cars_train).fit().rsquared
vif_hp = 1/(1-rsq_hp)

rsq_vol = smf. ols('VOL ~ HP + SP + WT', data=cars_train).fit().rsquared
vif_vol = 1/(1-rsq_vol)

rsq_sp = smf . ols ('SP ~ HP + VOL + WT', data=cars_train).fit().rsquared
vif_sp = 1/(1-rsq_sp)

rsq_wt = smf. ols('WT ~ HP + VOL + SP', data=cars_train). fit().rsquared
vif_wt = 1/(1-rsq_wt)

vif_frame = pd. DataFrame({
    'Variable' : [ 'HP', 'VOL', 'SP', 'WT'],
    'VIF' : [vif_hp, vif_vol, vif_sp, vif_wt]

})

print("\nVIF Values: \n", vif_frame)

# --------------------------------------------------
# VIF INTERPRETATION & COLUMN REMOVAL DECISION
# --------------------------------------------------

"""

Variance Inflation Factor (VIF) Interpretation:
Rule of Thumb:     meaning 

VIF = 1        No multicollinearity
VIF 1-5        Moderate (Acceptable) 
VIF > 5        High correlation concern         
VIF > 10   Severe multicollinearity (Problematic)


From the VIF results:
1.VOL and WT show very high VIF values.
    . Indicates strong multicollinearity.
    . Keeping both will make coefficients unstable.
    . These two variables are highly correlated with each other.

2.HP and SP may also show moderately high VIF
    . Indicates performance related variables are correlated


Column Omission Decision

1 Identify the variable with highest VIF.
2 Remove the variable with:
    .  Highest VIF
    . Higher p-value
    . Lower business relevance

In this case:
WT can be removed because:
    - It has very high VIF.
    - It is highly correlated with VOL.
    - It may also be statistically insignificant.

After removing WT:
    · Recalculate VIF.
    . Refit the regression model.
    . Check if remaining variables have VIE / 10


Final Goal:
Reduce multicollinearity to improve:
Coefficient stability
Model interpretability
Statistical significance reliability
"""

# --------------------------------------------------------
#  Modeling 
# --------------------------------------------------------


final_ml = smf . ols ('MPG ~ HP + VOL + SP', data=cars_train) . fit()
print(final_ml.summary())

"""

# -----------------------------------------------
# OLS REGRESSION RESULTS - INTERPRETATION
# -----------------------------------------------

1 Model Strength
    R-squared = 0.830
    Model explains 83.0% of variation in MPG.
    This is a strong model fit.
    Indicates predictors collectively explain fuel efficiency well.
    
    Adjusted R-squared = 0.821
    Very close to R2.
    No unnecessary variables inflating the model
    Model is stable and reliable 


2 Overall Model Significance

F-statistic = 97.60
Prob(F-statistic) = 4.75e-23 (< 0.05)

Does the independent variable(s) collectively explain the dependent variable?
Or is the relationship happening just by chance?

Model is statistically significant.
predictors now significantly affects MPG.


3 Coefficient Interpretation

Variable  Coefficient p-value    Interpretation
  
   . HP       0.000                 Significant
   . VOL      0.000                 significant
   . SP       0.124                 likely Significant
   

HP (Horsepower)
Coefficient = - 0.234
p-value = 0.000 (Highly significant)
Higher horsepower > Lower MPG.
Powerful engines consume more fuel

VOL (Engine Volume)
Coefficient = - 0.195
p-value = 0.000 (Highly significant)
Higher engine volume > Lower MPG
Bigger engines reduce fuel efficiency.

SP (Speed)
Coefficient = 0.468
p-value = 0.006 (Significant)
Higher speed capability slightly increases MPG.
May indicate better aerodynamic efficiency.

Intercept
Not statistically significant (p = 0.124).
Intercept significance is generally not critical.

4 Residual Diagnostics
The Durbin-Watson statistic checks whether residuals are independent.


DW Value          Meaning

= 2         No autocorrelation (Ideal)
< 1.5        Positive autocorrelation
> 2.5          Negative autocorrelation
1.5-2.5        Acceptable

Durbin-Watson = 1.714
Value is close to 2.
Lies within acceptable range.
No serious autocorrelation problem.
Residuals are reasonably independent.


Normality Check:
Jarque-Bera p-value = 0.625 (> 0.05)
Residuals are approximately normally distributed

5 Multicollinearity Warning
Condition Number = 6.44e+03 (Very High)

Indicates possible multicollinearity.
Predictors may be correlated.
Coefficients may be sensitive to small data changes.
Interpretation should be done carefully.
"""
#-----------------------------------------------------
# Assumptions checking
# ----------------------------------------------------
# PREDICTIONS 
train_pred = final_ml.predict(cars_train)
test_pred = final_ml.predict(cars_test)

# Residuals.
residuals = final_ml.resid

# -----------------------
# --- QQ Plot --
# ---------------------
sm.qqplot(residuals)
plt.title("QQ Plot - Residuals")
plt.show()

"""
Interpretation:
    Residuals are approximately normally distributed.
    Minor tail deviations indicate presence of a few mild outliers.
    No severe skewness or heavy-tailed behavior observed.
Conclusion:
    Normality assumption of Linear regression is satisfied.
    Model residuals behave well.

The regression model is statistically reliable from a normality perspective.
"""


# ---Residual vs Fitted

sns. residplot(x=train_pred, y=y_train, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted")
plt.show()


"""
Interpretation:
     Linearity assumption is mostly satisfied.
     No severe heteroscedasticity detected
     Minor curvature suggests slight model misspecification.
     Some outliers may influence the model
"""

#=====================================
# STEP 14: MODEL EVALUATION (RMSE)
#======================================

train_rmse = np.sqrt(np.mean((train_pred - y_train) ** 2))
test_rmse = np. sqrt(np.mean((test_pred - y_test) ** 2))

print("Train RMSE: ", round(train_rmse,4))
print("Test RMSE :", round(test_rmse, 4))

"""
Interpretation Guide:
    
Train RMSE ‹ Test RMSE -> Normal case
Train RMSE = Test RMSE -> Ideal
Train RMSE >> Test RMSE -> Underfitting 
Train RMSE << Test RMSE -> Overfitting 
"""

# --------------------------------------------------------
# Final Model Summary 
# --------------------------------------------------------


"""
FINAL MODEL SUMMARY:

    · Data preprocessed successfully.
    . Multicollinearity checked using VIF.
    . High VIF variable removed.
    · Model assumptions verified.
    · Model evaluated using Train/Test RMSE.

    Model is ready for the Buisness Interpretation
"""
 