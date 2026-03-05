# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 21:06:06 2025

@author: chait
"""

##############################################################

lst = ['Milk','Eggs','Bread']

for index in range(len(lst)):
    print(f"{index+1}:{lst[index]}")

###################################################

# Enumerate 
# printing the lists with the their indexs 

for index,item in enumerate(lst):
    print(index,item)

# Specifying the starting point 

for index,item in enumerate(lst,start=1):
    print(index,item)

###################################################

# zip function 

lst_a = [234001,234014]
lst_b = ["Arya","Chaitanya"]

for friends in zip(lst_a,lst_b):
    print(friends)

# unpacking of tuple using the zip function 

for enr_no,name in zip(lst_a,lst_b):
    print(enr_no,name)

############################################################

# zip_largest()
from itertools import zip_longest

enr_no = [1,2,3,4]
name = ['chaitanya','Omkar','Arya']

for name,enr in zip_longest(enr_no,name):
    print(name,enr)

############################################

lst = [1,2,3,4,5,-1,6,-34,-5]

if all(lst):
    print("All values are true...")
else:
    print("All values are null values...")
    
#########################################

# any() --> Check for any non zero value is present or not

lst = [0,0,0,2,34,5] 

if any(lst):
    print("Has some zero values.")
else:
    print("Has all null values.")
    
#########################################

# counter from itertools 

from itertools import  count

counter = count()

for i in range(1,5):
    print(next(counter))
    
#####################################

# what if i want to do certain task at loop 

import random 
from itertools import cycle

def take_user_input():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    return num1,num2

def caculate_the_sum():
    x,y = take_user_input()
    print("The sum is:",x+y)
def caculate_the_diff():
    x,y = take_user_input()
    print("The difference is",x-y)

func = ['user_input','calc_sum','calc_diff']

for ins in cycle(func):
    if ins in func:
        take_user_input()
        caculate_the_sum()
        caculate_the_diff()
    
####################################################

# what if you want to repete the process for the same 
# for about 3 times

from itertools import repeat

for quote in repeat("Hello,arya would you like to be my best friend.",times=4):
    print(quote)
    
###########################################################






















































