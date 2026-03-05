# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 15:11:50 2026

@author: chait
"""

##################################################################

# DataFrame 


import pandas as pd 
index_label  = ['r0','r1','r2','r3','r4','r5','r6']
technologies = {
                "Cources":["Spark","PySpark",'Hadoop','Python','Pamdas',
                           'Oracle','Java'],
                "Fees":[20000,25000,26000,22000,24000,21000,22000],
                "Duration":['30days','40days','35days','40days',
                            '60days','50days','55days'],
                "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
                }

df  = pd.DataFrame(technologies,index = index_label)
df

#######################################################


df.query("Cources != 'Spark'")

###############################################################

technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }

df = pd.DataFrame(technlogies)
df
################################################

# Wrong code is there ........
# Pandas add a column to dataframe 
tutors = ["Ram","Shyam","GhanShyam","Ganesh","Ramesh"]


df2 = df.assign(TutorsColumn = tutors)
df2

df.columns

##############################################

############

technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }

df = pd.DataFrame(technlogies)
df
MNCCompanies = ['Tata',"HCL","Infosys","Google","Amazon"]
df2 = df.assign(MNC = MNCCompanies,tutors = tutors)
df2

#########################################

# Derive a new column from existing column 


technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
df = pd.DataFrame(technlogies)
df2 = df.assign(Discount_percent = lambda x:x.Fee * x.Discount*100)
print(df2)


##############################################


# Another way of appending a column to the existing dataframe 

technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
MNCCompanies = ['Tata',"HCL","Infosys","Google","Amazon"]
df['MNC'] = MNCCompanies
df['MNC']

#################################################

#  Insert the column specific index.

technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
df = pd.DataFrame(technlogies)
MNCCompanies = ['Tata',"HCL","Infosys","Google","Amazon"]
df.insert(0,'MNC',MNCCompanies)
df

##############################################

# IF you want to count the number of rows.

technlogies = {
    "Courses":["spark",'pyspark','hadoop','python','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
df = pd.DataFrame(technlogies)
row_count = len(df.index)
print(f"The rows count is {row_count}")
###################################################

# FInd the number of the rows and columns 
# Number of rows --> df.shape[0]
row_count = df.shape[0]
row_count

# NUmber of columns --> df.shape[1]

col_count = df.shape[1]
col_count

######################################################

"""Pandas apply functions on the dataframe"""

import numpy as np 
import pandas as pd 


data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]}

df = pd.DataFrame(data)
df

# Create a finctoon to add a number to the dataFrame 

# Add the 3 to each value in the dataframe 
def add_3(x):
    return x+3

df2 = df.apply(add_3)
df2

##########

# Apply the same for the for single column 

# Add the 3 to column B 

df2 = (df.B).apply(add_3)

df2


#####################################


# Instade of adding the 3 add 4 to column B 

def add_4(x):
    return x+4
df2 = (df.B).apply(add_4)
df2

################################################

# Apply the same functionalitty to the multiple columns 

# Instade of passing a column as a string , pass it as a list of 
# columns

# EX : Add the 4 to column A and B 

# DataFrame creationn
import numpy as np 
import pandas as pd 


data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]}

df = pd.DataFrame(data)
df

# Define a function 

def add_4(x):
    return x+4

df2 = (df[['A','B']]).apply(add_4)

df2

################################################


# Apply the function to each column 

import numpy as np 
import pandas as pd 


data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]}

df = pd.DataFrame(data)
df

# Add 2 to each column
df2 = df.apply(lambda x:x+2)
df2

# APpply lam=mbda function to t=he single column 

df["A"] = df["A"].apply(lambda x :x-3)
df["A"]
###################################################

"""transform function 
"""

import numpy as np 
import pandas as pd 


data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]}

df = pd.DataFrame(data)



def add_2(x):
    return x + 2

df2 = df.transform(add_2)  # Transform and apply are the same

print(df2)

####################################

# Map functions  

df2 = df.map(lambda x : x-2)
df2


################################

df['A'] = df["A"].apply(np.square)
df['A']

##################

# Using the numpy.square()
# Using the numpy.squatre() with []
import numpy as np 
import pandas as pd 


data = {"A":[1,2,3],
        "B":[4,5,6],
        "C":[7,8,9]}

df = pd.DataFrame(data)

df["A"] = np.square(df['A'])
df['A']

##############################

# Pandas.groupby()
import pandas as pd

technlogies = {
    "Courses":["spark",'pyspark','hadoop','hadoop','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
df = pd.DataFrame(technlogies)

# Use groupby to compute the sum 

df2 = df.groupby(['Courses']).sum()
df2

###############################

# Groupby to the multiple columns 

df2 = df.groupby(["Courses","Discount"]).sum()

df2

#############################################

# Reset the index of the dataframe after groupby() operation.

df2 = df.groupby(["Courses"]).sum().reset_index()
df2

##########################################################


import pandas as pd

technlogies = {
    "Courses":["spark",'pyspark','hadoop','hadoop','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }
df = pd.DataFrame(technlogies)


df1 = df.sample(frac=1)

print(df1)

df1 = df.sample(frac=0.5)
df1

# Create a a new index strating form zero 

df1 = df.sample(frac=1).reset_index()
df1

# He tu --> Online bgh : Me nahe kela.
##########################################################
# Joins in Pandas 

###########################################################
# Inner joins 
###########################################################
# Left joins 
##########################################################
# Right table 
###########################################################





