#!/bin/bash

# Script Name:                 code challenge 3
# Author:                       Robert Gillespie
# Date of latest revision:      6/2/2023
# Purpose:Create a bash script that launches a menu system with the following options:


#Hello world (prints “Hello world!” to the screen)

print_menu() {
  echo "Menu:"
  echo "1. Hello world"
  echo "2. Ping self"
  echo "3. IP info"
  echo "4. Exit"
}
#Ping self (pings this computer’s loopback address)
#Referenced for command and syntax in Chat GPT
handle_choice() {
  read -p "Enter your choice: " choice
  case $choice in
    1) echo "Hello world!";;
    2) ping -c 4 127.0.0.1;;   # Ping the loopback address (127.0.0.1) 4 times
    3) ifconfig;;               # Print network adapter information
    4) exit;;
    *) echo "Invalid choice";;
  esac
}
#IP info (print the network adapter information for this computer)
while true; do
  print_menu
  handle_choice
done
#Exit