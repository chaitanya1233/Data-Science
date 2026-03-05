# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:13:32 2025

@author: chait
"""

######################################################

"""Day : 13/12/2025 , About the revision"""

# return the minimum and maximum value from the dictonary 

dict1 = {'a':12,'b':32,'c':1}
min_value_key = min(dict1,key=dict1.get)
min_value = dict1[min_value_key]
print("The minimum value from the dictonary is:",min_value)


min_value_key = max(dict1,key=dict1.get)
max_value = dict1[min_value_key]
print("The maximum value from the dictonary is:",max_value)

########################################################

# Doing the summation of the dictonry 
dict1 = {'a':12,'b':32,'c':1}
total = 0 
for i in dict1.values():
    total = total + int(i)

print("Total is:",total)

# using generator function to calculate the sum 
dict1 = {'a':12,'b':32,'c':1}
total = 0
total = sum([total+int(i) for i in dict1.values()])
print("Total is:",total)


#######################################################

"""Unpacking the dictoanry"""

student = {
    "name":"Chaitanya",
    "marks":{
        "maths":85,
        "science":90,
        "english":78
    }
}

print(student['name'])
print(student['marks'])

# Accessing (Unpacking) Nested Dictionary Values

# direct access --> This is not real unpacking 
student['name']
student['marks']['science']
student['marks']['maths']
student['marks']['english']

# Unpacking a Nested Dictionary into Variables

marks = student['marks']
print(marks)

print(marks.items())
print(marks.values())


math = marks['maths']
print(f"You got {math} marks in maths")

english = marks['english']
print(f"You got {english} marks in english")


science = marks['science']
print(f"You got {science} marks in science")
######################################################


######################################################
"""*****************BASIC CRUD OPERATIONS***********"""

"""You have a dictionary of employee salaries:
{"Amit": 52000, "Neha": 68000, "Ravi": 45000}
How do you update Ravi’s salary to 50,000?"""

emp = {"Amit": 52000, "Neha": 68000, "Ravi": 45000}

# Update the salary of Ravi
emp['Ravi'] = 50000
print(emp.values())

"""You receive a new employee entry. How do you
 add a new key-value pair dynamically?"""
 
emp = {"Amit": 52000, "Neha": 68000, "Ravi": 45000}
emp['Chaitanya'] = 60000
print(emp.items())

# If a key is missing, how do you safely 
# fetch its value without raising an error?

print(emp.get("amit"))

# You want to check if “Neha” exists in the dictionary.
# How do you do that?

print("Neha" in emp)
########################################################

"""**********************Sorting Dictionaries***************************"""

# Sort a dictionary of students by marks (values)
# in descending order.
student = {"Amit": 80, "Neha": 34, "Ravi": 44}

sorted_by_desc = dict(sorted(student.items(),key = lambda item :item[1],reverse=True))
sorted_by_desc


# Sort a product inventory dictionary by
 # product names (keys) alphabetically.

products = {1:"Soap",2:"Nirma",3:"Peanuts"}
sorted_by_Product_names = dict(sorted(products.items(),key = lambda item :item[0],reverse=True))
print(sorted_by_Product_names)


# Given {"A": 42, "B": 12, "C": 42}, sort it
# by values and then by key if values tie.

dict1 = {"A": 42, "C": 12, "B": 42}
sorted_by_keys = dict(sorted(dict1.items(),key = lambda item:item[0],reverse=False))
print(sorted_by_keys)
sorted_by_values = dict(sorted(dict1.items(),key = lambda item:item[1],reverse=False))
print(sorted_by_values)

# You have 50k product prices stored in a dictionary. 
# Which sorting approach is faster and why?


#######################################################

"""*****************Merging Dictionaries*****************************"""

"""You have two dictionaries of sales from two 
branches. How do you merge them if keys overlap?
Example:
Branch A: {"Tea": 120, "Coffee": 200}
Branch B: {"Tea": 180, "Juice": 90}
Result should be: {"Tea": 300, "Coffee": 200, "Juice": 90}"""

branch_a = {"Tea":120,"Coffee":200}

#######################################################

# functions in python

def info(name,age):
    return name , age

name = "Chaitaya"
age = 19
name,age = info(name,age)
print(f"Name is {name} and age is {age}")
#######################################################

def my_func(par1,par2):
    print(f"I am {par1} and my friends name is {par2}")
    
my_func("Arya","Chaitanya")

######################################################


# *args and **kwargs


def fruits(*args):
    print(f"the first fruit is {args[0]} and last fruit is {args[-1]}")

fruits("papaya","banana","mango","kiwi")


def info(**kwargs):
    for key,value in kwargs:
        print(f"{key}:{value}")
        
info(name = "Chaitanya",age = 21,college = "GPCS")

######################################################


"""Problem Statement:
Build a command-line grocery billing application
 where users can add items, update quantities, 
 calculate final billing, and apply discounts."""
 

def add_item(item):
    item_name = input("Enter the product name:")
    price = input("Enter the price of the product:")
    item[item_name] = price
    print("Item added successfully....")

def update_item(item):
    item_name = input("Enter item name you want to update:")
    price = int(input("Enter the price you want to update"))
    item[item_name]=price
    print("The item updated successfully...")
    
def view_item(item):
    print("Following are items pres00ent in grocery along with their prices:")
    for key,value in item.items():
        print(f"{key}:{value}")
    

while True:
    item = dict()
    choice = int(input("Enter your choice:(1-4):"))
    
    match(choice):
        case 1:
            add_item(item)
        case 2:
            update_item(item)
        case 3:
            view_item(item)
        case 4:
            break
    
########################################################

# Given is a dictonary , print items with# a lowest price 

dict1 = {"pen":20,"book":40,"eraser":5}

# keys() --> Tuples of keys 
# values() --> Tuples of values
# items()  --> tuples of keys and values 
min_item_key = min(dict1,key = dict1.get)
min_item_price = dict1[min_item_key]
print(min_item_price)

#######################################################

dict2 = {"pen":20,"book":40,"eraser":5}

max_value = max(dict2,key = dict2.get)
maxs =dict2[max_value]
print(maxs)

######################################################

# Sort by values in descending order. 

dict2 = {"pen":20,"book":40,"eraser":5}
sort_by_dict_values = dict(sorted(dict2.items(),key = lambda item :item[1],reverse=True))
sort_by_dict_values

# Sort by keys in descending order.

dict2 ={"pen":20,"book":40,"eraser":5}
sorted_by_keys = dict(sorted(dict2.items(),key = lambda item:item[1],reverse=True))
sorted_by_keys

#######################################################

# Saturday : week2 "Question practice"

"""Question 1: Deep Dictionary Analysis (Multi-Concept)

You are given a nested dictionary representing employees:

employees = {
    "emp1": {"name": "Amit", "age": 28, "salary": 55000, "skills": ["python", "ml"]},
    "emp2": {"name": "Neha", "age": 24, "salary": 48000, "skills": ["sql", "excel"]},
    "emp3": {"name": "Rahul", "age": 30, "salary": 70000, "skills": ["python", "ds", "ml"]},
    "emp4": {"name": "Pooja", "age": None, "salary": 45000, "skills": []}
}


Tasks:

Remove employees whose age is None

Sort remaining employees by salary (descending)


Return a new dictionary containing:

employee id as key

name and salary only

Print the employee with the maximum number of skills

Constraints:

Do not use sorted() directly on dictionary values

Use loops and logic"""



employees = {
    "emp1": {"name": "Amit", "age": 28, "salary": 55000, "skills": ["python", "ml"]},
    "emp2": {"name": "Neha", "age": 24, "salary": 48000, "skills": ["sql", "excel"]},
    "emp3": {"name": "Rahul", "age": 30, "salary": 70000, "skills": ["python", "ds", "ml"]},
    "emp4": {"name": "Pooja", "age": None, "salary": 45000, "skills": []}
}


##############################################################

"""Question 3: Generator + List Comprehension

Create a generator function that yields only valid numbers 
from a mixed list:

data = [10, "20", None, 5.5, "abc", 30, -5, "40"]

0
Valid number rules:

Integers or floats only

Ignore strings (even numeric strings)

Ignore None

Ignore negative numbers

Then:

Convert generator output into a list using list comprehension

Calculate:

sum

minimum

"""

def valid_numbers(data):
    for item in data:
        if isinstance(item, (int ,float)) and item>0:
            yield item

data = [10, "20", None, 5.5, "abc", 30, -5, "40"]
valid_lst = [i for i in valid_numbers(data)]

min_num = min(valid_lst)
max_num = max(valid_lst)
sum_num = sum(valid_lst)

print("Min:",min_num)
print("Max:",max_num)
print("Sum:",sum_num)

#############################################################


def count_up_to_n(n):
    for i in range(1,n+1):
        yield i
    
gen = count_up_to_n(5)

print(next(gen))
print(next(gen))
for i in gen:
    print(i)

#############################################################
"""Task:
Create a generator that yields even numbers from 0 to 10.

Think first:

Loop

Condition

yield

Try it before scrolling."""

def even_nums_upto_n(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

even_gen_lst = [i for i in even_nums_upto_n(10)]
print(even_gen_lst)

##############################################################
"""LEVEL 2 — GENERATORS WITH CONDITIONS (FILTERING)
Concept 2: Generator as a Filter

Generators are excellent for filtering large datasets."""

#example: 

def positive_num(data):
    for x in data:
        if x>0:
            yield x 


data = [i for i in range(-10,4)]
positive_data = [i for i in positive_num(data)]    
print(positive_data)



"""Task:
From a list, yield only strings.

data = [10, "hi", 5.5, "python", None]


Expected output:

"hi", "python"

"""
def string_data(data):
    for i in data:
        if isinstance(i,(str)):
            yield i
            
            

data = [10,"hi",5.5,"python",None]

gen = string_data(data)
print(next(gen),end=",")
print(next(gen))
#string_data_lst = [i for i in string_data(data)]
#print(string_data_lst)

##############################################################
"""PRACTICE 3

Task:
Create a generator that yields numbers > 10, then convert it to a list.

data = [5, 12, 3, 25, 7]
"""
def nums_filter(data):
    for i in data:
        if i>10:
            yield i
            
data = [5,12,3,25,7]
gen_lst = [ i for i in nums_filter(data)]
print(gen_lst)

######################################################

"""LEVEL 4 — GENERATOR EXPRESSIONS (INTERMEDIATE)
Concept 4: Generator Expression (One-Line Generator)
gen = (x for x in range(10) if x % 2 == 0)


Difference:

Parentheses ()

Lazy evaluation

No function definition

PRACTICE 4

Task:
Create a generator expression that yields squares 
of odd numbers from 1 to 10."""

gen = (x*x for x  in range(1,11) if x%2!=0)
for i in gen:
    print(i)

######################################################

"""
Concept 5: Combining Rules

Pattern:

if isinstance(x, int) and x > 0:
    
Question :
Yield only positive integers from:

data = [10, -3, 4.5, "5", 8, None]

"""
data = [10, -3, 4.5, "5", 8, None]

def pos_int(data):
    for i in data:
        if isinstance(i,int) and i>0:
            yield i
            
gen_lst = [x for x in pos_int(data)]
print(gen_lst)

######################################################

"""
Task:
Flatten this list using a generator:

matrix = [[1, 2], [3, 4], [5]]
"""       

def flatten_lst(matrix):
     for i in matrix:
         for j in i:
             yield j
 
matrix = [[1, 2], [3, 4], [5]]
gen_lst = [x for x in flatten_lst(matrix)]
print(gen_lst)

######################################################

'''
LEVEL 7 — GENERATORS WITH STATE (ADVANCED)
Concept 7: Generator Remembers Its State            
'''          

def cummulative_sum(data):
    total = 0
    for i in data:
        total += i
        yield i


data = [1,2,3,4,5]
gen_lst = [x for x in cummulative_sum(data)]
print(gen_lst)

######################################################
    
"""LEVEL 8 — REAL-WORLD PATTERN (INTERVIEW LEVEL)
Concept 8: Generator + Validation

This mirrors real data pipelines.

PRACTICE 8

Task:
Yield valid numbers:

int or float

non-negative

data = [10, "20", None, 5.5, -3]"""

data = [10, "20", None, 5.5, -3]

def non_negative_nums(data):
    for i in data:
        if isinstance(i, (int, float)) and i > 0:
            yield i

# gen = non_negative_nums(data)
# print(next(gen))
gen_lst = [i for i in non_negative_nums(data)]

print(gen_lst)
#######################################################

""" Make a genrator to validate only the integers"""

data = [10,"20",None,5.5,-3]

def postive(data):
    for i in data:
        if isinstance(i,(int)) and i>0:
            yield i

gen_lst = [i for i in postive(data)]
print(gen_lst)    

######################################################


    
    
    
        




