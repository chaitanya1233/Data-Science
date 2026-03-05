# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 15:00:01 2025

@author: chait
"""

########################################################
"""Dictonaries """

dict1 ={'Bramd':"Maruti",'model':"2345","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))


# if you want specific value of the key 
dict1.get("Brand")
dict1.keys()
#######################################################



car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "year":1964
       }

x = car.keys()
print(x)
########################################################

# Add the one element to the dictonary 
car['color'] = "white"
print(car)

######################################################
# CHeck the length of the car 
print(len(car))


# pop()
"""QRP:"""
car.pop("Model")
print(car)
#######################################################

# Iterating over a dictonary
for x in car:
    # if i gave x as it is : output will be keys
    # print(x)
    # if i gave car[x] = output will be values
    print(car[x])
#######################################################

# If you want access both keys and values use dict.items()

for key,value in car.items():
    print("%s = %s" % (key,value))

# Another way to print same 
for key,value in car.items():
    print(f"{key}:{value}")



#######################################################

# Copy dictonary from one dictornary to another 
car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "Year":"1976"
       }

car2 = car.copy()
print(car2)

print(id(car)==id(car2))
# Another way of making copy of any dictonary

thisdict = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":"1976"
    }

dict1 = dict(thisdict)
print(dict1)

print(id(dict1)==id(thisdict))

######################################################

# Nested dictonary: I learned new concept

our_family ={
            "child1":{
                "Name":"Ram",
                "DoB":"21-05-2008"
                },
            "child2":{
                "Name":"Sham",
                "DoB":"01-01-2008"
                }
        }

print(our_family)
######################################################

""" Dictonary methods """

# claer(): Remove all the elements of the dictonary

car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "year":"1976"
       }

car.clear()
print(car)


# copy() : copy the dictonary from one list to another.


# fromkeys()
# Create a dictonary with three keys
# All with value 0

x = {"key1",'key2','key3'} # It is a set 
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)


# get(): to get the value for the given key 

car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "Year":"1976"}

model = car.get("Model")
print(model)

# items(): return the key and value

car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "Year":"1976"}

print(car.items())
print(car.keys())
print(car.values())
######################################################

# update():Add item to the dictonary
car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "Year":"1976"}

car.update({"Color":"White"})
print(car)
######################################################

# sort by keys 
data = {'b':2,'a':5,'c':1}
data.items()

sort_by_keys = dict(sorted(data.items()))
print(sort_by_keys)


######################################################

# Normal function 
def add(a):
    sum =  a+ 10
    return sum

sum = add(20)
print(sum)

# Lambda function

# very small and code optimization technique 
add = lambda a : a+10
print(add(20))
######################################################
# sort by values

data = {'b':2,'a':5,'c':1}

sort_by_values = dict(sorted(data.items(),key = lambda item:item[1]))
print(sort_by_values)

######################################################################
