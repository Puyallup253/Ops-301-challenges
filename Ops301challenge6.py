#!/bin/bash

# Script Name:                 code challenge 5
# Author:                       Robert Gillespie
# Date of latest revision:      6/6/2023
# Purpose:
# Importing OS (module) libray
import os

# Declare and initialize variables
name = "John"
age = 25
location = "Ubuntu"

# Print variable values to terminal
print("Name:", name)
print("Age:", age)
print("Location:", location)

# Execute bash commands using os.system()
os.system("whoami")  # Execute 'whoami' command
os.system("ip a")   # Execute 'ip a' command
os.system("lshw -short")   # Execute 'lshw -short' command
