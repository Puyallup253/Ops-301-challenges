#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/7/2023
# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

import os

def generate_directory_structure(path):
    for (root, dirs, files) in os.walk(path):
        print(f"Directory: {root}")
        print(f"Sub-directories: {dirs}")
        print(f"Files: {files}")
        print("-" * 50)

user_path = input("Enter the directory path: ")
generate_directory_structure(user_path)