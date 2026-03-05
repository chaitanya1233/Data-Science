# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 19:40:26 2026

@author: Chait
"""

#step 1 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.cluster.hierarchy import linkage,dendrogram
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
    )

#Step 2 = load the dataset 
Univ1=pd.read_excel(path)

print(Univ1.head())


#Step 3 - Basic eda : structure check
print("\nData Types:\n",Univ1.dtypes)
shape ,size

# Step4 - Summary stats
a=Univ.describe()
print("\nSummary Statistics:\n",a)

#Business moment decisions
#First moment 



#Step 7: Data Preprocessing
Univ=Univ.drop(["State"],axis=1)

univ_names=Univ.iloc[:,0]

univ_num = Univ.iloc[:,1:]

#Step 8 : Normalization

def norm_func(i):
    return(i-i.min())/(i.max()-i.min())

df_norm=norm_func(univ_name)

print("\nNormalized Data Summary:\n",df_norm.describe())


#Step 9 : Dendrogram (Cluster Tendency)

z=linkage(
    df_norm,
    method="complete",
    metric="euclidean"
    )

plt.figure(figsize(15,8))\
plt.title("Hierarchical Clusteriing endrogram")
