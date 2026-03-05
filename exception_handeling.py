# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 15:43:45 2025

@author: chait
"""

#################################################################

# Exception handeling -> try-except block

# Normal code without exception handeling 

a = 10
b = 0
result = a/b  # Code aborted hear.
print(result) # No execution is there.


# Same code by using exceptions  handeling 

a = 10
b = 0
result = 0
try:
    result = a/b
except ZeroDivisionError as e:
    print(f"error is {e}")


###############################

# List index out of range 

numbers = [1,2,4]
print(numbers[4])


try:
    print(numbers[4])
except IndexError as e:
    print("Error is:",e)
    

##################################

# Exception handeling : multiple exceptions 
try:
    numerator = 50
    denom = int(input("Enter denominator:"))
    quotient  = numerator / denom
    print("Calculations successfully done.")
except ValueError:
    print("Denominators can only be INTEGERS")
except:
    print("OPPS , another else exception other..")
    
    
#############################################

# Exception handeling with try-except-else

try:
    numerator = 50
    denom = int(input("Enter denominator:"))
    quotient = (numerator/denom)
    print("Division done successfully..")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Only INTEGERS should be entered.")
else:
    print("The result of the calculations is:",result)

#################################################################

# Handeling the exception using try - catch - else - finally


try:
    numerator = 50
    denom  =int(input("Enter denominator:"))
    quotient = (numerator/denom)
    print("The calculations is done.")
except ZeroDivisionError:
    print("Cannot divide a number by zero.")
except ValueError:
    print("Only INTEGERS are allowed")
else:
    print("The result is:",quotient)
finally:
    print("OVER AND OUT")

#############################################################
##############################################################
# FileNotFoundError

# Normal code without exception 
file_path = "C:/2-Ad_python/pi_digits.txt"
with open(file_path,'r') as file:
    line = file.readline()
    while True:
        print(line)
        
# Same code  with exception 
file_path = "C:/2-Ad_python/pi_digits.java"
try:
    with open(file_path,'r') as file:
        line = file.readline()
        while True:
            print(line)    
except FileNotFoundError as e:
    print("The error is:",e)
###############################################################

# Normal excecution error,Permission error 
file_path  = "C:/2-Ad_python/pi_digits.txt" 
with open(file_path,'r') as file:
    content  =file.read()
print(content)

# Try - catch block  --> PermissionError

try:
    file_path  = "C:/2-Ad_python/pi_digits.txt" 
    with open(file_path,'r') as file:
        content  =file.read()
    print(content)
except PermissionError as e:
    print("File cannot be accessed.")

###############################################################

# AttributeError 

obj = None
print(obj.some_attribute)

##############

onj  = None

if onj is not None:
    print(onj.some_attribute)
else:
    print("Obj is None!")

##################################################################

# MemoryError --> Exception is raised when system runs out of 
# memory 

huge_list = [1] * (10**10)

##############

#  Even try - catch block cannot handel that exceptions 
# Solution is generators 

def generate_memory():
    for i in range(10**10):
        yield i # yields number one by one preventing memoryError
    
gen = generate_memory()
print(next(gen))
    
#######################################################

# RecursionError 

def recursion_function():
    recursion_function()

recursion_function()

# Handeling this recursion function error by using sys 

import sys 

sys.setrecursionlimit(1000)

def safe_recursion_function(depth,max_depth):
    if depth >= max_depth:
        return "Done"
    return safe_recursion_function(depth + 1 , max_depth)

safe_recursion_function(0,1000)

###############################################################


    