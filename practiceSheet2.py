# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 21:27:34 2025

@author: chait
"""

'''1. Student Report Card Generator

Write a program that:

Asks the user for 5 subject marks. (use for loop)

Calculates the total and average.

Uses elif to assign a grade:
A (90+), B (80+), C (70+), D (60+), F (else)

If average < 40, print “Fail”, else “Pass”.

Repeat the whole program until the user types exit. (use while loop)

'''

marks = []
for i in range(1,6):
    user_input =int(input("Enter the marks of subjects:"))
    marks.append(user_input)

print(marks)

sum = 0
for i in marks:
    sum += i
print("The sum of subjects is:",sum)
average_marks = sum/5
print("The average of the marks is:",average_marks)
    
if average_marks > 90 and average_marks < 100:
    print("A grade")
elif average_marks > 80 and average_marks < 90:
    print("Grade B")
elif average_marks > 70 and average_marks < 80:
    print("Grade C")
elif average_marks > 60 and average_marks < 70:
    print("Grade D")
else:
    print("Grade F")
    
# Pass or fail 
if average_marks >= 36:
    print("Pass")
else:
    print("Fail")


'''2. Menu-Driven Calculator

Create a program that:

Runs in a while loop until the user chooses “quit”.

Shows a menu:

Add

Subtract

Multiply

Divide

Multiplication table

Quit

Uses if–elif to perform the correct operation.

If the user selects option 5, print its table using a for loop.
'''
while True:
    print("------------------------")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Quit")
    choice = int(input("Enter your choice:"))
    if choice != 5:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        
    match(choice):
        case 1:
            sum = num1 + num2
            print("The sum is",sum)
        case 2:
            sub = num1 - num2
            print("The subtration is:",sub)
        case 3:
            mul = num1 * num2
            print("The multiplication is:",mul)
        case 4:
            div = num1 / num2
            print("The Division is:",div)
        case 5:
            break


'''3. Number Analyzer

Write a program that:

Asks user for a number.

Checks if it is even or odd (if–else).

Checks if it is prime (use for loop).

Prints all factors of the number (use for loop).

Let the user analyze numbers repeatedly until they enter 0 (while loop).

'''

user=int(input("enter a number:"))

if user% 2== 0:
    print("it is an even number")
else:
    print("it is an odd number")

'''fact = 1
for i in user:
    fact = fact * i
print(fact)'''
    
    
    
    
    
    
    
    
    



