# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 21:26:59 2026

@author: chait
"""

#################################################################

# Create a DataFrame using a nested list 

import pandas as pd
technologies  =[["spark",20000,"30days"],
                ["Pandas",20000,"30days"]
                ]

df = pd.DataFrame(technologies)
print(df)

##############################################

# Adding a label to the DataFrame --> rows and columns 

# rows

rows_names = ['r1','r2']

df = pd.DataFrame(technologies,index = rows_names)
print(df)

# columns 

column_names = ['Tool','Fees','Duration']

df =  pd.DataFrame(technologies,columns = column_names)
print(df)

###############################################################

# Best way to create a DataFrame is through Dictonary.

technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          }) 

df = pd.DataFrame(technologies) 
print(df)


#############################################################

# Check the datatype of the DataFrame columns

df.dtypes

###########################################################

# Convert all the datatypes to the same types 

df = df.astype(str)
print(df)
print(df.dtypes)

#######################################################

# Changing the datatype of the perticular colunmn 

import pandas as pd 

technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })

df = pd.DataFrame(technologies)

# Current datatype of objects 

df.dtypes

# Convert the fees into string and discount into float 

df['Fee'] = df['Fee'].astype(object)
df['Discount'] = df['Discount'].astype(float)

print(df['Fee'].dtypes)
print(df['Discount'].dtypes)

###############################################################

# What if you are changing the datatype of column , which cannot 
# be depricated to lower power  
 # ---> Use property named : errors = 'ignore'/ errors = 'raise'

import pandas as pd 

technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
df = pd.DataFrame(technologies)

# Changing datatype without using safe 
df['Duration'] = df['Duration'].astype(int,errors = 'ignore')

# without safe ==> errors = 'raise'

try:
    df['Duration'] = df['Duration'].astype(int,errors = 'raise')
except:
    print("Error has occured....")

#############################################################################

# Change the dicount column datatype to float

df['Discount'] = df['Discount'].astype(float)
print(df['Discount'].dtypes)

###############################################################

# Converting a dataframe to  csv 

import pandas as pd 

technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })

df =  pd.DataFrame(technologies)    

df.to_csv()

################################################################

# Reading a csv file data 

path = "C:/3-Python for Data Science/data.csv"

data = pd.read_csv(path)
print(data)
###############################################################

import pandas as pd 
import numpy as np

technologies   = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          }


df =  pd.DataFrame(technologies)


# Assigning the row labels to the rows 

rows_names = ['r1','r2','r3','r4','r5','r6','r7','r8']

df = pd.DataFrame(technologies,rows_names)

df

###############################################################

# Attributes of the DataFrame.

import pandas as pd 

technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })

df = pd.DataFrame(technologies,rows_names)
print(df)
# Attributes of the dataframe.

# How many rows and columns are there.
rows , columns = df.shape
print(f"Rows:{rows}\nColumns:{columns}")

# Size of the dataframe
df.size  # Size =  number of cells (rows*columns)

# Access the names of all the columns 

columns = df.columns    
print(columns)
print(type(columns))

# Access the values of the columns 

col_values = df.columns.values
col_values
columns
print(type(columns))
print(type(col_values))

for i in range(len(col_values)):
    print(df[col_values[i]])
    print("_----------------------")
    
# df.info vs df.info()

df.info

df.info()

df.index

df.dtypes
###############################################################
import pandas as pd
technologies  =[["spark",20000,"30days"],
                ["Pandas",20000,"30days"]
                ]

df =  pd.DataFrame(technologies)
print(df)

# Adding rows and column lables 


column_names = ["Cources",'Fee','Duration']
row_names = ['a','b']


df = pd.DataFrame(technologies,columns=column_names,index=row_names)
print(df)

##################################

df.dtypes()# error 
df.dtypes

#########################

import pandas as pd
technologies = {
                "Cources":["Spark","PySpark",'Hadoop','Python','Pamdas',
                           'Oracle','Java'],
                "Fees":[20000,25000,26000,22000,24000,21000,22000],
                "Duration":['30days','40days','35days','40days',
                            '60days','50days','55days'],
                "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
                }

df = pd.DataFrame(technologies)
df.dtypes

##############################
# Convert the all the data types to object 

df1 = df.astype(str)
df1.dtypes

############################################

# Access the column 

df3  = df['Discount'].astype(int)
df3.dtypes

#########################

cols  = ['Discount','Fees']

df4 = df[cols].astype(int)
df4.dtypes

##################################

