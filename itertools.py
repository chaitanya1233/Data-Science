# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:07:00 2025

@author: chait
"""

#########################################################

# Simple iteration over a list 
lst = ["Milk",'Egges','bread']

for index in range(len(lst)):
    print(f"{index+1}:{lst[index]}")


# Enumerate 
# Printing the list with the indexs  

lst = ["Milk",'Egges','bread']

for index,item in enumerate(lst):
    print(f"{index+1}:{item}")
    

# Zip function 

name  = ['Dada',"Mama",'Kaka']
info = [9850,6032,9785]

for nm,info in zip(name,info):
    print(nm,info)
    
# Drawbacck of the zip function 

# Not suitable if the both imbalanced list 

name = ['Dada','Mama','Kaka','Baba']
info = [9850,6032,9785]

for nm,info in zip(name,info):
    print(nm,info)
    

# SOlution to this zip --> zip_longest()

from itertools import zip_longest
name = ['Dada','Mama','Kaka','Baba']
info = [9850,6032,9785]

for name,info in zip_longest(name,info):
    print(name,info)

#######################################################

# what if i dont want to fill value as null 
# instade i want to fill as 0

from itertools import zip_longest

name = ['Dada','Mama','Kaka','Baba']
info = [9850,6032,9785]

for name,info in zip_longest(name,info,fillvalue=0):
    print(name,info)

########################################################


# all()

lst = [1,2,-3,0,4,-53,32]

if all(lst):
    print("All values are true")
else:
    print("All values are null values")


######################################

# any() --> Check for any non zero value is present or not 

lst = [0,0,0,0,0,0,0,0,0]
if any(lst):
    print("Has some non zero values")
else:
    print("Has all null values")

###################################################

# Count() from itertools 

from itertools import count

counter = count()

print(next(counter))
print(next(counter))
print(next(counter))

####################################################

# Start = 1 
from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


#####################################################

# what if i want to call the instructions on the loop

import itertools
instructions = ('Eat','Drink','Sleep')
for instruction in itertools.cycle(instructions):
    print(instruction)
#####################################################
def eat():
    print("i am eating")
def drink():
    print("I am drinking")
def sleep():
    print("I am sleeping")
#cycle()- --> Practically used in a led blubs(Blinking pattern)
import itertools
instructions = ('Eat','Drink','Sleep')
for instruction in itertools.cycle(instructions):
    eat()
    drink()
    sleep() 

#########################################################

# repeating a process for three times 

from itertools import repeat

for msg in repeat("Hello,arya would you like to be my best friend.",times=3):
    print(msg)

####################################################

# Combinations 

from itertools import combinations

player = ['John','Jani','Janardhan']

for i in combinations(player,2):
    print(i)

# Meaing is that , give me the combinations of the players of two 


#######################################################

# Permutations 

from itertools import permutations

players = ['John','Jani','Janardhan']

for way in permutations(players,2):
    print(way)

#####################################################

# procuct()

from itertools import product

team_a = ['Rohit','Pandya','Bumrah']
team_b = ['Virat','Manish','Sami']

for pair in product(team_a,team_b):
    print(pair)
    
####################################################

# filter ages who are greater than or equals to 18

age = [27,22,17,19]

adults = filter(lambda age : age>=18,age)
print([age for age in adults])

#####################################################

# refreerncing 

lst_a = [1,2,3]
lst_b = [2,3,4]

print("Id of list_a:",id(lst_a))
print("Id of list_b",id(lst_b))

lst_a = lst_b

lst_a[0] = -10


print("lst_a:",lst_a)
print("lst_b:",lst_b)


#################################################

# Applying the concept of nested_list 

old_list = [[1,2,3],[4,5,6],[7,8,'a']]

new_list = old_list

new_list[2][2] = 9

print("Old List:",old_list)
print("Id of old list:",id(old_list))


print("New List:",new_list)
print("Id of new_list:",id(new_list))

#####################################################

import copy 
 
lst_a = [1,2,3,4,5]

lst_b = copy.copy(lst_a)

# DO not affect the another list 

lst_b[0] = -10

print(id(lst_a))
print(id(lst_b))

#################################################

import copy
lst_a = [[1,2,3,4,5],[6,7,8,9,10]]
lst_b =copy.copy(lst_a)

# Changes get affected even if the ids are different for nested list 
lst_a[0][0] = 'x'


print(lst_a)
print(lst_b)  

print("id of list A:",id(lst_a))
print("Id of list B:",id(lst_b))

###################################################

# deepcopy()

import copy 

lst_a = [[1,2,3,4,5],[6,7,8,9,10]]
lst_b =copy.deepcopy(lst_a)

# Changes get not affected 
lst_a[0][0] = 'x'


print(lst_a)
print(lst_b)  

# Both ids are different 
print("id of list A:",id(lst_a))
print("Id of list B:",id(lst_b))

#########################################










































    
    
    
    
    
    
    
    
    