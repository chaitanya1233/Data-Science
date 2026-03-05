# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 21:00:23 2025

@author: chait
"""

########################################################

# Sum of the digits :

def sum_digits(num):
    total = 0
    while num != 0:
        digit = num % 10 
        total += digit
        num //= 10
    
    return total

num = 123456
sum_digits(num)
######################################################

# Reverse the digits of the number.

def rev_num(num):
    while num != 0:
        digit = num % 10
        print(digit,end = "")
        num //= 10

rev_num(123)
#######################################################

# Find the maximum and minimum element from the list 

def min_max(lst):
    mini = float("inf")
    maxi = 0
    
    for i in lst:
        if i > mini:
            maxi = i
        else: 
            mini = i
    return mini,maxi

lst = [0.231,2,3,24,5]
mini , maxi = min_max(lst)
print("The minimum element is:",mini)
print("The maximum element from the element is:",maxi)

########################################################

# Sum of all the positive and negative numbers form the list 

def total(lst):
    n_sum = 0
    p_sum = 0
    for i in range(len(lst)):
        if lst[i] >= 0:
            p_sum += lst[i]
        if lst[i] < 0:
            n_sum += lst[i]
    return n_sum,p_sum

 m 
lst = [-1,-2,-4,9,53,3,-85]
n_sum,p_sum = total(lst)
print("The sum of negative numbers from the list are:",n_sum)
print("The sum of positive numbers form the list are:",p_sum)

#######################################################


# Mini peak problem



