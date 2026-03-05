# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 21:45:06 2025

@author: chait
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int,input().split())
    arr = list(arr)
    print(arr)
    sec_max = arr[0]
    def runner_up(arr):
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if arr[i] > arr[j]:
                    sec_max = arr[j]
                
        return sec_max 
        
    x = runner_up(arr)
    print(x)


#####################################################    
    
first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second)

#####################################################

python_students = [['Harry', 37.21], ['Berry', 37.21]
                   , ['Tina', 37.12], ['Akriti', 41],
                   ['Harsh', 39]]

tup =dict(tuple(python_students))

kys = []
def sec_max(tup):
    first = float('-inf')
    second = float('-inf')
    for key,value in tup.items():
        if value > first:
            second = first
            first = value
        elif first > value > second:
            second = value
                
    return second  


s_max = sec_max(tup)
        
print(second)
print(keys)


print(dict([for k,v in tup.items() if ]))



lst = [1,2,3,4,5,5]
def dup(lst):
    for i in lst:
        for j in range(1,len(lst)):
                if i == lst[j]:
                    print(i,lst[j])
                    return True,lst[j]
        print(f"pass for {lst[i]} ended")
                

print(dup(lst))

###################################################

python_students = [['Harry', 37.21], ['Berry', 37.21]
                   , ['Tina', 37.12], ['Akriti', 41],
                   ['Harsh', 39]]

-tup =dict(tuple(python_students))

max_val_key = max(sorted(tup.items(),key = tup.get))
max_val_key

#####################################################

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

input_name = input()
def ret_lst(lst):
    for key in students:
        if key == input_name:
            return students[key]

lst = ret_lst(students)
lst
def ret_avg(lst):    
    sum = 0
    avg = 0
    for i in lst:
        sum+=i
    avg = sum / len(lst)
    return avg

avg = ret_avg(lst)
print("Average is :",avg)

#####################################################################
n = int(input())
# Number of subjects 
x = int(input())
marks = []
for i in range(n):
    marks.append(input().split())
    

#######################################################

if __name__ == '__main__':
    student_lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_lst.append([name,score])

std_dict = dict(student_lst)
std_dict
sorted_lst = list(sorted(std_dict.items(),key=lambda a :a[1]))
# store the second smallest dict item
min_tup = []
for i in range(len(sorted_lst)):
    if i == 1:
        min_tup.append(sorted_lst[i])

#######################

if __name__ == '__main__':
    student_lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_lst.append([name,score])

# Sort the nested list 
sorted_lst = sorted(student_lst)
sorted_lst
# convert it into the dictonary -> sort it and again into the nested_list

d = dict(student_lst)
d_sorted = dict(sorted(d.items(),key=lambda a:a[1]))
sorted_lst = list(d_sorted.items())
sorted_lst


min_lst = []
# Store the second smallest number into another list 
for i in range(len(sorted_lst)):
    if i == 1:
        min_lst.append(sorted_lst[i])
        

min_lst


# check for any another duplicate 
for i in range(len(sorted_lst)):
    if i == 1:
        continue
    elif min_lst in sorted_lst:
        min_lst.append(tuple(sorted_lst[i]))
        
min_lst

min_dict = dict(min_lst)

for key in min_dict.keys():
    print(key)
    
        
name = "Chaitnaya"
lst = list(name)
lst[4] = 'C'
lst
name = "".join(lst)
name        

#####################################################

# pattern printing 
"""
print:
    if n = 4
    print following pattern upto n-1
    output: 
        1
        22
        333    
"""
# Only one for loop 
# you can use arithmatic oprators 
# Only one print statement

######################################################

# Sunday : 21st december : Today is Tai's aneversary , i miss you Tai....

def solve(s):
    lst = list(s.split(" "))
    for i in range(len(lst)):
         lst[i] = str.capitalize(lst[i])
    return "".join(lst)
result = solve("hello world")

#####################################################
# String validation 

if __name__ == '__main__':
    s = input()

    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())

    
#######################################################

# print the decimal of the number 

def decimal(n):
    if n == 0 or n == 1:
        return n
    else:
        
#######################################################

# New concept 
lst =  ['1','23','4','3','4','45','4','43']
new_lst = list(map(int,lst))
new_lst

####################

# Creating the set 

s = {1,2,43}
# Creating wmpty set
emp_set = set()

# Creating a list from the list 

lst =[1,2,3,4]
s =set(lst)
print(s)

#####################################

# Modifying the set 
my_set = set(['a','b','c'])
my_set.add("d")
my_set    

my_set.add("a")
my_set


# add at a certain index 
my_set.add((2,'A'))
my_set

# Update() function in set

my_set.update({1, 6}, [5, 13])
my_set

my_set.update({1,4},['r',67])
my_set

#####################################################

# remove() and discard() method in python 
my_set.remove(67)

my_set.discard(1)
my_set.discard(67)

####################################################


