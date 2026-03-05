# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 15:03:23 2025

@author: chait
"""
#########################################################

# Return the minimum item value as a free on purchase of something


sorted_dict = {"banana":40,'apple':100,'grapes':120,'mango':200}
free_item_key = min(sorted_dict,key = sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"You will get the lowest price item {free_item_key} ({free_item_value}) for free")

#######################################################
# For maximum valued item as a free 

sorted_dict = {"banana":40,'apple':100,'grapes':120,'mango':200}

max_free_key = max(sorted_dict,key = sorted_dict.get) 
max_free_key

max_free_value = sorted_dict[max_free_key]
print(f"You will get {max_free_key} ({max_free_value}) for free!")

###############################################################

# Sort the dictonary by the desending order or revered order 

sorted_dict = {"banana":40,'apple':100,'grapes':120,'mango':200}

sorted_by_desending = dict(sorted(sorted_dict.items(),key = lambda item:item[1],reverse=True))
print(sorted_by_desending)
########################################################

# Summing values of the dictonary 

dict1 = {
    'apple':'100',
    'grapes':'120',
    'mango':'200',
    'banana':'40'
    }

total = 0
for value in dict1.values():
    total=total+int(value)  
print(total)

######################################################

dict1 = {
    'apple':'100',
    'grapes':'120',
    'mango':'200',
    'banana':'40'
    }

total_sum_using_generator = ((int(value) for value in dict1.values()))
total_sum_using_generator

#######################################################  

# Concatination in dictonary can be done using update and | (pipe) oprator 

dict1 = {1:10,2:20}
dict2 ={3:30,4:40}
dict3 = {5:50,6:60}

dict1.update(dict2)
print(dict1)
dict1 = dict1 | dict3
print(dict1)
######################################################

"""Continue"""

fruits = ['apple','cherry','banana']
for i in fruits:
    if i == "banana":
        continue
    else:
        print(i)


 # if condition is statisfied for continue : skips that iteration 
 
 
######################################################

"""Functions"""

# function without argument
def my_function():
    print("Hello , from my function")
    
my_function()
######################################################
# Function with an argument 
def my_function(name):
    print("Hello",name)
my_function("Ram")
######################################################
# Arbitary arguments :*args
def my_function(*args):
    print(args[0]+" "+args[2])
    
my_function("Tappu","Sonu","Goli")

#########################################################
# kwargs stores the data as key and value 
def myFun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
myFun(first_name = "papalal",mid_name = "Mohanlal",last_name = "Goyal")
    
#  It is not necessory to write keys in string format.

######################################################

# Hear country is a default parameter
def my_function(country = "Norway"):
    print("I am from "+country)
    
my_function("Dubai")
my_function("India")
my_function("Maharashtra")
my_function()  # Default parameter is going to be used 

########################################################

# passing a list to functions
def my_function(fruits):
    for x in fruits:
        print(x)

fruits = ['Orange','Banana','Mango']
my_function(fruits)
######################################################

