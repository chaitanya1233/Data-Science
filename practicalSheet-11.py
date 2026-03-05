# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:30:08 2025

@author: chait
"""

#######################################################

# List unpacking using  * opraator 

lst = [1,2,34,54,34,45,3,42]

start = int(input("Enter the index from which you want to unpack:"))

print(*lst[start:])


#####################################################

# Search the value from the list 

lst = [1,2,3,4,5,6,7]

def found_or_not(lst,ele):
    for i in range(len(lst)):
        if lst[i] == ele:
            return "element found"
    return "element not found"

ele = int(input("Enter the element you want to search:"))
found_or_not(lst,ele)

######################################################

# count the number of vovels 

string = input("Enter hyour string:")
def count_vovels(string):
    for i in range(len(string)):
        if str.lower(string[i]) in ['a','e','i','o','u']:
            

count_vovels(string)  