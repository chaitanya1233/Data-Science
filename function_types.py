# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 15:10:54 2025

@author: chait
"""

#########################################################


# Function witg return value 

def my_function(x):
    y = x*5
    return y 

my_function(4)

######################################    

def my_function(x):
    y = x*5
    z = x*7
    return x,y

my_function(4)

########################################

# passs function keyword

def my_function(x):
    pass

my_function(4)
    
#########################################    
    
# Recursive function 

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

factorial(5)
######################################################

# lambda function

def add(x):
    sum = x + 10
    return sum 

add(20)


add = lambda a:a+10
print(add(20))


# take two arguments 
add = lambda a,b : a + b
add(2,4)
#######################################################

# filter function. 

# filter odd numbers and convert into list

lst = [34,12,64,55,75,13,63]

even_list = list(filter(lambda x:(x%2==0),lst))

print(even_list)


# Odd numbers list
odd_lst = list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)

################################################################

  