# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 15:13:36 2025

@author: chait
"""
#########################################################

"""
Question 1: Write a program to find the difference between two lists. 
List A = [1, 2, 3, 4, 5] 
List B = [3, 4, 6] 
Output: Difference (A - B) = [1, 2, 5,6]
"""
    
def lst_diff(A,B):
    # Removing the elements that are in B from A
    
    # Converting the lists into sets 
    s = set(A)
    x = set(B)
    # Returning the comman elements 
    x = s.intersection(x)
    return x
        
            
A = [1, 2, 3, 9 ,4, 5] 
B = [3, 4, 6,9]
# Calling function
x = lst_diff(A, B)


lst_B = []
for i in B:
    print(i)
    if i in x:
        continue
    else:
        lst_B.append(i)

lst_A  = []
for i in A:
    if i in x:
        continue
    else:
        lst_A.append(i)

# The difference is : A - B 
print(f"Difference (A - B) = {lst_A + lst_B}")   
            
######################################################
"""
Question 2: Write a program to count the number of digits in a given number. 
Example: 
Input: 98765 
Output: 5 
"""

def count_digits(num):
    lst = []
    while num != 0:
        rem = num % 10
        lst.append(rem)
        num //= 10
    return lst
        

num  = 9876554
digit_lst = count_digits(num)
count = len(digit_lst)
print("The number of digits are:",count)

########################################################

"""
Question 3: Write a program to find the product of all digits of a number. 
Example: 
Input: 234 
Output: 24
"""

def digits_product(num):
    product = 1
    while num != 0:
        rem = num % 10
        product *= rem 
        num //= 10
        
    return product



num = -12345
product = digits_product(num)
print(f"The product of digits of {num} is {product}")


####################################################

"""
Question 4: Write a program to check whether a number is a palindrome using digit manipulation. 
Example: 
Input: 1221 
Output: Palindrome
"""

def is_num_palendrome(num):
    s = str(num)
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"

num = 112211
output = is_num_palendrome(num)

print(f"The given number is {output}")

######################################################

"""
Question 5: Write a program to sum only odd digits of a number. 
Example: 
Input: 12345 
Output: 9 (1 + 3 + 5)
"""

def sum_odd_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            continue
        else:
            total += digit
        num //= 10
    return total

num  = 123456
to = sum_odd_digits(num)
print(f"The sum of odd digits from the given number is {to}")
################################################################


