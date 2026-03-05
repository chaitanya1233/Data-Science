# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 16:17:24 2025

@author: chait
"""

#########################################################

from datetime import date

def record_transaction():
    day = date.today()
    
    amount = float(input("Enter amount you want to log:"))
    catgory = input("Enter the amount category (Credit/Debit):")
    payment_method = str.capitalize(input("Enter the payment method (CASH/UPI):"))
    description = str.capitalize(input("Enter note if you want to enter:"))
    if description == "":
        description = "Hey, I need to make log of my money."
    
    print("Following is the dily log of your transcation:")
    
    print(f"Created on {day}")
    print(f"Amount you debited is {amount} and category is {catgory} through {payment_method}")
    
    print(f"Description:\n{description}")


record_transaction()



