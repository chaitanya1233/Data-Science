# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 22:57:10 2025

@author: chait
"""

###############################################################

"""LEVEL 1 — Controlled Iteration & Indexing (Foundations)

Concepts

range(len())

enumerate()

Objectives

Understand index–value relationships

Avoid manual index tracking

Tasks

Print a grocery list with numbering starting from 1 using range(len()).

Rewrite the same logic using enumerate().

Modify enumerate() to start indexing from 10.

Reverse-iterate the list and print index + value.

Identify why enumerate is safer than range(len()) in dynamic lists."""


# Print a grocery list with numbering starting from 1 
#using range(len()).

grocery = ['nirma','soda','soap']

for index in range(len(grocery)):
    print(index+1,grocery[index])

# Rewrite the same logic using enumerate().

for index,item in enumerate(grocery):
    print(index+1,item)
    
# Modify enumerate() to start indexing from 10.

for index,item in enumerate(grocery):
    print(index+10,item)

# Reverse-iterate the list and print index + value.

for index,item in enumerate(grocery[::-1]):
    print(index,item)

#############################################################

"""LEVEL 2 — Parallel Iteration & Data Pairing

Concepts

zip()

Imbalanced lists

zip_longest()

Objectives

Pair related datasets

Handle missing data safely

Tasks

Pair names and phone numbers using zip().

Demonstrate data loss when lists are imbalanced.

Replace zip() with zip_longest() and observe output.

Use fillvalue=0 instead of None.

Build a dictionary {name: phone} using zip_longest()."""


# Pair names and phone numbers using zip().

names = ["Chaitanya","om"]
no = [7020288007,8237652605]

for item in zip(names,no):
    print(item)

# Demonstrate data loss when lists are imbalanced.
# -->  When the lists are imbalanved we tend to go for the 
    # zip_longest()

# 
names = ['ram','chetan','Om']
no = [7020288007,8237247105,3747488222,9846482763]

for item in zip(names,no):
    print(item)

# Replace zip() with zip_longest() and observe output.

from itertools import zip_longest
for item in zip_longest(names,no):
    print(item)


# Use fillvalue=0 instead of None.

for item in zip_longest(names,no,fillvalue=0):
    print(item)

# Build a dictionary {name: phone} using zip_longest().

names = ['Chaitanya','ram']
no = ['70202888007','8237247105']
dict1 = dict()
for name,no in zip(names,no):
    dict1[name] = no

print(dict1)

############################################################

"""LEVEL 3 — Boolean Aggregation Logic

Concepts

all()

any()

Objectives

Validate datasets

Write clean condition checks

Tasks

Check if a list contains only non-zero values.

Validate whether at least one positive value exists.

Write a function is_valid_data(lst) using all().

Write a function has_signal(lst) using any().

Apply all() and any() on mixed data types."""

# Check if a list contains only non-zero values.

lst = [1,2,-34,3,0,65]

if all(lst):
    print("All are non zero elements.")
else:
    print("There is null elements present.")
    
# takeAway --> If any zero element is present => False
# if all element are non-zero --> True
            
# Validate whether at least one positive value exists.

lst = [1,2,3,4,-4,-4,52,-54]
if all(lst):
    for i in lst:
        if i > 0:
            print("Atleaast one positive element is present.")
            break
else:
    print("There are zeros in a list.")
    
# Write a function is_valid_data(lst) using all()

def is_valid_data(lst):
    if all(lst):
        print("Valid Data")
    else:
        print("Invalid Data")


lst = [1,2,4,0,54]
is_valid_data(lst)

# Write a function has_signal(lst) using any().

def has_single(lst):
    if any(lst):
        print("has zeros in the list")
    else:
        print("There are non-zeros in the list.")

lst = [1,2,3,5,0]
has_single(lst)

# Takeaway -> There are some zeros in list  => any(lst)

##############################


  
# Apply all() and any() on mixed data types.

# dataset 

mixed_data = [1,2,3,4,None,True,False,"Hello",3.14]

if any(mixed_data):
    print("zero is present.")
else:
    print("Zero is not present.")
    
# Song name : Main rahu,zhol --> listened with Arya 
   
"""LEVEL 4 — Infinite & Controlled Counters

Concepts

itertools.count()

start parameter

Objectives

Generate controlled sequences

Replace manual counters

Tasks

Generate first 5 natural numbers using count().

Start counting from 100 with a step of 5.

Stop count() safely using a condition.

Use count() to generate user IDs.

Compare range() vs count() use-cases.""" 

# Generate first 5 natural numbers using count().

from itertools import count
def generate_natural_num(limit):
    counter = count(start=1)
    for i in range(limit):
        print(next(counter))

limit = 5
generate_natural_num(limit)

# Start counting from 100 with a step of 5.

from itertools import count

counter = count(start=100,step=5)
print(next(counter)) # 100
print(next(counter)) # 105
print(next(counter)) # 110


# Stop count() safely using a condition.

def stop_safely(start,limit,stop):
    counter  = count(start = 1)
    for i in range(limit):
        print(next(counter))
        if i == stop:
            break
start = 1
limit = 10
stop = 5

stop_safely(start,limit,stop)   


##############################################################################


















   
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
    
    
    
    
    











