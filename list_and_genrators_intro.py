# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 12:18:56 2025

@author: chait
"""

#########################################################

# Create a list 

lst = []
for i in range(1,21):
    lst.append(i)
    
print(lst)


#################################

# Create a list on the fly 
lst = [num for num in range(1,11)]
print(lst)

######################################################

# Capitalize the first name of each item from the list 

names = ['dada','mama','kaka']
names = [name.capitalize() for name in names]
names

####################################################\\
    
# List comprehension with if statements 

def is_even(num):
    return num % 2

lst = [num for num in range(1,11) if is_even(num)]
lst        
#######################################################

# print only even numbers from the list 

even_lst = [i for i in range(1,11) if i % 2 == 0]
even_lst
########################################################

# Generator expression 
even_sum = sum((i for i in range(10)))
even_sum

######################################################

# List comprehension for inside for 

lst = [f"{i}:{j}"for i in range(1) for j in range(3)]
print(lst)

###################################

# set comprehesion 

s = {s for s in range(1,10)}
print(s)

###########################

# Generator function in python 

def num(n):
    for i in range(n):
        yield i 

num(10)
##################################

