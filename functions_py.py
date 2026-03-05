# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:43:48 2025

@author: chait
"""
#########################################################

def info(name):
    return name

name = info("Arya")
print("The name is:",name)

########################################################

# Function with multiple parameters 

def calc(a,b):
    add = a + b
    mul = a * b 
    return mul,add

a = 10
b = 2
x,y =calc(a, b)
print("x:",x)
print("y:",y)

#######################################################


# pass keyword : when buisness logic is not known to us.
def syn():
    pass

syn()


#######################################################

# n factorial = n * factorial(n-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(5)
print(fact)

#######################################################

# filter function.

# lambda function  
# func_name  = lambda argument : buisness logic 

# simple function 

def info(name,age):
    print(f"Name is {name} and age is {age}")

name = "Arya"
age = 34

info(name, age)

#########################

# same execution with lambda function

info  = lambda name,age:name , age


# Error containing lines 
# name,age = info("Arya",34)
# print(info("Arya",34))


#########################################################


lst = [12,3,4,23,6,78976,34]

even_lst  = list(filter(lambda x:x%2==0,lst))
print(even_lst)

odd_lst=list(filter(lambda x:x%2!=0,lst))
print(odd_lst)


######################################################
"""List comprehension"""
                
lst = [1,2,3,4,5]

for i in lst:
    print(i)
    
# Iterating over a string 

name =  "Arya"
for i in  name :
    print(i,type(i))
    
################################################

syntax : [value | loop | condition]

# create a list of having numbers from 1 to 10 usig list comprehension 

lst  = [ i for i in range(1,11)]
print(lst)

# store only numbers that are even 
even_lst = [i for i in lst if i % 2 == 0]
print(even_lst)

# Nested list -> List inside list 

nested_lst = [[1,2,3,4],[5,6,7,8,9,10]]


lst = []
for i in nested_lst:
    for j in i:
        lst.append(j)
        

print(lst)


dictonary  = {"Name":"Arya","Age":34}
print(dictonary.items())
# dictoanry = {},[(),()] --> Tuples of list.
# list = []
# tuples = ()
# set = {}

##########################################################

current_dict = {"person1":1000,"person2":3000,"person3":4000,"person4":4300,"person5":500}


new_dict = [value for value in current_dict.values() if value>2000]
print(new_dict)

######################################################

