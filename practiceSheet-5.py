# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:21:02 2025

@author: chait
"""
'''
1️⃣ Sort Country Names (Hyphen Format)

You are given:
"india-japan-china-brazil-france"
Write a function to return them alphabetically in the same hyphen format.
'''
countries = "india-japan-china-brazil-france"
def sorted_country(countries):
    sort = countries.split("-")
    sort = sorted(sort)
    return "-".join(sort)
sorted_countries = sorted_country(countries)
print("The sorted countries are:",sorted_countries)

######################################################


'''
2️⃣ Remove Duplicate Colors

Input: "red-blue-green-blue-red-yellow"
Return: "red-blue-green-yellow" sorted and without duplicates.
'''
colors = "red-blue-green-blue-red-yellow"
def remove_duplicated_colors(colors):
    colors = colors.split("-")
    colors_set = sorted(set(colors))
    colors_list = list(colors_set)
    return '-'.join(colors_list)

unique_sorted_colors = remove_duplicated_colors(colors)
print("The sorted unique colors :",unique_sorted_colors)

######################################################

'''    
3️⃣ Check Palindrome Sentence
Write a function that checks if a sentence is 
palindrome ignoring spaces and case, e.g.
"Nurses run" → Palindrome.
'''

def palindrome(input_str): 
    if input_str == "":
        print("Please ,enter valid string")
    else:
        # convert the unput into lower case 
        input_lower = str.lower(input_str)
        #print(input_lower)
        # remove the white space
        input_lwr_split =input_lower.split(" ")
        #print(input_lwr_split)
        input_lwr_split_joint ="".join(input_lwr_split)
        
        if input_lwr_split_joint == input_lwr_split_joint[::-1]:
            return True
    return False


input_str = "Madam madam"
output = palindrome(input_str)

if output == True:
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")


#####################################################

'''
4️⃣ Count Occurrence of a Word
Given a paragraph and a word, find 
how many times the word appears.
'''

paragraph = """Ratan Tata was the son of Naval Tata, 
               who was adopted by Ratanji Tata, son 
               of Jamshedji Tata, the founder of the
               Tata Group. He graduated from Cornell
               University College of Architecture with
               a bachelor's degree in architecture.
              He had also attended the Harvard Business
              School (HBS) Advanced Management Program 
              in 1975.He joined the Tata Group in 1962,
              [7] starting on the shop floor of Tata Steel.
              He later succeeded J. R. D. Tata as chairman of 
              Tata Sons upon the latter's retirement in 1991. 
              During his tenure, the Tata Group acquired Tetley, 
              Jaguar Land Rover, and Corus, in an attempt to turn
              Tata from a largely India-centric group into a
              global business."""
              
def count_words(paragraph):
    paragraph_list = paragraph.split(" ")
    paragraph_list.remove("\n")
    paragraph_list.remove("")
    count = paragraph_list.count("the")
    return count

count = count_words(paragraph)
print("The count of Ratan Tata is:",count)

######################################################

'''
5️⃣ Extract Email Username
Input: "johndoe@gmail.com"
Output: "john.doe" using string slicing and find().
'''
email = "ckale5157@gmail.com"

def extract_username(email):
    email_split = email.split("@")
    return email_split[0]

username = extract_username(email)
print("The username of the email is:",username)


######################################################
'''
6️⃣ Mask a Phone Number

Input: "9876543210"
Output: "******3210"
(Only last 4 digits visible.)
'''
number = "98765432110"

#######################################################
'''
7️⃣ Reverse Words in a Sentence

Input: "Python is very powerful"
Output: "powerful very is Python"
'''
def reverse_words(sentence):
    sentence_list = sentence.split(" ")
    sentence_list.reverse()
    return " ".join(sentence_list)

sentence = "Chaitanya jagannath Kale"
revered_wrods=reverse_words(sentence)
print("The reversed words in a sentence are:",revered_wrods)

#############################################################

'''
8️⃣ Generate Username from Full Name

Input: "Rohan Patil"
Output: "rohan_patil_01"
Use string split & formatting.

BOOLEAN, IF-ELSE, CONDITIONS (beyond basics)
'''

import random 
def username_generator(name):
    name_list = name.split(" ")
    random_num = random.randint(1,100)
    name_list = "_".join(name_list)
    username = name_list +"_"+ str(random_num)
    return username

name = input("Enter the name of yours:")
username = username_generator(name)
print("The username is:",username)
#######################################################

'''
9️⃣ Validate Password Strength

Conditions:

length ≥ 8

contains digit

contains uppercase

contains special character

Return "Strong" or "Weak".
'''

######################################################

'''
🔟 Determine Student Grade

Marks input (0–100).
Rules:

≥90: A

≥80: B

≥70: C

≥60: D

else: Fail'''


#######################################################
'''
1️⃣1️⃣ Check Vowel or Consonant

Take a character input and identify if it's:

vowel

consonant

invalid input
'''

def is_vowels(char,vowel):
    if char in vowel:
        print(f"{char} is vowel")
    else:
        print("It is a consonent")
        
        
vowel = ['a','e','i','o','u']
char = input("Enter the character:")

if len(char)>1:
    print("Enter valid character")
else:
    is_vowels(char,vowel)

######################################################

'''
1️⃣2️⃣ Compare Two Strings (Case Independent)

Input two strings;
Return: "Same" or "Different"
ignoring capitalization.
'''

def is_similar(string1,string2):
    if str.lower(string1)==str.lower(string2):
        return True
    else:
        return False
    
string1 = input("Enter a string1:")
string2 = input("Enter a string2:")
is_output = is_similar(string1, string2)

if is_output == True:
    print("Same")
else:
    print("Different")
######################################################

'''
LIST & LOOP BASED (beyond your current level)
1️⃣3️⃣ Remove Negative Numbers from List

Input: [3, -2, 7, -8, 9]
Output: [3, 7, 9]
'''
lst = [3, -2, 7, -8, 9]

def remove_negatives(lst):
    return [i for i in lst if i>0]

lst = remove_negatives(lst)
print("After removing all negatives list is:",lst)

#######################################################

'''
1️⃣4️⃣ Sum of Even & Odd Numbers

Given a list of integers, print:

sum of all even numbers

sum of all odd numbers
'''
lst = [i for i in range(1,21)]
print(lst)

# Function to calculate sum of even numbers
def even_sum(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            total += i
    return total

# Function to calculate sum of odd numbers
def odd_sum(lst):
    total = 0
    for i in lst:
        if i % 2 != 0:
            total += i
    return total

e_sum = even_sum(lst)
o_sum = odd_sum(lst)

print("The sum of even numbers is:", e_sum)
print("The sum of all odd numbers is:", o_sum)

######################################################
'''
1️⃣5️⃣ Find Second Largest Number

Input: [10, 40, 20, 60, 30]
Output: 40
'''
def second_largest_num(lst):
    lst.sort(reverse=True)
    return lst[1]

lst = [10, 40, 20, 60, 30]
num = second_largest_num(lst)
print("The second last number is:",num)
######################################################
'''
1️⃣6️⃣ Shopping Cart Price Calculator

List of items:
[("Milk", 40), ("Bread", 30), ("Eggs", 60)]
Calculate total cost using a loop.'''

items = [("Milk", 40), ("Bread", 30), ("Eggs", 60)]
print(items)
print(type(items))

total = 0
for item in items:
        total+=item[1]
print("Total is:",total)
    
#####################################################

''''1️⃣7️⃣ Word Length Mapping

Input: ["apple", "banana", "mango"]
Output: {"apple": 5, "banana": 6, "mango": 5}'''

fruits = ["apple", "banana", "mango"]

fruits_map = dict()
for i in fruits:    
    fruits_map[i] = len(i)

print(fruits_map)
######################################################
'''
1️⃣8️⃣ Find Names Starting With a Letter

Input: names = ["Riya", "Rohan", "Kunal", "Ritika"]
Letter: "R"
Output: ["Riya", "Rohan", "Ritika"].
'''

names = ["Riya", "Rohan", "Kunal", "Ritika"]
print([i for i in names if i[0]=="R"])
######################################################
'''
SLICING, ESCAPE, FORMATTING (beyond what you wrote)
1️⃣9️⃣ Format a Receipt Using f-string

Input:

item: "Chocolate"

qty: 3

price: 45

Output example:
"You bought 3 Chocolate(s) for ₹135"
'''
item = "Chocolate"

qty = 3

price = 45

print(f"You bought {qty} {item}(s) for rupees {price} ")
#####################################################
'''
2️⃣0️⃣ Escape Characters – Print This EXACT Line

Print the following using escape characters:

He said, "It\'s a great day to learn Python!"
'''
print("He"+"\t"+"said,\t\"It\'s\ta\tgreate\tday\tto\tlearn\tpython!")
#######################################################
