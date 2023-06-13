#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/12/2023
# # Purpose:Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.



# Create a new text file
file_name = "code.txt"
with open(file_name, "w") as file:
    file.write("Dogs eat dog food. 1\n")
    file.write("Cats eat cat food. 2\n")
    file.write("Turtles eat turtle food. 3\n")

# Read and print the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("First line:", first_line)

# Delete the file
import os
os.remove(file_name)
