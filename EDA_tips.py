# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 13:48:00 2026

@author: chait
"""

##################################################################

import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset("tips")

tips


sns.heatmap(tips.corr(numeric_only = True),annot = True)

"""
# Interpretation :
  1. Correlation between the features.
  - correlation values ranges from -1 to 1 .
  - Strong positive correlation 
  - moderate correlation
  - weaker correlation 
  
"""


# Box plot 

sns.boxplot(tips.tip)

#########################################################################
# countplot() -- > ex . these many coustomers coming on Sunday ,
               # --> ex . Most of customers are Males 
               
               
sns.countplot(x = tips.day)
# Interpratation:
    # -> saturday , customers are more , and on Friday --> cusomers are less.
sns.countplot(x = tips.sex)

# Interpretation : Most of customers are Males 

###############################################################

tips.sex.value_counts().plot(kind = 'pie',autopct = "51.1f%%")

sns.countplot(data = tips[tips.time == 'Dinner'],x = 'day')
# Dinner is most polular on saturday and sunday 

sns.countplot(data = tips[tips.time == 'Lunch'],x = 'day')
# On thrsday , Lunch were done most by customers.

############################################################
fg = sns.FacetGrid(tips, row = 'smoker',col = 'time')
fg.map(sns.histplot,'total_bill')

# Interpretation :  

    # 1. Those Non-smoker audiance is greater than the smakers 
    # There should be the coner room for the smokers.


################################################################

# Histogram of total_bill 

plt.hist(tips['total_bill'],bins = 20 , edgecolor = 'black')
plt.title("Total Bill Distribution.")
plt.xlabel("Total_bill")
plt.ylabel("Count")
plt.show()


################################################################
from scipy.stats import gaussian_kde
import numpy as np
data = tips['total_bill']

density = gaussian_kde(data)
x = np.linspace(min(data),max(data),200)
y = density(x)

plt.hist(data,bins = 20,density=True,alpha=0.6,edgecolor = 'black')
plt.title("Total bill distribution with density curve.")
plt.xlabel("Total bill")
plt.ylabel("Density")
plt.show()

##########################################################

plt.hist(tips['tip'],bins = 20,edgecolor = 'black')
plt.title("Tip Distribution")
plt.xlabel("Tip")
plt.ylabel("Count")
plt.show()

##################################

plt.scatter(tips['tip'],tips['total_bill'],alpha = 0.6)
plt.xlabel("Tip")
plt.ylabel("Total bill")
plt.show()

##################################################################$#

corr = tips.corr(numeric_only = True)

plt.imshow(corr,interpolation='none')
plt.colorbar()

plt.xticks(range(len(corr)),corr.columns,rotation = 45)
plt.yticks(range(len(Corr)),corr.columns)
plt.title("Correlation matrix")
plt.show()


# Box plots 

plt.boxplot(tips['total_bill'])
plt.title("Box Plot - Total Bill")
plt.show()

##################

plt.boxplot(tips['tip'])
plt.title("Box Plot -tip")
plt.show()

###############################################################


# Bar and Pie chart 

tips['day'].value_counts().plot(kind = 'bar')
plt.title("Count by Day")
plt.show()


tips['sex'].value_counts().plot(kind = 'bar')
plt.title("Count by Gender")
plt.show()


tips['day'].value_counts().plot(kind = 'pie',autopct = "%1.1f%%")
plt.title("Gender Distribution")
plt.show()

################################################################

# Homework :
    
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
import pandas as pd 

# Load the titanic dataset (Passenger survival and safety data)

titanic = sns.load_dataset("titanic")

titanic

######################################################################









































