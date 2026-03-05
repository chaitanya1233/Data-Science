# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:15:29 2026

@author: chait
"""

###########################################################

"""
#----------------- Regression ---------------------------#
#----------------- Analysis -----------------------------#
"""
============================================================
CALORIES CONSUMED vs WEIGHT GAINED
SIMPLE LINEAR REGRESSION WITH TRANSFORMATIONS
============================================================
------------------------------------------------------------
BUSINESS UNDERSTANDING
------------------------------------------------------------
1️ Business Problem Statement:
Nutritionists and healthcare professionals want to understand
how daily calorie consumption affects weight gain.
2️ Business Objective:
- Identify the strength of relationship between calorie intake
and weight gain
- Build a predictive model for weight gain
- Improve diet planning recommendations
3️ Motivation:
Understanding calorie–weight relationship helps:
- Prevent obesity
- Design controlled diet plans
- Estimate risk of excessive weight gain
4️ Constraints:
- Human metabolism varies
- Data size may be small
- Linear assumptions may not always hold
- Outliers may affect regression
5️ Success Criteria:
Business Success:
- Accurate prediction of weight gain
- Actionable dietary insights
ML Success:
- Lower RMSE
- Strong correlation
- Stable performance on test data
------------------------------------------------------------
DATA UNDERSTANDING
------------------------------------------------------------

'''

Feature Name	Description	Type	Business Relevance
wt_gained	Weight gained (grams)	Numeric	Target variable
cal_consumed	Calories consumed per day	Numeric	Key predictor
'''			
# ============================================================
# CALORIES CONSUMED vs WEIGHT GAINED
# EXPLORATORY DATA ANALYSIS WITH INFERENCE
# ============================================================

# ------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# STEP 2: LOAD THE DATASET
# ------------------------------------------------------------
cal = pd.read_csv("c:/360DG/Datasets/calories_consumed.csv")
cal.columns = ["wt_gained", "cal_consumed"]

print("First 5 Rows:\n", cal.head())

# ------------------------------------------------------------
# STEP 3: BASIC EDA
# ------------------------------------------------------------
print("\nData Types:\n", cal.dtypes)
print("\nSummary Statistics:\n", cal.describe())


# ------------------------------------------------------------
# BUSINESS MOMENT DECISIONS
# ------------------------------------------------------------

# Mean
print("\nMean:\n", cal.mean())
'''
Inference:
• Average calorie intake represents typical daily consumption.
• Average weight gain shows normal gain pattern.
• If both means are high → population likely in calorie surplus.
• Indicates calories may be contributing to weight gain.
'''

# Variance
print("\nVariance:\n", cal.var())
'''
Inference:
 High variance in calories → different eating habits.
 High variance in weight gain → metabolic differences.
 Larger spread means predictions may vary across individuals.
'''

# Standard Deviation
print("\nStandard Deviation:\n", cal.std())
'''
Inference:
 Shows average deviation from mean.
 Lower value → stable population behavior.
 Higher value → more fluctuation in diet and weight gain.
'''

# Skewness
print("\nSkewness:\n", cal.skew())
'''
Inference:
 Skew ≈ 0 → Symmetric distribution.
 Positive skew → few individuals consume very high calories.
 Positive skew in weight  cal consumtion too → few individuals gain extreme weight.
'''

# Kurtosis
print("\nKurtosis:\n", cal.kurtosis())
'''
Inference:
 High kurtosis → presence of extreme values.
 Low kurtosis → uniform spread.
 Extreme calorie or weight values may influence regression.
'''

# Correlation
print("\nCorrelation Matrix:\n",
      np.corrcoef(cal.cal_consumed, cal.wt_gained))
'''
Inference:
 Correlation close to +1 → Strong positive relationship.
 Confirms higher calories → higher weight gain.
 Suitable for linear regression modeling.
'''


# ------------------------------------------------------------
# STEP 4: UNIVARIATE ANALYSIS
# ------------------------------------------------------------

# Histogram - Weight Gained
plt.figure(figsize=(6,4))
plt.hist(cal.wt_gained)
plt.title("Weight Gained Distribution")
plt.xlabel("Weight Gained")
plt.ylabel("Frequency")
plt.show()

'''
Inference:
Most individuals gained lower to moderate weight (clustered in the lower range).
The distribution appears positively skewed (right-skewed).
A few individuals show very high weight gain, creating a long right tail.
These extreme values may act as outliers and can influence regression results.
'''

# Histogram - Calories Consumed
plt.figure(figsize=(6,4))
plt.hist(cal.cal_consumed)
plt.title("Calories Consumed Distribution")
plt.xlabel("Calories Consumed")
plt.ylabel("Frequency")
plt.show()

'''
Inference:
Calorie intake is spread across a moderate to high range.
Most individuals consume calories within a normal daily intake band.
The distribution shows a slight right skew, indicating a few individuals consume very high calories.
Presence of high-calorie values suggests potential overconsumption cases.'''

# ------------------------------------------------------------
# BOX PLOT (OUTLIER DETECTION)
# ------------------------------------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=cal[['cal_consumed','wt_gained']], orient='h')
plt.title("Boxplot of Numerical Features")
plt.show()

'''
Inference:
Both Calories Consumed and Weight Gained show a reasonable spread.
The data points lie within the whiskers — no extreme outliers detected.
Calories consumed has a wider range compared to weight gained.
Median values appear centrally positioned, indicating stable distributions.
'''


# ------------------------------------------------------------
# BIVARIATE ANALYSIS (SCATTER PLOT)
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(x='cal_consumed', y='wt_gained', data=cal)
plt.title("Calories Consumed vs Weight Gained")
plt.xlabel("Calories Consumed")
plt.ylabel("Weight Gained")
plt.show()

'''
Inference:
Clear positive linear relationship observed.
As calories consumed increase, weight gained also increases.
Data points follow an upward trend, indicating a strong correlation.
No major irregular patterns or clustering observed.
'''


# ------------------------------------------------------------
# CORRELATION HEATMAP
# ------------------------------------------------------------
plt.figure(figsize=(5,4))
sns.heatmap(cal.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

'''
Inference:
The correlation between calories consumed and weight gained is 0.95, which indicates a very strong positive relationship.
This means as calorie intake increases, weight gain increases significantly.
The value is close to +1, showing a strong linear association.
No negative relationship observed.'''


# ------------------------------------------------------------
# PDF & CDF ANALYSIS
# ------------------------------------------------------------
for col in ['cal_consumed','wt_gained']:
    plt.figure(figsize=(12,4))

    # PDF
    plt.subplot(1,2,1)
    sns.kdeplot(cal[col], fill=True)
    plt.title(f'PDF of {col}')

    # CDF
    plt.subplot(1,2,2)
    sorted_vals = np.sort(cal[col])
    y = np.arange(len(sorted_vals))/len(sorted_vals)
    plt.plot(sorted_vals, y)
    plt.title(f'CDF of {col}')

    plt.show()

'''
Inference:
PDF (Probability Density Function) fig-1
The distribution appears slightly right-skewed.
Most individuals consume calories in the mid-range (around 1800–2800).
A few individuals consume very high calories, forming the right tail.
Indicates moderate variability in daily calorie intake.
CDF (Cumulative Distribution Function)
The curve increases steadily, showing gradual accumulation.
Around 80% of individuals consume below approximately 3000 calories.
Only a small percentage consume extremely high calories (above 3500–4000).

PDF (Probability Density Function) fig-2

The distribution is positively skewed (right-skewed).
Most individuals gained weight in the lower to moderate range.
A small number show high weight gain, forming the right tail.
Indicates that extreme weight gain cases are limited but present.
CDF (Cumulative Distribution Function)
The curve rises quickly in the lower range, meaning many individuals gained smaller amounts of weight.
Around 70–80% of individuals gained below approximately 600–700 grams.
Only a small percentage experienced very high weight gain (above 900–1000 grams).
'''
# ------------------------------------------------------------
# FINAL EDA SUMMARY
# ------------------------------------------------------------
"""
FINAL SUMMARY:

 Strong positive relationship observed between calorie intake and weight gain.
 Distribution mostly stable with few extreme cases.
 Correlation confirms calories significantly impact weight.
 Linear regression is appropriate for modeling.
 Useful for diet planning and obesity prevention strategies.
"""

#------------------------------------------------
# Data Preprocessing
#------------------------------------------------

# Step1 : Import the libaries.
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from scipy.stats import skew
from feature_engine.outliers import Winsorizer


# Step 2: Import the dataset 

cal = pd.read_csv("../../13-Regression/calories_consumed.csv")

# rename the columns 
cal.columns = ['wt_gained','cal_consumed']


print("Initial Shape:",cal.shape)
print(cal.head)


# step 3: Basic cleaning 

print("Missing values before treatment:\n",cal.isna().sum())

"""
Inference :
Dataset contains only numerical variables .
No identifier column present.
If missing values exist must be handled.
If zero -i dataset is clean.
"""

# Step 4: Missing values treatment if applicable 

# Using median imputation (Roburst to skewness)

for col in cal.columns:
    cal[col].fillna(cal[col].mean(),inplace = True)
    
print("\nMissing values After tremtment\n",cal.isna().sum())

"""
Median is used because it is roburst to extreme 
prevent distortion in regression coeficients
Suitable for the numeric regression datasets
"""

# STEP S: DUPLICATE REMOVAL if applicable
cal.drop_duplicates(inp1ace=True)
print( "\nShape After Removing Duplicates: ",cal.shape)

"""
Inference :
Removes repeated observations.
Prevents model from Learning duplicated
Improves generalization capability.
"""

# Step 6: Outlier detection 

plt.figure(figsize = (8,5))
sns.boxenplot(data = cal,orient = 'h')
plt.title("Boxplot Before Treatment")
plt.show()

"""
 - Check for extreme colories consumption 
 - check for extreme weight gain 
 - outliers can heavily influence regresssion slope 
 """
 
# Stpe 7 : Outlier treatment (Winsorization)

winsor = Winsorizer(
    capping_method='iqr',
    tail = 'both',
    fold = 1.5,
    variables=['cal_consumed','wt_gained'])

cal[['cal_consumed','wt_gained']] = winsor.fit_transform(cal[['cal_consumed','wt_gained']])


plt.figure(figsize=(8,5))
sns.boxenplot(data = cal,orient='h')
plt.title("Boxplot After Winsorzation")
plt.show()


"""
Inference :
Extreme values capped using IQR method.
Reduces impact of abnormal observations.
Improves regression stability.
Recommended for Linear regression.
"""


# Step 8 : Skewness ckeck 

print("Skewness:\n",cal.skew(numeric_only = True))

"""
Inference:
Skewness > 1 - Strong skew (Log transformation may help).
Mild skew > transformation optional.
Helps decide model transformation stage
"""

#------------------------------------
# FINAL PREPROCESSING SUMMARY
#------------------------------------

"""
FINAL DATA PREPROCESSING SUMMARY:
· Dataset validated and cleaned.
· Missing values handled using median.
· Duplicates removed.
· Outliers treated using IQR-based Winsorization.
· Skewness evaluated.
· Dataset is now ready for the regression modeling.
"""

#-------------------------------------------------
# MODEL DEVELOPMENT - SIMPLE LINEAR REGRESSION.
#-------------------------------------------------
# let us apply to various models and check the feasibility

import statsmodels. formula.api as smf
import numpy as np
import pandas as pd
import matplotlib. pyplot as plt
from sklearn.model_selection import train_test_split

#--------------------------------------
# 1 SIMPLE LINEAR REGRESSION
#--------------------------------------
model1 = smf. ols ( 'wt_gained ~ cal_consumed' , data=cal ) . fit ( )
pred1 = model1.predict(cal)
rmse1 = np.sqrt(np.mean((cal.wt_gained - pred1) ** 2))
print ( "SLR RMSE: ", rmse1)
#103.30
model1. summary()


"""
#R-squared = 0.897 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -625.75
#beta-1 = 0.4202

Goal of the Model
We are trying to predict wt_gained (Dependent Variable)
using cal_consumed (Independent Variable).
1. Model Fit (Goodness of Fit)
R-squared = 0.897(applicable for MLR)
“Adjusted R² tells us whether adding more variables truly improves the model or just artificially increases R².”
→ About 89.7% of the variation in wt_gained is explained by cal_consumed.
This means the model fits the data very well.
Adjusted R-squared = 0.888
→ Adjusted for number of predictors; still very high.
Since there is only one predictor, overfitting is not a concern.

purpose of F-statistic
Does the independent variable(s) collectively explain the dependent variable?
Or is the relationship happening just by chance?
F-statistic = 104.3
An F-value of 104.3 is very large.
This means the model explains much more variation in weight gain than random chance.
It indicates that calories consumed significantly improves prediction of weight gained.


 Model is statistically significant.
 It performs much better than a model with no predictor.
 Calories consumed significantly explains weight gain.

2. Coefficient Interpretation
Variable	Coefficient	Interpretation
Intercept	-625.75	When calories = 0, predicted weight gain is -625g (not practical, just mathematical baseline).
cal_consumed	+0.4202	For every 1 unit increase in calories, weight increases by 0.42 units.  Strong positive relationship.

P-value for cal_consumed = 0.000
 Highly statistically significant.

This confirms:
Higher calorie intake leads to higher weight gain.

3. Residual Analysis

The Durbin-Watson statistic checks whether residuals are independent.

DW Value	Meaning
≈ 2	 No autocorrelation (Ideal)
< 1.5	 Positive autocorrelation
> 2.5	 Negative autocorrelation
1.5–2.5	 Acceptable

Durbin-Watson = 2.537

 Slightly above 2 but still acceptable.
 No serious autocorrelation problem.

Normality Check

Jarque-Bera p-value = 0.541 (> 0.05)
 Residuals are approximately normally distributed.
 Regression assumption satisfied.

In One Sentence :
“Calories consumed has a strong and statistically significant impact on weight gained, and this model explains nearly 90% of the variation in weight. The regression assumptions are largely satisfied, so the model is reliable for prediction.”
"""

#--------------------------------------
# 2. LOG MODEL
#--------------------------------------

model2 = smf.ols('wt_gained ~ np.log(cal_consumed)',data = cal).fit()

pred2 =  model2.predict(cal)
rmse2 = np.sqrt(np.mean((cal.wt_gained - pred2) ** 2))
print("Log-X Model RMSE:", rmse2)
#141.005
model2.summary()

 
"""
#R-squared = 0.808 > 0.80, Model is very strong
#p = 0 < 0.05 hence acceptable
#beta-0 = -6955.6501
#beta-1 = 948.3717

Calories consumed is actually contributing to weight gained.

Higher calories intake even after log transformation leads to 
higher weight gain.

- Residual Analysis.
  . Durbin watson value : 2.488
      - value lies within range of 1.5 to 2.5 which is acceptable 
      - SO , there is no serious auto-correlation problem

- Normality check
    . Jarque Bera p - Value : 0.0566 
    . It is slightly greater than 0.05
    . Errors are normally distributed.
    . All assumptions are satisfied

- Conclusion: RMSE is higher than privious one, 
    and there is slight correlation in errors.

"""



#--------------------------------------
# 3. EXPONENTIAL MODEL
#--------------------------------------

model3 = smf.ols('np.log(wt_gained) ~ cal_consumed',data = cal).fit()
pred3 = model3.predict(cal)
rmse3 =  np.sqrt(np.mean((cal.wt_gained - pred3) ** 2))
print("Log-X Model RMSE:", rmse2)
#141.005
model3.summary()


"""
Inference :
- RMSE value : 141.005
- R-Squared : 0.878
- F Statistics : 86.04
    Summary :
    . R-squared value is greater than 0.80 , meaning model is best fit 
      model.
    . f-Statistics is higher , calories consumed contribting to weight 
      gain

- Coeficient Interpretation
    Beta-0 : what is the value of y when x = 0
    Beta-1 : What is the coeficient of the x, is it contributing to y
    p values of Beta-0 and Beta-1 should be < 0.05
    
    Inference:
        . As the p-values are lesser than the 0.05 , meaning 
        both Beta-0 and Beta-1 are really contributing to weight gain

- Residual Analysis
    
    Durbin Watson values : 3.13
    Jarque Bera p-value : 0.0469
    
    - DW value is greater than 2.5 , so there is negative Auto-correlation problem 

Summary :
    - RMSE is still lesser than the previous model.
    - Although features are contributing to the target variable,
    - Srious auto correlation problem is there and errors are not normally 
    distributed
    so model is  NOT ACCEPTABLE.

"""


#--------------------------------------
# 4. POLYNOMIAL MODEL
#--------------------------------------     

model4 = smf.ols('np.log(wt_gained) ~ cal_consumed + I(cal_consumed ** 2) ',data =  cal).fit()
pred4 = np.exp(model4.predict(cal))
rmse4 = np.sqrt(np.mean((cal.wt_gained - pred4) ** 2))
print("Polynomial Model RMSE:", rmse4)
#117.41
model4. summary()


"""
- R-squared = 0.878 
     . Values are greater than 0.80 
         meaning , about 87.8% variation is explained by polynomial
         model
- f-statistics : 39.44 , meaning features are statistically significant.
- probability of f-statistics : 9.61e-06 , lesser than 0.05 
        so , overall model is acceptable.

- Intercept : 2.8287
- cal_consumed : 0.0011

- Residual  Analysis
     DW values : 3.131 , still higher than 2.5
     meaning , Negative Auto correlation problem is there.

- Normality check
    . JB p-values : 0.04 --> Lesser than 0.05 meaning , errors are 
    normally distributed.

SUMMARY:
    - RMSE is greater than rest of the models.
    - Although errors are normally distributed and features are 
        significantly contrbuted to the target variable
    - Model is not acceptable.
"""

# model comparision  
import pandas as pd

results = pd.DataFrame({
    "Model": ["SLR", "Log-X", "Exponential", "Polynomial"],
    "RMSE": [rmse1, rmse2, rmse3, rmse4],
    "R_squared": [
        model1.rsquared,
        model2.rsquared,
        model3.rsquared,
        model4.rsquared
    ]
})

print(results)

best_model_name = results.loc[results['RMSE'].idxmin(), 'Model']
print("Best Model:", best_model_name)


"""
Inference:
    - By comapring all RMSE and R-Squared values of the dataset,
    our best model is SLR(Simple Linear Regression)
"""

#------------------------------------------------------------------------
# TRAIN-TEST VALIDATION USING BEST MODEL (SLR IS BEST HERE)
#------------------------------------------------------------------------

train, test = train_test_split(cal, test_size=0.3, random_state=42)

# Since SLR has highest R2 (0.897) and lowest RMSE, choose model1

final_model = smf . ols ( 'wt_gained ~ cal_consumed', data=train) . fit()

train_pred = final_model.predict(train)

test_pred = final_model.predict(test)

train_rmse = np.sqrt(np.mean((train.wt_gained - train_pred) ** 2))
test_rmse = np.sqrt(np.mean((test.wt_gained - test_pred) ** 2))
print("\nTrain RMSE:", train_rmse)
print("Test RMSE :", test_rmse)


"""
Inference:
    Train RMSE : 105.48 
    Test RMSE : 101.59
    Model performes significantly better on the testing data.
"""


"""
# Buisness Impact
 . It can be helpful for the peoples who wana gain weight or loose fat.
 . Dietician for their clients to track their gaining.

"""
