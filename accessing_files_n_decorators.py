# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:49:25 2025

@author: chait
"""
################################################
import pandas as pd
file = pd.read_csv("C:\\2-Ad_python\\buzzers.csv")
print(file)

##################################################

"""
Created on Mon Dec 30 16:49:25 2025

@author: chait
"""

# Python do not accept the back slash '/'

import pandas as pd 
f1 = pd.read_csv('buzzers.csv') # realative path
f1 = pd.read_csv("C:/2-Ad_python/buzzers.csv") # Absolute path

# Donot use this --> "\"
# instade use this --> "/"  
#########################################################

# Ckeck for working directory 
import os 

with open("C:/2-Ad_python/buzzers.csv",'r') as file:
    print(file.read())

#########################

# reading csv as a list 
import csv
with open("C:/2-Ad_python/buzzers.csv",'r') as file:
    for line in csv.reader(file):
        print(line)

###########################

# reading a csv in form of dictonary 
import csv

with open("C:/2-Ad_python/buzzers.csv",'r') as file:
    for line in csv.DictReader(file):
        print(line)

################################

# implementation of csv.reader()

with open("C:/2-Ad_python/buzzers.csv",'r') as file:
    ignore = file.readline()
    for line in file:
        flights = line.strip().split(",")
        print(flights)

###################################

# Safely reading a sample.txt file in utf-8
file_path = "C:/2-Ad_python/sample_utf8.txt"

try:
    with open(file_path,'r',encoding='utf-8') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"File not found:{file_path}")
except UnicodeDecodeError:
    print(f"Could not decode {file_path} using utf-8")
    
###########################

# utf-16 

file_path =  "C:/2-Ad_python/sample_utf16.txt"
    
try:
    with open(file_path,'r',encoding ='utf-16') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found:",file_path)
except:
    print(f"Could not decode {file_path} using utf-16")
    
##################################

# Latin
file_path = "C:/2-Ad_python/sample_latin1.txt"

try:
    with open(file_path,'r',encoding='latin') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found:",file_path)
except UnicodeDecodeError:
    print(f"Could not decode {file_path} using unicode")

###################################

# ASCII

file_path = "C:/2-Ad_python/sample_ascii.txt"

try:
    with open(file_path,'r',encoding='ascii') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found:",file_path)
except UnicodeDecodeError:
    print(f"Could not decode {file_path} using unicode")

################################################################

# Pre-requisite to decorators 

def plus_one(number):
    number1 = number + 1
    return number1

plus_one(5)

##########################

#  Defining a function inside a another funvtion 

def plus_one(number):
    
    def add_one(number):
        number1 = number +1
        return number1
    result = add_one(number)
    return result
plus_one(5)
##############################################################

# THis is a part where i am strugulling with.
# PAssing function as argument --> Error is occuring.

def plus_one(number):
    number1 = number+f1
    return number1

def function_call(function):
    result = function(5)
    return result

result = function_call()
result()
##############################################

# Functions returning other functions

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

# Calling a hello function 
hello = hello_function()
hello()

#####################################

# Need for decorators 
import time 

def calc_square(numbers):
    start = time.time()
    result = []
    for number  in numbers:
        result.append(number*number)
    end = time.time()
    total_time = (end-start)*1000
    print(f"Total time for execution of the squares is {total_time}")
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number**3)
    end = time.time()
    total_time = (end-start)*1000
    print(f"Total time for execution of the cubes is {total_time}")
    return result 

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)      
##############################################################

# decorator 
def say_hi():
    return "hello there"

def uppercase_decorator(function):
    def wraper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wraper

decorate = uppercase_decorator(say_hi)
decorate()    

#####################################################
@uppercase_decorator 
def say_hi():
    return "arya is upset now on me"
say_hi()
####################################################
################################################################

# Day 2 :
   
# Applying two decorators to multiple functions 

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper


def uppercase_decorator(function):
    def wraper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wraper
 

@split_string 
@uppercase_decorator
def say_hi():
    return "hello there"
say_hi()
##############################################################

import time 

def time_it(func):
    # This is a decorator function that takes another func
    # as a input 
    
    def wraper(*args,**kwargs):
        # *args and **kwargs allows wraper 
        # to accept any number of positional and keyword 
        # argument 
        start = time.time()
        result = func(*args,**kwargs)
        # calls the original function (func)
        # with the provided info 
        end = time.time()
        print(func.__name__+" took "+ str((end-start)*1000)+" mili sec ")
        return result
    return wraper
        

@time_it 
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number**2)
    return result


@time_it
def calc_cube(numbers):
    result = []

    for number in numbers:
        result.append(number**3)
    return result


array = range(1,100000)
out_sq = calc_cube(array)
out_cube = calc_cube(array)

#################################################################