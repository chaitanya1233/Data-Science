# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:59:58 2025

@author: chait
"""
#########################################################

def valey_count(n,path):
    elevation = 0  # current heigh from sea level (0 = sea level)
    valey_count = 0 # Number of valleys = number of times returned at sea level after going down
    
    for step in path: # Go through each step in the journey
        if step == "U": # If a step is UP
            elevation += 1  # move one step up
            if elevation == 0: # Just came back to sea level
                valey_count += 1 # Completed one valley
        else: # If step is Down ("D")
            elevation -= 1 # Move one step down 
    return valey_count 

        
n = 8
path = "UDDDUDUU"
valley_count = valey_count(n,path)
print(f"The valey count is {valley_count}")


########################################################


"""MY VERSION"""

def valley_count2(n,path):
    elevation = 0
    valley_count = 0
    for step in path:
        if step == "D":
            elevation -= 1
        else:
            elevation += 1
            if elevation == 0:
                valley_count += 1
    return valley_count


n = 3
path  = "UDDDUDUU"
valley_count2(n, path)

#######################################################

def rotate_keft(lst,d):
    # what if d > than elements of lst so always use following synax
    n = len(lst)
    if d > n:
        d = d % n
        
    rotate_lst = lst[d:] + lst[:d]
    return rotate_lst


d = 3
lst = [1,2,3,4,5]
rotate_keft(lst, d)

######################################################

# Matrix in python -> List of lists 

mat = [
       [1,2,3],
       [4,5,6],
       [7,8,9]]

print(mat)

rows = len(mat)
cols = len(mat[0])
print("The number of rows are:",len(mat))
print("The number of columns are:",len(mat[0]))

for i in range(rows):
    for j in range(cols):
        print(f"The element at mat[{i}][{j}] is {mat[i][j]}")

#############################################################

#addition of the matrix.
#To add the two matrix their number of rows
#should be equals to columns

mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

mat2 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

rows = len(mat1)
cols = len(mat1[0])

for i in range(rows):
    for j in range(cols):
        result[i][j] = mat1[i][j] + mat2[i][j]

print(result)

#######################################################

# Find dau=igonal elements of the matrix 
mat4 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

rows = len(mat4)
cols = len(mat4[0])

print("The daigonal elements are:")
for i in range(rows):
    for j in range(cols):
        if i == j :
            print(mat4[i][j])

#######################################################

mat = [[0,0,2],
      [1,2,54],
      [0,32,20]]

rows = len(mat)
cols = len(mat[0])

count = 0

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == 0:
            count += 1
        else:
            continue

total_elements = rows * cols
print("total elements:",total_elements)
print("Count:",count)         
if count > total_elements/2:
    print("The given matrix is sparse.")
else:
    print("The given matrix is not sparse.")

#######################################################
