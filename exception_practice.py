# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 00:31:42 2026

@author: chait
"""
####################################################################

# Types of exception i learnt today

# 1.ZeroDivisionError
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide a  number by zero")
else:
    print("The result is:", result)
finally:
    print("OPPS IS CORE OF DEVELOPMENT")


# 2. ValueError

numerator = 50
try:
    denom = int(input("Enter denominator:"))
    quotient = numerator / denom
except ValueError:
    print("The error has occured.")
except ZeroDivisionError:
    print("Cannot divide a number by zero.")
else:
    print(quotient)


# 3. List index out of range

lst = [1, 2, 3]
try:
    print(lst[5])
except IndexError:
    print("Cannot access the element which is out of range.")


# 4.FileNotFoundError


file_path = "c:/chait/desktop/demo.java"

try:
    with open(file_path,'r') as file:
        line = file.readline()
        while True:
            if not line:
                break
            print(line)
except Exception as e:
    print("The error is:",e)    


# 5. Attribute error 


# The dictonary has no attribute named append 

dict1 = dict({"NAME":"cHAITNAYA","AGE":18})
try:
    dict1.append()
except Exception as e:
    print("Error occured is:",e)
    
# 6. recursion error 

# This causes a  RecursionError 
def call_function():
    call_function()
    
call_function()


# FOllowing is a error handeling mechanishm 
import sys

# Set recursion limit (be cautious with very high values)
sys.setrecursionlimit(2000)

def safe_recursion_function(depth, max_depth):
    if depth >= max_depth:
        return "Done"
    else:
        return safe_recursion_function(depth + 1, max_depth)

depth = 0
max_depth = 1000
call = safe_recursion_function(depth, max_depth)
print(call)


# MemoryError

try:
    huge_list = [0] * (10**10)
except MemoryError:
    print("Error occured")

# Another way to handel this kind of error is to genrating values 
# instade of acepting all  values at once.

def genrate_values(numbers):
    for number in range(10**10):
        yield number

try:
    gen = genrate_values(numbers)
    print(next(gen))
except StopIteration as e:
    print("Intruption has occured..")
except:
    print("Error has occured..")
finally:
    gen.close()
    print(next(gen))
######################################################################






