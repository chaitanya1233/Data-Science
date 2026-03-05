# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 15:06:29 2025

@author: chait
"""

#########################################################
"""Write a python function to take a list and retunrn 
True if thay have at least one common member"""

def is_comman(lst):
    org_len = len(lst)
    s = set(lst)
    aft_len = len(s)
    if  org_len == aft_len:
        return False
    else:
        return True

lst = [1,12,3,1,4,5,2]
output = is_comman(lst)
print("Output:",output)

#######################################################

"""Use list comprehension to create a new list and add
6 to each list"""

lst = [i+6 for i in range(1,6)]
print(lst)

#######################################################

"""Write a python program to reverse a string"""

def str_reverse(st):
    rev_str = ""
    for i in st[::-1]:
        rev_str += i
    return rev_str

st = input("Enter your string you want to reverse:")
rev_str = str_reverse(st)
print("The reversed String is :",rev_str)

# Alternate solution:
rev = st[::-1]
print("The reversed is:",rev)

#######################################################

"""Write a program to iterate over a dictonary using loop"""

car = {
    'Brand':'Maruti',
    'Model':'Mustang',
    'year':'1987'
    }

print("The dictonary elements are:")
for key,value in car.items():
    print(f"{key}:{value}")

#######################################################

"""Use dictoanary comprehension and conditional atrgument
create a dict form current dict where only key and value
pairs with values above 2000 are taken to new dictonary"""

current_dict = {"person1":1000,"person2":3000,"person3":4000,"person4":4300,"person5":500}

new_dict =dict([(key,value) for key,value in current_dict.items() if value > 2000])
print(new_dict)

##############################################################





























