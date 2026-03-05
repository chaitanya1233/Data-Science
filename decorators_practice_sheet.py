# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 01:35:33 2026

@author: chait
"""

##################################################################

# A function defined inside another function:
def outer_function():
    return "Hello from outer function"
    def inner_function():
        return "Hello from inner function."

outer_function()

################################

# Instead of returning the result, you can 
# return the function itself:
    
def outer_function():
    def inner_function():
        return "hello from inner function"
    return inner_function # Notice there is no parenthesis

inner = outer_function()
inner()

################################

# Inner functions can use arguments from the outer function:
    
    