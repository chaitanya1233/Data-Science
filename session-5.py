# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 16:30:31 2025

@author: chait
"""
###############################################################



#List 
lst = ['cherry','banana','apple',1]
print(lst)

print(lst[0])
print(lst[1])
print(lst[2])

#append() function
lst = ['cherry','banana','apple']
lst.append("Mango")
print(lst)

#clear , ie empty the list
lst = ['cherry','banana','apple']
lst.clear()
print(lst)

#copy() method
lst =  ['cherry','banana','apple']
lst2 = lst.copy()
print(lst2)

# After copy function , check if id's change or not.
if id(lst) == id(lst2):
    print("Address are same.")
else:
    print("Address are not same.")
#count() method
lst =  ['cherry','banana','apple', 'cherry']
print(lst.count('cherry'))

#extend() function
lst1 = [1,2,3]
lst2 = [4,5,6]
lst = lst1 + lst2
print(lst)

lst1.extend(lst2)
print(lst1)

#insert() method
lst = ['cherry', 'cherry','banana']
lst.insert(1,'Mango')
print(lst)

#pop()
lst = ['cherry', 'cherry','banana']
lst.pop(1)
print(lst)

#remove()
lst = ['cherry', 'cherry','banana']
lst.remove('cherry')
print(lst)

#reverse()
lst = ['cherry', 'cherry','banana']
lst.reverse()
print(lst)

#sort()
lst = ['cherry', 'cherry','banana']
lst.sort()
print(lst)

#sorted()  -> You can use parameters 
lst = ['cherry', 'kiwi','banana',"apple"]
sorted_lst = sorted(lst,key=len)
print(sorted_lst)

#nested list

nested_lst = [[1,2,3],['a','b','c'],[True,False]]
print(nested_lst)

#Accessing elememts
nested_lst[0][2]
nested_lst[1][0]

#Accessing the first inner list
print(nested_lst[0])

#Accessing specific element
print(nested_lst[1][2])

#accessing the last element of last list
print(nested_lst[-1][-1])

#Modifying element
nested_lst[1][1] = 'z'
print(nested_lst)
 
#list comprehension
lst = []
for num in range(0,20):
    lst.append(num)
print(lst)
    
# List comprehension -> List on the fly
lst = [num for num in range(0,20)]
print(lst)


# Capitalize the name of the lists 
names = ['dada','mama','kaka']
lst = [name.capitalize() for name in names]
print(lst)

#iterating over a nested list
for sublist in nested_lst:
    print(sublist)
flat_list = [ item for sublist in nested_lst for item in sublist]
print(flat_list)

#USinf 2 for loops 
for sublist in nested_lst:
    for item in sublist:
        print(item,end=" ")
        
#list comprehenssion using nested for loop
#flattening of list
flat_lst = [item for sub_list in nested_lst for item in sub_list]
print(flat_lst)

#Adding an entire sublist
nested_lst.append(['new','list'])
print(nested_lst)

#adding an element inside sublist
nested_lst[0].append(4)
print(nested_lst)

#removing elemnt from sublist
nested_lst[1].remove('z')
print(nested_lst)

##################################################


#######################################################
# tuples 

tup = ("apple","cherry","banana")
print(tup)
print(type(tup))

# once tuple is crreated you cannot change the values 
tup[1] = "Kiwi"

# if you want to change the values of the tuple 
# then conert the tuple into the list

x = ("apple","banana","cherry")
y = list(x)
print(y)

y[1] = "Kiwi"

#convert list into tuple 
x = tuple(y)
print(x)
print(type(x))

# you can access the tuples
print(x[0])
#######################################################

# to join two or more tuples you can use + oprator
tuple1 = ("a","b","c")
tuple2 = (1,2,3) 
tup1 = tuple1 + tuple2
print(tup1)

########################################################
"""Dictonaries """

dict1 ={'Bramd':"Maruti",'model':"2345","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))


# if you want specific value of the key 
dict1.get("Brand")
dict1.keys()
#######################################################

car = {
       "Brand":"Ford",
       "Model":"Mustang",
       "year":1964
       }

x = car.keys()
print(x)
########################################################
    
































