# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 21:37:12 2025

@author: chait
"""

# Date : 5th and 6th of december
###############Saturday and Sunday###############################
'''Smart Attendance Formatter
 Build a Python program that takes a list
 of student names and their present/absent
 status, then generates a clean formatted 
 attendance report.'''
 
stud = dict()
def add_student():
    enr_no = int(input("Enter enrollment number of student:"))
    name = input("Enter name of the student:")
    status = input("wether student is Present or Absent?:")
    
    stud[enr_no] = [name,status]
    print(stud.items())

def get_students_attendence():
    enr_no = int(input("Enter the enrollment number of student to get attendence status:"))
    for i in stud.keys():
        if i == enr_no:
            print("The attendance status is:",stud.get(enr_no))
        else:
            print("Please enter valid enrollment number.")

add_student()
get_students_attendence()    

############################################

# List data structure

student = ['Arya','Chaitanya','Om']
print(student)
print(type(student))

# List constructor
l1 = list("Chaityanya")
print(l1)
print(type(l1))

l2 = list([1,2,3,4,5])
print(l2)
print(type(l2))

l3 = list(l2)
print(l3)

#Accessing a list
name = ["A","B","C","D"]
print(name[0])
print(name[-1])
print(name[:])
print(name[::-1])
print(name[-2:1])

# Inserting element

arr = [1,2,3,4,5]
arr.append(10)
print(arr)

arr.insert(0,"Om")
print(arr)


marks = [3,5,6]
print(marks[0])
print(marks[1]) 
print(marks[2])

# Order of insertion is maintained 
# Lists are enclosed within sqyare items 
# seperated by commas 
# Are mutable 
# Indexing start from 0 

# in keyword --> To check wether is item present

if 7 in marks:
    print("yes")
else:
    print("No")


# To check wether the substring is present
# in a list or string

if "Ar" in "Arya":
    print("yes")
else:
    print("No")
 

# Print all the elements of list

colors = ["Red",'Yello',"Blue",'Orange']

print(colors)
print(colors[:])

# JumpIndex concept
print(colors[1:3])
print(colors[1:3:1])

nums = [18,293,92,843,294,2234,45,4]
print(nums[1:8])

print(nums[1:8:2])

# List comprehesion -> Creating lists on fly

lst1 = [i for i in range(5)]
print(lst1) 

 
# print the table of 20 
lst = [i*20 for i in range(1,11)]
print(lst)

# List comprehension with conditions
lst3 = [1,2,4,4,5,234,2]
lst2 = [i for i in range(10) if i in lst3]
print(lst2)


# Put only even numbers in the list 
even_lst = [i for i in range(10) if i%2==0]
print(even_lst)


'''Create a list of squares of numbers from 1 to 10.'''

square_num = [i*i for i in range(1,11)]
print(square_num)
Extract only even numbers from a list of numbers 1–20.

#Convert a list of strings to uppercase using list comprehension.
color = ["red","yellow","blue","pink","orange"]
color = [str.upper(i) for i in colors]
print(color)


#Given a list of words, generate a list 
#containing the length of each word.
lenth_word = [len(i) for i in color]
print(lenth_word)

# Create a list containing the first
# letter of each word in a given sentence.'''

first_word = [i[0] for i in color]
print(first_word)

# Given a list of integers, create a list with positive numbers only.
nums = [-1,3,4,-3,4,-23,23,42,-323]
pos_num = [i for i in nums if i>0]
print(pos_num)

#From a list of fruits, return only fruits that contain the letter "a".
fruits = ["Mango","Apple",'Guava',"Orange","Kivi","papaya","Berry","Aster"]
frut = [i for i in fruits if "a" in i]
print(frut)

#Given a list of numbers, make a list containing "even" or "odd" for each number.

nums = [1,2,36,56,67,3,56,4,2,3,2454,534,23213,234,213,2334,1232]
even_nums = [i for i in nums if i%2==0]
odd_nums = [i for i in nums if i%2!=0]

print(even_nums)
print(odd_nums)

# Flatten a list of lists (e.g. [[1,2],[3,4],[5]]) into a single list.

nested = [[1,2],[3,4],[5]]
flattened =[i for item in nested for i in item]
print(flattened)


# Create a list of numbers from 1–50 that are divisible by both 3 and 5.

nums_div_by_three_five = [i for i in range(1,51) if i%3==0 and i%5==0]
print(nums_div_by_three_five)

###########################################

"""**********List methods***********"""

# list.append()
ls = [1,2,3,4]
ls.append("Hello")
print(ls) 

# list.sort()
ls = [1,4,3,12,999,544,45,65]
ls.sort()
print(ls)
# list.sort(reverse=True)
ls.sort(reverse=True)
print(ls)

# list.copy()
l = [1,2,3,4,5]
m = l  # referencing concept
m[0] = 34
print(m)
print(l)

# list.reverse()
ls = [1,2,3,4,5]
ls.reverse()
print(ls)

# list.insert(index,value)
ls = [10,20,30,40]
ls.insert(3,999)
print(ls)

# list.index(value)
ls = [89,4393,3,4,12,45]
x = ls.index(12)
print(x)


# list.count(value)
fruits = ["Papaya","Apple","Apple","Banana","Kivi"]
print(fruits.count("Apple"))

# list.extend(list)

l = [1,2,3,4,5,6]
m = [10,20,30,50,4000]
l.extend(m)
print(l)
print(m)
###########################################
 

"""Day 7 : 7th december 2025"""
# Create a tuple
tup = (1,)
print(type(tup),tup)

# You cannot change the value of the tuple 
# Once you created it.

tup = (1,4,6,16,22)
print(type(tup))
tup[0] = 32

# Index based accessing is allowed in tuple

tup = (1,32,42,33,27,35,42,63,52,32,12)
print(tup[0])
print(tup[::-1])
print(tup[:-1])
print(tup[4:-5])

# Length of the tuple 
print(len(tup))


if 243 in tup:
    print("yes")
else:
    print("No")

tup1 = tup[1:4]

if id(tup1)==id(tup):
    print("Referencing to the same object")
else:
    print("Not referencing to same object")






"""This will considered as a integer"""
t = (3)
print(t)
print(type(t))


"""This is be considered as a tuple"""
t = (3,)
print(type(t))
print(t)

###########################################

# Set datastructure 

"""This will be dictornary not set"""
s = {}
print(s)
print(type(s))

# Do not repete values.
# It is a collection of the unordered collection items
# Seperaated by commas , and enclosed within curly brackets 
# Immutable.

# Can contain values with any datatype


s = {1,2,3,2,3,4,3,2,2,2,3,4}
print(s)
print(type(s))

s1 = {"Car",True,4,"Demo"}
print(s1)
print(type(s1))


# To create a empty set 

chaitnya = set()
print(type(chaitnya))

# Accessing the values of the set

x = set([1,2,3,4,5,6,7,7,87,4])
for i in x:
    print(i)
    
# Check if item is present in a list or not 
items = {"A","B","C","D",5,6,7,23,234}
print(items)
print(type(items))

if 4 in items:
    print("Yes")
else:
    print("No")

# Union and intersections 
a = set([1,2,3,4,5])
b = set([3,2,4,6,7,9])

print("Intersection:",a.intersection(b))
print("Union:",a.union(b))


# Symmetric difference 
a = a.symmetric_difference(b)
print(a)

# Subset and superset 
print(a.issuperset(b))
print(b.issubset(a))

# Add , remove , discard and pop.
print(a)
a.add("Chaitanya")
print(a)

# remove 
print(a.remove("Arya"))
print(a.remove("Chaitanya"))

# pop
x = a.pop()
print(x)
print(a)

# del keyword 
del a
print(a)


# Clear function 
a = {1,2,3,4,5}
a.clear()
print(a)


# 


























 

