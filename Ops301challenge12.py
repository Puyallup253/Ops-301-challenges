#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/14/2023
# # Purpose:Today, you will be performing HTTP GET requests using the requests Python library. This library is very useful for a security professional to evaluate how a web server responds to outside requests.

import requests

# Prompt the user for destination URL and HTTP method
url = input("Enter the destination URL: ")
http_method = input("Enter the HTTP method (GET/POST/PUT/DELETE/HEAD/PATCH/OPTIONS): ")

# Print the request information
print(f"Sending {http_method} request to: {url}")
confirmation = input("Are you sure you want to proceed? (yes/no): ")

# Check user confirmation
if confirmation.lower() != "yes":
    print("Request canceled.")
    exit()

# Perform the request
response = requests.request(http_method.upper(), url)

# Translate status code to plain terms
status_code = response.status_code
status_message = requests.status_codes._codes[status_code][0].replace("_", " ").title()

# Print the response information
print(f"\nResponse Status: {status_code} - {status_message}")

# Print response header information
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
