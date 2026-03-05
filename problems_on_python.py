# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:17:42 2025

@author: chait
"""

#######################################################


# Unpacking of the list 
lst = [13,4,6,8,9]

num = int(input("Enter the number from the list:"))
start = lst.index(num)
print(*lst[start:])

#######################################################

# Search the value from the list

lst = [13,4,6,8,9]
num = int(input("Enter the number you want to search:"))

def search_num(lst,num):
    for i in range(len(lst)):
        if i == num:
            return "value found"
    return "value not found"

search_num(lst, num)

############################

# Wrong logic 

def search_num(lst,num):
    for i in range(len(lst)):
        if lst[i] == num:
            return 'value found'
        else:
            return 'value not found'

num = 6
search_num(lst, num)
##############################################

# count the number of vovels

input_string = str.lower(input("Enter your string:"))

def count_vovels(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i] in ['a','e','i','o','u']:
            count += 1
    return count

count_vovels(input_string)
########################################################

# Find sum of numbers from list which are divisible by  5 or 7 

lst  = [1,2,5,15,7,42]

total = 0
for i in lst:
    if i % 5 == 0 or i % 7 == 0:
        total += i
print(total)

#####################################################
# write  a function that return True if any duplicate element
# is present in the list 
def find_dup(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

find_dup(lst)

########################################################

#  Write a program to count the digits from the numbers

def count_digits(num):
    count = 0
    while num != 0:
        digit = num % 10
        count = count +1 
        num //= 10
    return count

num  = 1234
count_digits(num)

####################################################

num = 1234
count_digits(num)