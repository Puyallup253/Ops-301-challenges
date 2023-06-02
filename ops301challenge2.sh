#!/bin/bash

# Script Name:                 code challenge 2
# Author:                       Robert Gillespie
# Date of latest revision:      5/31/2023
# Purpose: Copies /var/log/syslog to the current working directory 
#Appends the current date and time to the filename                   

#Created a variable (now) that creates a timestamp with the below information
now=$(date +'%Y-%m-%dT%H:%M:%S%z')
#Copies var/log/syslog which is the full path of the file to the current directory named syslog with the contents of "now" attached
cp /var/log/syslog ./syslog-$now.txt