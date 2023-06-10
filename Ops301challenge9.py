#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/8/2023
# # Purpose: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

a = 5
b = 10

# Using the "equals" conditional (a == b)
if a == b:
    print("a is equal to b")
    
# Using the "not equals" conditional (a != b)
if a != b:
    print("a is not equal to b")

# Using the "less than" conditional (a < b)
if a < b:
    print("a is less than b")
    
# Using the "less than or equal to" conditional (a <= b)
if a <= b:
    print("a is less than or equal to b")

# Using the "greater than" conditional (a > b)
if a > b:
    print("a is greater than b")

# Using the "greater than or equal to" conditional (a >= b)
if a >= b:
    print("a is greater than or equal to b")

# Using an if statement with elif and else
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b or an error occurred")
