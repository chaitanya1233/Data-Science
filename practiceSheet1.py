# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 19:26:34 2025

@author: chait
"""

'''Type Casting – Add Two Numbers (String Input)
You are given two numbers as strings: "45" and "30".
Convert them to integers and print their sum.
'''
num1 = '45'
num2 = '30'

sum = int(num1) + int(num2)
print('Sum of the two numbers is :',sum)

'''
⿢ Find Data Type of User Input

Ask the user to enter anything.
Print:

the value

the data type of the input
'''
user_input = input("Enter anything you want to enter:")
print("You entered:",user_input)
print(type(user_input))


'''⿣ Simple Interest Calculator

Take input:

principal amount

rate

time
Calculate and print Simple Interest using:
SI = (P * R * T) / 100

'''
principle = float(input('Enter your principle amount:'))
rate_of_intrest = float(input("Enter rate of intrest:"))
time = float(input('Enter the time:'))
simple_intrest = (principle*rate_of_intrest*time)/100
print('The simple intrest is:',simple_intrest)


'''Temperature Converter

Input temperature in Celsius, convert it to Fahrenheit using:
F = (C * 9/5) + 32

'''
celcius_temp = float(input('Enter the temperature in C'))
farhenite_temp = (celcius_temp* 9/5) + 32
print('The temperature in farhenite is:',farhenite_temp)


'''⿥ Even or Odd Checker

Take a number from the user.
Use the % operator to check whether it's even or odd.

'''
number = int(input('Enter your number:'))
if number%2==0:
    print('The number is even')
else:
    print('The number is odd')
    
    
    
    
'''⿦ Arithmetic Operations Program

Take two numbers from the user.
Print:

addition

subtraction

multiplication

division

floor division

modulus

exponent
'''
num1 = int(input("Enter the first number:"))
num2 = int(input('Enter second number:'))

print("The addition is:",num1+num2)
print("The subtraction is:",num1 - num2)
print("The multiplication is:",num1*num2)
print('The division is:',num1/num2)
print('The exponent is:',num1**num2)
print("The modulus is:",num1 % num2)

# Note : The modulus gives us remainder.

'''
⿧ Type Conversion – List of Strings to Integers

You have this list:
["10", "20", "30", "40"]
Convert it into a list of integers.'''

l1 = ["10", "20", "30", "40"]
print(type(l1))
l2 = []
for i in l1:
    x = int(i)
    l2.append(x)
    print("The type of the list2 is:",type(i))

print("The list 2 is:",l2)
print()   # +++++++++++


'''⿩ Swap Two Variables (Without Using Third Varia'ble)'

'Input two numbers.
Swap them using Python arithmetic:

Print new values.'''

a = int(input('Enter value of a:'))
b = int(input('Enter the value of b:'))

print("Before swapping:")
print("a:",a)
print("b:",b)
a = a + b
b = a - b
a = a - b 
print("After swapping:")
print("a:",a)
print("b:",b)


'''Input your age in years.
Convert it into:

months

days

hours


(Assume 1 year = 12 months, 365 days)'''

print("*Welcome to the Age converter application*")
age = float(input('Enter your age:'))

years  = age 
months = age * 12

hours = months * 24

days = years * 365 
print('Years lived on earth:',years)
print('months lived:',months)
print('Hours lived:',hours)
print('Days lived :',days)


'''Conclusion : Question 9th and 10th i feeled a bit difficult, codes are totally incorrect so make sure you implement on your own.'''



#########################################################
"""Problem Statement: Smart Billing & Analytics System

Create a Python program that works like a smart billing calculator for a small shop.
The program must do all the following using type casting, arithmetic operators, and data types:


---

🟦 Requirements

1. Take Inputs From User (as Strings)

Ask the user to enter:

Product name

Quantity (string input → convert to int)

Price per item (string input → convert to float)

Discount percentage (string input → convert to float)



---

2. Perform Calculations

Using arithmetic operators:

total amount = quantity × price

discount amount = (total amount × discount%) / 100

final amount = total amount − discount amount

GST = 18% of final amount

final bill amount = final amount + GST



---

3. Show Analytics

Store these values in proper data types:

A dictionary with all details

Example keys: "product", "quantity", "price", "total", "discount", "gst", "final_bill"



---

4. Output Requirements

Print:

Data type of each input and each calculated value

A clean formatted bill like:


Product: Apples
Quantity: 5
Price per Item: 30.5
---------------------------------
Total Amount: 152.5
Discount Applied: 7.62
GST (18%): 26.07
---------------------------------
Final Bill Amount: 170.19"""

print("Welcome to the Smart Billing System.")
product_name = input('Enter product name:')
quantity = int(input("Enter the how many you want:")) # (string input → convert to int)
# Price per item (string input → convert to float)
price_per_item = int(input("Enter price per item:"))
# Discount percentage (string input → convert to float)
dicount_percentage =0
GST_percentage = 18 

# Total ammount 
total_ammount = price_per_item * quantity
discounted_amount = (total_ammount*dicount_percentage)/100
final_ammount = total_ammount - discounted_amount
GST_amount = (final_ammount*GST_percentage)/100
final_billed_amount = final_ammount + GST_amount

bill = {'product':product_name,'Quantity':quantity,
        'price_per_item': price_per_item,
        'total_ammount':total_ammount,
        'Discounted_price':discounted_amount,
        'GST':GST_amount,
        'final_billed_amount':final_billed_amount}

 
print("product:",bill.get("product"))
print("Quantity:",bill.get("quantity"))
print("price per item:",bill.get("price_per_item"))
print("-----------------------------------")
print("Total amount:",bill.get("total_ammount"))
print("Discount Applied:",bill.get("discounted_amount"))
print("GST(18%):",bill.get("discounted_amount"))
print("-----------------------------------")
print("Final Bill Amount:",bill.get("final_billed_amount"))
print("*********Thank you************")
