# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 20:03:34 2025

@author: chait
"""

##########################################################

"""Dictonaries in python """

dict1 = {"Brand":"Maruti","Model":"Mustang","Year":1978}
print(dict1)
print(type(dict1))

# if you want to get the specific value of the dictonary 
dict1.get("Brand")
dict1.get("year")

# return the tuple of keys 
car = {
       "Brand":"Maruti",
       "Model":"Mustang",
       "Year":1986}

print(car.keys())

print(type(car.keys()))

# return the values 

print(car.values())


# Return the set of keys and values 
print(car.items())

# Adding element to the dictoanry 

# way1 : through key
car['Fule_type'] = "Petrol"
print(car)

# way2 : update function

car = {"Brand":"Maruti","Model":"Mustang","Year":1983}



# removing the element of dictonary 

car.pop("Brand")
print(car)

# Takeaway : There should be key instade of element index 

# Iterating over a dictonary 

car = {
       "Brand":"Maruti",
       "Model":"Mustang",
       "year":1987}

for key,value in car.items():
    print(f"{key}:{value}")

# another way to iterate 
for i in car:
    print(f"{i}:{car[i]}")
    

# copy dictonary from one dictonary to another 
dict2 = dict1.copy()
print(dict2)

"""Nested dictonary"""


employees ={
    "emp1":{"Name":"Chaitanya","Age":29,"Salary":55000,"Skills":["Python","ml"]},
    "emp2":{"Name":"Arya","Age":25,"Salary":65000,"Skills":["sql","excel"]},
    "emp3":{"Name":"Om","Age":23,"Salary":55000,"Skills":["python",'ds',"ml"]},
    "emp4":{"Name":"Saket","Age":None,"Salary":45000,"Skills":[]}
     }

print(employees)


# uodate the value of the dictoanary 

dict2 = {"Brand":"Maruti","Model":"Mustang","year":1978}
print(dict2)

dict2.update({"Oil":"Disel"})
print(dict2)

# add the price to the dictonary 
dict2.update({"Price":50000})
print(dict2)

# another way to update a dictonary
dict2['Price'] = 300000
print(dict2)


###############################################################################

# sort by keys  and values 

dct = {'a':5,'b':1,'c':4}
print(dct)

sorted_by_keys = dict(sorted(dct.items(),key=lambda item:item[0]))
print(sorted_by_keys)


sorted_by_values = dict(sorted(dct.items(),key = lambda l:l[1]))
print(sorted_by_values)


# Sort by keys descedning and values in desending 

sorted_by_keys_desc = dict(sorted(dct.items(),key = lambda l:l[0],reverse=True))
print(sorted_by_keys_desc)

sorted_by_values_desc = dict(sorted(dct.items(),key=lambda l:l[1],reverse=True))
print(sorted_by_values_desc)

###############################################################################


###########################################################

""" Enumerate in python """   # Extra done.

# Simple function that add a unique value to an iterable
# Used when both index and values are important 

lst = ['bread','milk','butter','cheese']
for item in lst:
    print(item)
    
    
# Using enumerate() function 

lst = ['bread','milk','butter','cheese']
for index,item in enumerate(lst):
    print(f"{index}:{item}")
    
# you can hold index and item on the same variable 
lst = ['bread','milk','butter','cheese']

for item in enumerate(lst):
    print(item)

# The iterable object return the tuple of the index and value 

#######################################################

# Using conditional statements to process items 
# can be a very powerful technique.

tasks_by_priority = ['workout','diet','gamming']

for i,task in enumerate(tasks_by_priority):
    if i == 0:
        print("*"+str.upper(task)+"!")
    else:
       print(f"*{task}") 
      
     #Takeaway:
         
        """Calling enumerate() allows you to control
        the flow of a loop based on the index of each
        item in a list, even if the values themselves 
        aren’t important to your logic."""
        
#######################################################
"""
# Getting Every Second Item of an Iterable

You can also combine mathematical operations with 
conditions for the index. For example, you might 
need to grab every second item from a Python string.
 You can do this by using enumerate()
 """

secrate_message = "3LAigf7eq 5fhiOnpdDs2 Ra6 nwUalyo.9"

message = ""

for index,char in enumerate(secrate_message):
    if index%2==0:
        message += char
    
print(message)


#######################################################


lines = [
    "This is a\tline",
    "This line is fine",
    "Another line with whitespace  "
    ]

for lineno , line in enumerate(lines):
    if "\t" in line:
        print(f"Line {lineno}:contains a tab character")
    if line.rstrip() != line:
       print(f"line {lineno}:contains trailing whitespace") 
############################################################

# Nested dictonary

persons ={
        "person1":{"Name":"Chaitanya",
                 "Age":21,
                 "Year":2004},
        "person2":{
            "Name":"Aru",
            "Age":18,
            "Year":2007}
    }

print(persons)


# Iterate over a dictonary

person1 = {"Name":"Chaitanya",
         "Age":21,
         "Year":2004}

print(person1)    

# Accessing the dictonary 
for index,key in enumerate(person1.keys(),start = 1):
    print(index,key)
    
# Values()

print(person1.keys())
print(person1.values())
print(person1.items())

# Add an element to the dictonary 

person1['College'] = "Government Polytechnic Chhatrapati Sambhajinagar"
print(person1)

# get function 

print(person1.get("College"))

# pop()

person1.pop("Age")
print(person1)
print(len(person1))

# Iterate over a dictonary 
for i in person1:
    print(f"{i}:",person1[i])
    

# if you want to access both keys and values

for key,value in person1.items():
    print("%s %s"%(key,value))
    
# Another way to print the same 
for key,value in person1.items():
    print(key,value)
    
    
# Copy dictonary 

person2 = person1.copy()
print(person2)
print(id(person1)==id(person2))

person2 = person1
print(id(person1)==id(person2))

# another way to create a dictonary
person2 = dict(person1)
print(person2)
print(type(person2))


# update()

person1.update({"address":"Usmanpura"})
print(person1)

# Sort dictonary by keys 
person1 = {"Name":"Chaitanya",
         "Age":21,
         "Year":2004}

person1.update({"Address":"Usmanpura"})
sort_by_keys = dict(sorted(person1.items()))
print(sort_by_keys)


# Lambda functions
sum= 0
def add(n):
    sum =  n + 10
    return sum

sum = add(20)
print(sum)

# implementation of the lambda function 

add = lambda x:x+10
sum = add(20)
print(sum)
###################################
# pass age and name through the lambda function and print it

def info(name,age):
    print(name,age)

name = "Arya"
age = "34"
info(name,age)


info = lambda name,age:print(name,age)
info("Arya",34)

############################################


# sort by values 

sort_by_values = dict(sorted(person1.items(),key = lambda item:item[1]))
print(sort_by_values)


