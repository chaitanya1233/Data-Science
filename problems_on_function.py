# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:01:59 2025

@author: chait
"""

#########################################################

# The given year is leap year or not
# If it is divisible by 4 -> candidate leap year
# But , if it is also divisible by 100 , then it is NOT
# leap year
#Exception: If it is divisible by 400 , it is a leap year

def is_leaP_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is leap year")
    else:
        print(f"The {year} is not leap year")

is_leaP_year(1990)

#########################################################

score = int(input("Enter your score:"))

if score < 400 or score > 850:
    print("Invalid")
else:
    if score > 400 and score < 599:
        print("Genral")
    if score > 600 and score < 799:
        print("Diluxe")
    if score > 800 and score < 850:
        print("Premium")

#######################################################

# reverse the digits of the number 
num = int(input("Enter a number:"))

while(num!=0):
    digit = num % 10
    print(digit,end = "")
    num = num //10

#######################################################
# My logic to do this same 

def rev_num_digit(num):
    num = str(num)
    return int(num[::-1])

rev_num_digit(1234)

#######################################################

# Sum of even numbers in a list 

# Sir logic : error is there 
lst = [3,5,7,6,8]
total = 0

for i in range(len[lst]):
    if i % 2 == 0:
        total += lst[i]


print(f"Total is {total}")
###################################
# Logic 1:
total = sum([i for i in range(1,11) if i%2==0])
print(total)

# Logic 2:
lst = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in lst:
    if i % 2 == 0:
        total += i

print(total)

########################################################

# To add the digits of total numbers

# SIR's LOGIC 

num = int(input("Enter any number:"))
total = 0

while(num!=0):
    digit = num % 10
    total += digit
    num = num // 10

print(f"The total is {total}")

# MY LOGIC
def add_digits_num(num):
    total = 0
    num = str(num)
    for i in num:
        total += int(i)
    return total
total = add_digits_num(123)
print("The total is:",total)

######################################################


# Sum of the digits if they are 3 , 6, 9

num = int(input("Enter the number:")) 

total = 0

while(num!=0):
    digit = num % 10
    if digit in (3,6,9):
        total += digit
    
    num //= 10
    
print(f"Total is {total}")


######################################################

# Sum of all the positive and negative numbers form the list 

def return_total(lst):
    
    pos_total = 0
    neg_total = 0
    for i in lst:
        if i>=0:
            pos_total+=i
        else:
            neg_total+=(i)

    return pos_total,neg_total

lst = [0,-1,-2,4,5,6,-3,20]
p,n = return_total(lst)
print(f"The sum of the positive integers is {p} and negative integers is {n}")

################################################################

# reverse elements in the list # I struggled hear 

lst = [1,2,3,4,5]
for j in range(len(lst)-1,-1,-1):
    print(lst[i],end = " ")
    
    
######################################################

# Mini peak problem :
"""Those elements who are greater than their neighbors
(Also called as local maxima)"""

lst = [1,3,2,5,4,6,5]
for i in range(1,len(lst)-1):
    if lst[i-1]<lst[i]>lst[i+1]:
        print(lst[i])
######################################################

# find the maximum and minimum elements from the list 
# Note : DO NOT USE BUILD-IN FUNCTIONS.
def max_ele(lst):
    max_ele = lst[0]
    min_ele = lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max_ele:
            max_ele = lst[i]
        elif lst[i]<min_ele:
            min_ele = lst[i]
    return max_ele,min_ele
    
lst = [-1,2,4,3,54,344,65,3,343]
max_ele,min_ele = max_ele(lst)
print(f"the maximum element from the list is {max_ele}")
print(f"the minimum element from the list is {min_ele}")

#########################################################
 