# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 15:12:32 2025

@author: chait
"""

#######################################################
# Write a python function that accpts a hypen 
#separated string as a input and return a colors 
#in a hyphen separated sequence after to sort the string and store it again in 
# the same format

input_string  = "red-green-blue-yello"

def sorted_colors(input_string):
    input_string = input_string.split("-")
    sorted_str = sorted(input_string)
    return '-'.join(sorted_str)

sorted_str = sorted_colors(input_string)
print("The sorted string is:",sorted_str)

#######################################################
# Check wether the givenstring is paliendrome or not 


def is_palindrome(input_string):
    if input_string == "":
        print("You entered a wrong input")
    else:
        string = input_string[::-1]
        if string == input_string:
            return True
    return False

input_string = input("Enter your string:")
output = is_palindrome(input_string)

if output == True:
    print("Given string is palindrome")
else:
    print("The given string is not palindrome")
    
#######################################################

# find function for finding the substring from the string

x = "This is python and it is very powerful"
print(x.find("python")) 

address = "4/116 Sunder Apartments,Suyognagar"
print(address.find("Sunder"))

address[6:22]
#######################################################
# String concatination 
x = "Hello"
y = "World"

print(x+y) 

# To introduce white space
print(x+" "+y)
#######################################################
# String formatting 
x = 36
y = "My name is Anthony"
print(x+y)

print(f"My name is Anthony and my age is {x}")
#######################################################

quantity = 3
item_no = 54
price = 67

print(f"I want {quantity} pieces and item number is {item_no},its price is {price}")

#######################################################

# Passing a postional argument
my_order = "I want {} pieces and item number is {},its price is {}"
print(my_order.format(quantity,item_no,price))

#######################################################      


# You can pass the postion of the agrument in the 
# format function.
quantity = 3
item_no = 54
price = 67

my_order = "I want {2} items and its item number is {1},its price is {0}"
print(my_order.format(price,item_no,quantity))

######################################################

# Escape characters

# this will show you an error
text = "This is fun fare and it has got big " round rigo""
print(text)

 #This will not give you an error
text = "This is fun fare and it has got big \" round rigo\""
print(text)

######################################################

# Python boolean 
print(10>9)
print(10==10)
print(10==9.9999)
print(9 == 9.0)

######################################################
a = 20 
b = 10

if a>b :
    print("A is greater than B")
else:
    print("B is greater than B")

######################################################

a = 20
b =10
print(a==b)

######################################################

a = 20
b =10
print(a!=b)

######################################################

"""
p = Parenthesis
E = Exponetial
M = multiply
D = DIvision
A = Addition
S = Saturday 

"""
print(3*3 + 3/3 -3)

######################################################

# indetity oprator 
a = 20
b = 10

print(a is b )
print(a is not b)
######################################################

lst1 = ["Cheery","Banana","Apple"]
print(lst1)
print(type(lst1))

print(lst1[0])
print(lst1[2])

lst = ["Cherry",1,1.3]
print(lst)

#append 
lst1.append("Mango")
print(lst1)

# Clear the list.
lst1.clear()
print(lst1)
######################################################






















