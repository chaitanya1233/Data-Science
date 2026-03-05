# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:11:30 2025

@author: chait
"""

# Write a program to input a number and print whether it is even or odd
def is_even_odd(num):
    if num % 2==0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter any number:"))
is_even_odd(num)


# Write a program to find the sum of digits of a number.

def sum_of_digits(n):
    sum = 0
    while n!=0:
        # extract the last digit 
        last = n % 10
        
        # Add a last digit to the sum 
        sum += last
        
        # remove the last element 
        n //= 10
    return sum
    
digit = int(input("Enter any number:"))
total = sum_of_digits(digit)
print("sum of entered number digit is:",total)

# Write a program to reverse an integer.

def reverse_int(num):
    while num != 0:
        reversed_num = ""
        # extract the last number 
        last = num%10
        # Add to the reversed 
        reversed_num += str(last)
    reverse_str_num = int(reversed_num)
    return reverse_str_num



digit = 123
rev_num  = reverse_int(digit)
print("The reversed number is:",rev_num)



# Sort the given dictoanry 
data = {'a':5,'z':1,'c':4}

print(data)

sorted_by_keys = dict(sorted(data.items(),key = lambda item:item[0]))
print(sorted_by_keys)

sorted_by_values = dict(sorted(data.items(),key = lambda a:a[1]))
print(sorted_by_values)

# Return the minimum key
data = {'a':5,'z':1,'c':4}
min_value_key  = min(data,key = data.get)
min_value = data[min_value_key]
print(min_value)
#######################################################################
 # sorted in reversed order 
data = {'a':5,'z':1,'c':4}
sorted_in_rev = dict(sorted(data.items(),key = lambda arya:arya[0],reverse=True))
print(sorted_in_rev)

#######################################################

# sum of the all values in the dictoanry 

data  = sum()







