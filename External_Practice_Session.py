# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 21:40:25 2025

@author: chait
"""

# That was my logic 
"""def is_leap(year):
    leap = False
    
    # Write your logic here
    if year >= 1900 and year <= (10**5):
        if year % 4 == 0:
            if year % 400 == 0:
                leap = True
            else:
                if year % 100 == 0:
                    leap =  False
                
    
    return leap
"""

# Expected logic was:
def is_leap(year):
    leap = False
    if year >= 1900 and year <= (10**5):
        if year % 4 == 0:
            if year % 400 == 0:
                leap = True
        elif year % 100 == 0:
            leap =  False
    return leap
            
is_leap(1992)

##########################################################

from itertools import combinations

s = "HACK"

s = sorted(s)

for i in combinations(s,2):
    print("".join(i))
    
#######################################################
"""
You are given a string .
Your task is to print all possible combinations, 
up to size , of the string in lexicographic sorted 
order.
"""
string = "Chaitanya"

s = sorted(string)

count = 0
for i in range(3):
    for c in combinations(s,i):
        print("".join(c))
        count += 1

print(count)


#######################################################
# combinations means no repetition of a char is allowed 
# ex : AA BB VV SS Not allowed .
#EX : AC BD ANS ANDS, are allowed , only unique combinations are allowed 
# there is list of numbers make a app possible combinations 
from itertools import combinations
lst = sorted([3,42,1,4,3,656,756])

for i in combinations(lst,2):
    print(i)
    
#######################################################


# combinations_with_replacement means repeated combinaitions are allowed 
# Ex , AA BB CC JJ etc
from itertools import combinations_with_replacement
s,k = input().split()
k = int(k)
s = sorted(s)

for i in combinations_with_replacement(s,k):
    print("".join(i))
    
#######################################################


