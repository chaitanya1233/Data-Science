# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 15:07:45 2025

@author: chait
"""

"""Date : 3 December 2025"""
print(100/20)
print(type(100/20))
# / --> It is called as the Integer Division oprator.

print(100//20)
print(print(type(100//20)))


# Modulus division oprator 
print("Modulus division:",100%3)
print("Modulus division:",3%2)


# Power oprator
a = 5
b = 3
print(a**b)

# Assignment oprator 
x = 0
x += 1
print(x)


# None data type 
   """Very important for ML , AI and Data 
   science"""
winner = None
# Returns true if it is None else return False
print(winner is None)
print(winner is not None)
print(type(winner))
print("Set winner to True")
winner = True
print(winner)
print(type(winner))

###########################################

# Fow control 
  """ Comparision oprators is is must '==' """
# 1. if 
num = int(input("Enter your number:"))
if num > 0:
    print(num)
    
# Else in an If statement 
why to use: If there are two major conditions.
num = int(input("Enter yet another number:"))

if num > 0:
    print("It's Positive")
else:
    print("It's Negative")


"""If there are 
subcnditions under condition use elif"""

savings = float(input("Enter how much money you have in savings:"))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("Well done")
elif savings < 1000:
    print("That's a tidy sum")
elif savings < 10000:
    print("Welcome sir!")
else:
    print("Thank you")
    
    
###########################################
# While loop
"""Loop will continue untill and
unless some breaking condition comes."""

count  = 1
print("Starting")
while count <= 10:
    print(count)
    count += 1
    
############################################

# for loop 
"""The loop will continue untill n-1"""
print("Print out the values in range")
for i in range(2,10):
    print(i)
    #print("Done")
    
print("Done")

###########################################
# Break statement
"""Used to select the block of code 
according to the condition."""
num =  int(input("Enter a number to check for:"))
for i in range(0,16):
    if i == num:
        break
    print(i)
print("Done")
###########################################

# Annonymus variable --> _

for _ in range(0,10):
    print('.',end = ' ')
    print()
    
###########################################

#Python program to print the odd
#numbers from the give list 

start , end = 4,19

#Iterate each number in a list
for num in range(start,end+1):
    # Checking condition
    if num % 2 != 0:
        print(num,end = " ")
        
###########################################

#Python program to print the odd
#numbers from the give list 

start,end = 4,19

for num in range(start, end+1):
    if num % 2 ==0:
        print(num, end = " ")
    
