#!/bin/bash

# Script Name:                 code challenge 3
# Author:                       Robert Gillespie
# Date of latest revision:      6/1/2023
# Purpose:Take care to only perform this operation in user-created directories. 
#Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

#Create a new bash script that performs the following:

#Prompts user for input directory path.
read -p "Enter the directory path: " directory_path

#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "Enter the permissions number: " permissions_number

#Navigates to the directory input by the user and changes all files inside it to the input setting.


chmod -R $permissions_number $directory_path 

#Prints to the screen the directory contents and the new permissions settings of everything in the directory.
echo "${directory_path} has new permissions of ${permissions_number}"
ls -l $directory_path 