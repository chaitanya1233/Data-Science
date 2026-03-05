# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:02:53 2025

@author: chait
"""

#############################################################
# Given is a list , return the index of element if element found\
# else return not found.

def find_ele(lst,ele):
     for i in range(len(lst)):
         if lst[i] == ele:
             print(f"The element {lst[i]} is present at index {i}")
             break
         else:
             continue
     print("Not found")
         
     

lst  = [1,2,3,4,5]
ele = int(input("Enter index number:"))
find_ele(lst,ele)
########################################################

#Print the all elements after the number.

def print_ele(lst,num):
    print(lst[lst.index(num):])

num = 20
lst = [10,20,30,40,50]

print_ele(lst,num)

##########################################################

# Write a functions that returns how many times the number 
# appears in a list 

def count_duplicated(lst,num):
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
        else:
            continue
    return count


lst = [1,11,12,12,1,23,34,4,4,3,2,2,1,2,2,1]
num = 2
count = count_duplicated(lst,num)
print(f"The number of times the element {num} present is {count}")

##############################################################

# find the largest and smallest number in a list without 
# using a max() and min()

def min_max(lst):
    mini = 0
    maxi = lst[0]
    for i in range(len(lst)):
        if lst[i] > maxi: 
            maxi = lst[i] 
        elif lst[i] < mini:
            mini = lst[i]            
    return  mini,maxi

lst = [1,-2,3,7,5,6]
mini,maxi = min_max(lst)
print("The minimum element is:",mini)
print("The maximum element is:",maxi)

#######################################################

# Count vovels and consonents 

def count_consonent_vovels(string):
       vovel_count = 0
       conso_count = 0
       for i in range(len(string)):
           if str.lower(string[i]) in ['a','e','i','o','u']:
               vovel_count += 1
           else:
               conso_count += 1
       return vovel_count,conso_count

string  = "Chaitanya"
vc , cc = count_consonent_vovels(string)
print("The vovel count is:",vc)
print("The consonent count is:",cc)

########################################################

#  Number based questions 

# Write a program to count the number of digits in a
# Given number

def count_digits(num):
    count = 0
    while num != 0:
        digit = num % 10
        count += 1
        num //= 10
    return count 


count = count_digits(12334)
print("The number of digits in a given number are:",count)

#################################

# Find sum of digits of a number 

def sum_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

total = sum_digits(8742)
print("The sum of digits of a given numbers is:",total)

#################################

# Count how many digits are even and how many are odd

def count_even_odd_digits(num):
    even = 0
    odd = 0
    while num != 0 :
        digit = num % 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even , odd        
num = 123456
even,odd = count_even_odd_digits(num)
print(f"(even digits : odd digits) = {even}:{odd}")


###########################################################




























