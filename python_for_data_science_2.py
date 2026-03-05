                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 16:07:54 2026

@author: chait
"""

###################################################################

# Read the datafram 

import pandas as pd 
index_label  = ['r0','r1','r2','r3','r4','r5','r6','r7']
technologies = {
                "Cources":["Spark","PySpark",'Hadoop','Python','Pamdas',
                           'Oracle','Java'],
                "Fees":[20000,25000,26000,22000,24000,21000,22000],
                "Duration":['30days','40days','35days','40days',
                            '60days','50days','55days'],
                "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
                }

df  = pd.DataFrame(technologies)
df.iloc[0]

#############################################
#Access fist two  rows 

df.iloc[:2]

# Access the rows and columns -> first 3 rows and 2 columns 

df.iloc[:3,:2]

# Access all the rows with columns first and second 
df.iloc[:,1:3]

# what if i want only specific rows only

df.iloc[[0,1,2]]

# Select  last row 

df.iloc[-1:]

# Select last 3rd row 
df.iloc[:-3]

#Select every alternate row ,but in a reverse order.
df.iloc[-1::-2]
################################################################

# Select the rows and columns based on their labels 

df.loc['r1']

# Most of this questions are skipped ....


########################################################

# using loc aad columnn names along with df 


df.loc[:"Duration"]  # Data with all the rows and columns upto Duration 

# What if you want to select the random column 

df.loc[:,["Cources","Discount"]]

################################################################









