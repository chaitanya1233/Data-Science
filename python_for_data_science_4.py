9# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:07:00 2026

@author: chait
"""

###################################################################

# Merging the daataframe 

import pandas as pd

students = {
    "student_id": [101, 102, 103, 104],
    "name": ["Amit", "Neha", "Ravi", "Priya"],
    "department": ["CS", "IT", "CS", "ECE"]
}

df1 = pd.DataFrame(students)
df1
marks = {
    "student_id": [101, 102, 104, 105],
    "subject": ["Maths", "Maths", "Maths", "Maths"],
    "marks": [85, 90, 78, 88]
}

df2 = pd.DataFrame(marks)



df3 = df1.merge(df2)

df3.columns
# Apply the joins on follwing....
##################################

# Concatination 

data = [df1,df2]

df3 = pd.concat(data)
df3

# It will add the two dataframes vertically.

# You can concat multiple dataframes using pd.conact()

technlogies = {
    "Courses":["spark",'pyspark','hadoop','hadoop','pandas'],
    'Fee':[20000,25000,23000,24000,26000],
    "Discount":[0.1,0.2,0,0.5,0.1]
    }

df3 = pd.DataFrame(technlogies)

df4  = pd.concat([df1,df2,df3])
df4

##################################################

import numpy as np

# Create an array.

arr  = np.array([10,20,30])
arr

# Create a nultidimentional array.

arr = np.array([1,2,3],[4,5,6])
arr

# Three dimensional array 

arr3  = np.array([[[10,20,30]]])
arr3
# or 
arr4   = np.array([1,2,4,6],ndmin = 3)
arr4
######################################


# get the dimensions of the array 

arr  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)
print(arr)

# ndim = 2  --> Gives you the dimensions of the array.
######################################################

# Finding the size of the each items in bytes 

arr  = np.array([10,20,30])
arr.itemsize

#####################################################

# get the data type of the each item from the array

arr  = np.array(['a','b','c'])
arr.dtype

# For numbers 
arr = np.array([1,2,4,456])
print(arr.dtype)

#########################################

# Get the shape and size of the array 

arr = [[1,2,3],[4,5,6],[7,8,9]]

print("Array Size:",arr.size) # How many intities are there.
print("Array Shape:",arr.shape) # How many rows and columns are there 

#############################

arr  = np.array([[1,2,3,4],[5,6,7,8]],dtype = 'float')

arr


#####################################

# Create  a sequence of elements using arrange function.
# arange()

# Create a seq of integers from the 0 to 20 

arr = np.arange(0,20)
arr

########################################

# Accessing the single element from the array.

arr = [1,2,4,5]

print(arr[0]) # First element
print(arr[-1]) # LAst element 
print(arr[5])# EXception 
###########################################

# Accessing an element based on the row and column index.
arr = np.array([[1,2,4,5,6],[6,7,8,9,10]])

arr.shape

print(arr[1][4])

###########################################

# Accessing the array elements based on slicing 

arr = [0,1,2,3,4,5,6,7,8,9]

arr.size


# Return the index elementss strating  from 1,3,5,7
arr[1:8:2]
arr[-1:3:-1]
arr[-2:10]

#####################################################

# indexing and slicing on the multi dimenstional array 

multi_arr = np.array([[10,20,30,40,50],[60,70,80,90,23],[43,5,4,3,3]])
multi_arr

multi_arr[0:2]  # Access first tow rows 

# Access only two columns 

multi_arr[:,:2]

# Access the perticular element of the index 2,4

multi_arr[2,4]

##############################

x  = multi_arr[:3,::2]
x

#############################################################

import numpy as np 
arr  = np.arange(35).reshape(5,7)
print(arr)

############################

# Error is there in this code.
arr = np.arange(12).shape(3,4)
rows = np.array([False,True,False])
rows
wanted_rows  = arr[rows,:]

######################################

# Convert the array into the list.

arr = np.array([1,2,3,4,5])

print("Array:",type(arr))

lst = arr.tolist()
lst
print("List:",type(lst))

#######################################

# Converting a  multidimensional array into the list.

mul_dim_arr = np.array([[[1,2,3,4]]])

nested_lst = mul_dim_arr.tolist()
nested_lst
#######################################################

# Square matrix 

sq_mat = np.array([[1,2],[6,7]])
print(f"The square matrix is:\n{sq_mat}")

####################################

# Rectangular matrix 

rect_matrix  = np.array([[1,2,4],[4,5,7]])
print(f"The rectangular matrix is:\n{rect_matrix}")

#######################################################

# Daigonal matrix.

arr  = np.diag([10,20,30])
arr

###################################

# Scalar matrix 

scalar_matrix = np.diag([1,1,1])
scalar_matrix

#####################################

# Indentity matrix --> 1's on daigonal , 0's on elsewhere 

iden_mat  = np.eye(3)
iden_mat

############################

# zero matrix 

zero_mat  = np.zeros((3,3))
print("\n Zero Matrix is:\n",zero_mat)

##########################################

# Ones matrix 
ones_mat = np.ones((3,3))
ones_mat

# upper traingular matrix 

arr  = np.array([[1,2,3],[0,,3,5],[0,0,6]])

arr

#########################################

# Lower triangular matrix

# Symmetrix matrix...

# Skew_Symmetric_matrix is a minus of transpose.

# Sparse matrix

# Row matrix # only one row and n-columns 

row_mat = np.array([12,12,12])
row_mat

# column matrix -->  n-rows and 1 column

col_mat = np.array([[1],[2],[3]])
col_mat

###########################################
# SIngleton matrix --> This is a matrix where only one element is there 

singolton_mat =  np.array([2])
singolton_mat

# Matrix Addition 

a  = np.array([1,2,4,5])
b = np.array([4,5,6,7])
add = a + b
print("Addition is:",add)
#################################
# Matrix Subtraction
print("Subtraction is:",a-b) 
##################################
# Matrix scalar multiplication
x = 4 * a
print(x)
#################################
# Dot product or matrix multiplication 
dot_of_a_b = a.dot(b)
print("Dot product of A and B is :",dot_of_a_b)
#################################
# Transpose of the A and B 

a = np.array([[1,23,4,55],[3,5,5,64]])
x = a.T
print("Transpose of matrix A is:\n",x)

###########################################################
