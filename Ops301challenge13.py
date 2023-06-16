#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/15/2023
# # Purpose:

# Import the Active Directory module
Import-Module ActiveDirectory

# Set the user attributes
$givenName = "Franz"
$lastName = "Ferdinand"
$displayName = "$givenName $lastName"
$department = "TPS Department"
$title = "TPS Reporting Lead"
$company = "GlobeX USA"
$office = "Springfield, OR"
$email = "ferdi@GlobeXpower.com"

# Set the username and password for the new user
$username = "ferdinand"
$password = "@Bentonharbor253269"  # Set a strong password for the user

# Set the path where the user will be created
$ouPath = "OU=TPS Department,DC=corp,DC=globex,DC=com"

# Create a new user object
$newUser = New-ADUser -SamAccountName $username -GivenName $givenName -Surname $lastName -DisplayName $displayName -Department $department -Title $title -Company $company -Office $office -EmailAddress $email -Enabled $true -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) -ChangePasswordAtLogon $true -PassThru

# Move the user to the specified OU
Move-ADObject -Identity $newUser.DistinguishedName -TargetPath $ouPath

# Display the newly created user information
Write-Host "User created successfully:"
Write-Host "Username: $username"
Write-Host "Full Name: $displayName"
Write-Host "Department: $department"
Write-Host "Title: $title"
Write-Host "Company: $company"
Write-Host "Office: $office"
Write-Host "Email: $email"
