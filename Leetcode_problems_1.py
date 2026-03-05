# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 13:52:27 2025

@author: chait
"""
#########################################################

"""
Logic 1: Track when you are below sea level

Instead of checking only when you come back to sea level,
we can check whenever we enter a valley (going below sea level)
and count it once.
"""

def deeper_count(path):
    elevation = 0
    valey_count = 0
    for i in path:
        if i == "U":
            elevation += 1
        else:
            elevation -= 1
            if elevation == 0:
                valey_count += 1
    return valey_count

deeper_count("UDDDUDUU")

########################################################

"""
Problem: Counting Mountains

A mountain is a sequence of steps above sea level that starts with an upward step ("U") from sea level and ends when you return to sea level.

Task: Write a function that counts the number of mountains in a given hike path.

Input:

n: number of steps

path: string of "U" (up) and "D" (down) steps

Output:

Integer, the number of mountains
"""

def count_mountains(path):
    elevation = 0
    mountains = 0
    for i in path:
        if i == "U":
            elevation += 1
        else:
            elevation -= 1
            if elevation == 0:
                mountains += 1
    return mountains


count_mountains = count_mountains("UDUUUDDD")
print(f"Number of mountains are: {count_mountains}")

#####################################################################################

# Rotate an arrray to ,left by 4 

def rotate_array(arr,d):
    n = len(arr)
    if d > n:
        d = d % n
    rotated_arr = arr[d:] + arr[:d]
    return rotated_arr

arr = [1,2,3,4,5,6]
d = 4
rotated_arr = rotate_array(arr, d)
print("The rotated array is:",rotated_arr)

#######################################################

# print the matrix and daigonal elements 

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

rows = len(mat)
cols = len(mat[0])


for i in range(rows):
    for j in range(cols):
        print(f"The element at index mat[{i}][{j}] is {mat[i][j]}")
        
#####################################################
# Daigonal elements are :

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

rows = len(mat)
cols = len(mat[0])    
    
print("The daigonal elements are:")
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(mat[i][j])
print("------------------------") 

######################################################           
# Perform the matrix Addition 

mat1 = [[1,2,3],
       [3,4,5],
       [6,7,8]]

mat2 = [[1,2,4],
        [3,4,5],
        [5,6,7]]

add = [[0,0,0],
       [0,0,0],
       [0,0,0]]
rows = len(mat1)
cols = len(mat1[0])


for i in range(rows):
    for j in range(cols):
        add[i][j] = mat[i][j] + mat2[i][j]

print(add)

###############################################################

# Sparse matrix

matrix = [[0,0,0],
          [0,3,0],
          [3,0,0]]             

rows  = len(matrix) 
cols = len(matrix[0])

count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            count += 1

if (rows*cols)/2 < count:
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")

######################################################






