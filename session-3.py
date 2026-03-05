# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 14:38:32 2025

@author: chait
"""

x,y,z=5,6,7
print(x)
print(y)
print(z)
x,y,z=5
print(x)
print(y)
print(z)

#global variable
x="awesome"
def my_function():
    print("python is "+x)
my_function()

x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)

# range
x=range(6)
print(x)
print(type(x))

#distionary
x={"name":"ram","age":34}
print(type(x))

#list
lst=[1,2,3]
print(lst)
print(type(lst))

#tuple
tup=(1,2,3)
print(tup)
print(type(tup))

set1={1,2,3}
print(set1)
print(type(set1))

str1="hello"
str2=2
str3=str1+str2
print(f"hello{str2}")


x="this is python. it is very powerful"
print(x)
print(x[2:8])

#to start slicing from 0
print(x[:3])

x="government polytechnic osmanpura chhatrapati sambhajinagar"
print(x[23:32])
print(x[:10])
print(x[:22])

x="this is python.it is very powerful"
print(x[4:])

#negative indexing
s="python"
print(s[-1])
print(s[-2])
print(s[-6])
print(s[0:5:2])#pto
print(s[:5:2])#pto

s="powerful"
print(s[-6:-2])
print(s[-2:-6])
print(s[-2:-6:-2])

s="python"
print(s[ : :-1])#reverse string
print(s[-2:-6:-1])# moves backward        

#mixing positive and negative indices
print(s[1:-1])
print(s[-5:5])

x="this is python. it is very powerful"
print(x.upper())


x=x.upper()
print(x)
print(x.lower())

x="  this is python  "
print(x.strip())

x="  this is python"
print(x.lstrip())

x="this is python  "
print(x.rstrip())

x="hello"
print(x.replace("hello","gello"))

x="hello_world"
print(x.split("_"))

x='hello world'
print(x.split(' '))

x="blue-green-red"
print(x.split('-'))

x="this is python. it is difficult to implement"
print(x.split('.'))


#-------------------------------------------


"""⭐ GOOGLE-STYLE PROBLEM STATEMENT
Project Title: Smart Search Query Analyzer

You are required to build a Search Query 
Analyzer that simulates how a search engine\
(like Google) processes user queries.

The program must take a single search 
sentence as input and perform the 
following tasks:

Preprocess the query

Remove extra spaces from left, right, 
and both sides.

Convert the query to uppercase
 and lowercase.

Extract the first 3 characters,
last 3 characters, and a substring using mixed positive and negative slicing.

Tokenize the query

Split the query into individual words.

Count how many times each word appears.

Store these counts in a dictionary.

Remove duplicate words

Convert the list of words into a set
 to identify unique words.

Keyword replacement

Replace the word "python" with "java"
 wherever it appears in the query.

Character indexing

Print the characters at index 
-1, -2, and -6 of the original query.

Range-based indexing

Using range(), print the position of 
each word along with the word itself.

Store complete analysis

Save all processed information 
(cleaned query, slices, lists, sets, 
and dictionaries) into a single dictionary.

Final Output

Display all the processed results clearly,
like a mini search engine analysis report."""







