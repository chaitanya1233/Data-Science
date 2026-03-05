# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:04:17 2025

@author: chait
"""
############################################
'''. Write a Python program to assign
    three variables x, y, z in one line and
    print them.
'''
x,y,z =  10,20,30
print(x)
print(y)
print(z)
#############################################
'''Write a program to demonstrate a 
global variable and a local variable
 with the same name.
'''
age =  22
print(age)
def my_age():
    print(age)

my_age()


# Local variable is preferred over
# global variable

name  = "I am global variable, Chaitanya"
def my_name():
    name =  "I am local variable, Arya"
    print(name)

my_name()
##############################################

'''. Write a program to take a string 
    as input and print characters from
    index 2 to 8.
'''

input_str = input("Enter any string:")
print("The characters from index 2 to 8 are:",input_str[2:9])

############################################

'''Write a program to reverse a string 
    using slicing ([::-1]).
'''
name = "Chaitanya"
print("The reversed string is:",name[::-1])

############################################

'''5. Write a program to print:

first 3 characters

last 3 characters
of a given string.'''

x = "I love Someone"
print("First 3 characters are:",x[:3])
print("Last 3 characters are:",x[-1:-4:-1])
############################################

'''
6. Write a program to slice a string 
using step size 2.
'''
y = "I eat mango"
print("The string slice using step 2 is:",y[::2])
############################################

'''
7. Write a program to convert 
a sentence into UPPERCASE 
and then back to lowercase.
'''
sentence = "Hello Shivani, How are you?"
print("Uppercase is:",sentence.upper())
print("Lowercase is:",sentence.lower())

###########################################
'''
8. Write a program to remove spaces from:

left side using lstrip()

right side using rstrip()

both sides using strip()
'''

word = "Deon Deselva. "
print("word before strip:",word)
print("The word after rsplit:",word.rstrip())

word = " Saket Gokhle"
print("The word before lstrip:",word)
print("The word after lstrip:",word.lstrip())

###########################################
'''
9. Write a program to replace 
"python" with "java" in a string.
'''

sentence = "Hello ,i am learning Python."
sentence = sentence.replace("Python","Java")
print("The new sentence after replacement is:",sentence)

###########################################
'''
10. Write a program to split a string
 on "_" and print the resulting list.
'''

x = "Chaitanya_Jagannath_Kale"
print("After splitting:",x.split("_"))
###########################################
