# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 15:15:50 2026

@author: chait
"""

##################################################################

# Create using constructor
# Create a pandas data Frame using lists.
import pandas as pd
technologies  =[["spark",20000,"30days"],
                ["Pandas",20000,"30days"]
                ]

df =  pd.DataFrame(technologies)
print(df)

#####################################


# Adding a label  to the dataframe --> rows and columns names 

column_names = ["Cources",'Fee','Duration']
row_names = ['a','b']


df = pd.DataFrame(technologies,columns=column_names,index=row_names)
print(df)

#################################################
# Check the data type of the columns
print(df.dtypes)

####################################

# Bestest way to create a dataframe is : with Dictonaries 
import pandas as pd
technologies = {
                "Cources":["Spark","PySpark",'Hadoop','Python','Pamdas',
                           'Oracle','Java'],
                "Fees":[20000,25000,26000,22000,24000,21000,22000],
                "Duration":['30days','40days','35days','40days',
                            '60days','50days','55days'],
                "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
                }

df =  pd.DataFrame(technologies)
print(df.dtypes)    

#####################################################

df2 = df.convert_dtypes()
#################################################

# Convert all columns to same types 

df =  df.astype(str)
print(df.dtypes)

################################################################
 
df.astype(str)
print(df.dtypes)


# Now again if you want to change the datatype of perticuler columns

import pandas as pd
technologies = {
                "Cources":["Spark","PySpark",'Hadoop','Python','Pamdas',
                           'Oracle','Java'],
                "Fees":[20000,25000,26000,22000,24000,21000,22000],
                "Duration":['30days','40days','35days','40days',
                            '60days','50days','55days'],
                "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
                }

df =  pd.DataFrame(technologies)
print(df.dtypes)
cols = ['Fees','Discount']
df[cols].astype(str)
print(df.dtypes)

#########################################################

df = df.astype({"Cources":int},errors='ignore')
print(df.dtypes)

df = df.astype({"Cources":int},errors='raise')

######################################################

# Change the dicount column datatype to float

df['Discount'] = df["Discount"].astype(float)
df['Discount']

########################################################

# Create a daatframe from dictonary 

technlogies = {
    "Courses":["spark",'hadoop','hadoop'],
    'Fee':[20000,25000,26000],
    "Duration":['30days','40days','35days'],
    "Discount":[11.8,23.7,13.4]
    }

df = pd.DataFrame(technlogies)
df


# Converting the DataFrame to CSV

df.to_csv('data.csv')

######################################################
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })

row_labels = ['r1','r1','r2']
df = pd.DataFrame(technlogies,index = row_labels)
print(df)


########################################################

# How many rows and how many columns are there in dataFrame 

df.shape

df.size

df.columns

df.columns.values

df.info

df.info()

df.index

df.dtypes
#############################################################

# Accessing one column 

df['Fee']

# Accessing the more than one columns 

df[['Fee','Discount']]

# Selecting a rows based on indexs 

df[:]
df[1:3]
df[2:3]

##########################################################

# Accessing certain cell 

df['Fee'][2] # It is depricated version 

# Instade you can use --> iloc[]

df.iloc[0]

########################################################

# Renaming the columns

# Remained to write the logic for that.


###############################################################

# Drop rows by labels 


rows = ["r0",'r1','r2']
df = pd.DataFrame(technlogies,index=rows)

df

# Now drop the rows by labels => r1

df1 = df.drop('r0')
df1


# delete the rows by position/index 

df2 = df.drop(df.index[1])
df2

# Delete the rows by index range 

df2 = df.drop(df.index[:2])
df2

# When you have default indexes for the rows 

df = pd.DataFrame(technlogies)

df1 = df.drop(0)
df1

# Drop two or more indexes 

df = pd.DataFrame(technlogies)
df1 = df.drop(df.index[0,2])
df1


# Drop the rows in range 
df = pd.DataFrame(technlogies)
df1 = df.drop(range(0,2))
df1


###############################################################

technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })

df = pd.DataFrame(technlogies)

################################################################



