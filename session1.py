# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
################################################################

print('Chaitanya')


# Types of the number 
# 1.Number
x  = 10
print(type(x))


# Type casting.
# Default type of input() is String
age = input("Enter your age:")
print(type(age))                        
print(age)

# Take a input for the age1 
age1 = input('Enter your age1:')
print(type(age1))
print("The value of the age1 is:",age1)

# Take age2
age2 = 24
print("The value of the age2 is:",age2)

# what if we add age1 and age2 into age 
age = age1 + age2
print('The value of the age is',age)


# Method 
# Explicit type casting. 
# Implicit type casting.
age = int(age1) + int(age2)
print("The value of the age is:",age)
print(type(age))


# 2. Floating point number or Real number 
 # 755 STANDARDS
 
exchange_rate = 1.83
print(type(exchange_rate))
print("The exchange rate is:",exchange_rate)

# Converting to float 
int_value = 100
float_value = 1.5
string_value  ='1.5'
float_value = float(int_value)

print("The int value as a float is:",float_value)
print(type(float_value))


float_value = float(string_value)
print('The string value as a float is:',float_value)
print(type(float_value))


# 3 Complex Numbers 
c1 = 1   # --> Real number
c2 = 2j  # --> Imaginarry number
print('c1:',c1 ,"c2:",c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)


# 4. Boolean type 
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))  # ---> class <bool>


# Converting a string into boolean 
status = bool(input('OK is it confirmed?'))
print(status)
print(type(status))



# Arithmatic oprators 
home = 10 
away = 15
print(home + away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

print(100/20)
print(type(100/20))
# / --> It is called as the Integer Division oprator.


