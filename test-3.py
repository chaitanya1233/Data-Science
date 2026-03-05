# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 15:08:49 2026

@author: chait
"""

###############################################################

""" Write a Python program to find the second largest number in a list without using built-in 
functions like max() or sort(). """

def second_max(lst):
    first = float('-inf')
    second = float('-inf')
    for i in lst:
        if i > first:
            second = first
            first = i
        else:
            second = first
    return second
lst = [1,5.5,2,4,100,5,6,20000]
second_max = second_max(lst)
print("The second maximum element from the list is:",second_max)
#################################################################

""" Write a function compress_string(s) that compresses repeated characters in a string using 
the count of repetitions. For example:  
compress_string("aaabbccdaa") → "a3b2c2d1a2" """

def compress_string(s):
    pass


s  = "aaabbccdaa"
compress_string(s)
################################################################

"""3.Write a Python decorator called greet_decorator that
 adds the line "Hello!" before calling 
any function. Use it on a function say_name() 
that prints "My name is Python.".  """

def greet_decorator(func):
    def wrapper():
        print("Hello!")   
        func()
    return wrapper

@greet_decorator
def say_name():
    print("My name is Python.")

say_name()

#################################################################

"""4 Create an iterator that returns the squares of numbers
 from 1 to 5 using a custom class."""
 
def print_squares(lst):
    for i in iter(lst):
        print(i*i)
lst = range(1,6)


print_squares(lst)
###############################################################

"""5 Write a code example showing the difference between 
shallow copy and deep copy using a 
list of lists. Modify one inner list after copying 4
and show how each copy is affected.""" 

# Copy()
import copy

lst  = [1,2,3,4,5]

lst2 = copy(lst) # Using a shallow copy.,, no changes are reflected after using a shallow copy
lst2
lst[0] = 10 
id(lst)
id(lst2) 
lst2
lst
#############################

# Deepcopy 
import copy

mat = [[1,2,3],[4,5,6],[7,8,9]]

print('Id of mat is:',id(mat))

mat2  = copy.deepcopy(mat)

print("Id of the mat2 is:",id(mat2))

# Doing changes in the mat2
mat2[0][0] = 'x'
mat
mat2
# Even if we did changes in mat2 ,it does not affect another.->  when using copy.deepcopy()
# Changes will reflect into another when used --> copy.copy()