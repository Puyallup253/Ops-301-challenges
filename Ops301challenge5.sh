#!/bin/bash

# Script Name:                 code challenge 5
# Author:                       Robert Gillespie
# Date of latest revision:      6/5/2023
# Purpose: Write a log clearing bash script

#Write a bash script that performs the following tasks:

#Print to the screen the file size of the log files before compression
#Compress the contents of the log files listed below to a backup directory /var/log/syslog /var/log/wtmp
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#Example: /var/log/backups/syslog-20220928081457.zip
#Clear the contents of the log file
#Print to screen the file size of the compressed file
#Compare the size of the compressed files to the size of the original log files

#Print to the screen the file size of the log files before compression
backup_dir="backups"
mkdir "$backup_dir"
timestamp=$(date +%Y%m%d%H%M%S)
print_file_size() {
    file=$1
    size=$(wc -c "$file" | awk '{print $1}')
    echo "File size of $file: $size"
}

# Print original file sizes
echo "Original file sizes:"
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# Compress log files and move them to backup directory
zip_file_syslog="$backup_dir/syslog-$timestamp.zip"
zip_file_wtmp="$backup_dir/wtmp-$timestamp.zip"
zip -r "$zip_file_syslog" "/var/log/syslog"
zip -r "$zip_file_wtmp" "/var/log/wtmp"


# Print compressed file sizes
echo "Compressed file sizes:"
print_file_size "$zip_file_syslog"
print_file_size "$zip_file_wtmp"

# Compare file sizes
orig_file_syslog_size=$(du -h "/var/log/syslog" | awk '{print $1}')
orig_file_wtmp_size=$(du -h "/var/log/wtmp" | awk '{print $1}')
comp_file_syslog_size=$(du -h "$zip_file_syslog" | awk '{print $1}')
comp_file_wtmp_size=$(du -h "$zip_file_wtmp" | awk '{print $1}')

echo "Comparison of file sizes:"
echo "Original syslog size: $orig_file_syslog_size"
echo "Compressed syslog size: $comp_file_syslog_size"

echo "Original wtmp size: $orig_file_wtmp_size"
echo "Compressed wtmp size: $comp_file_wtmp_size"

# Clear log files
cat /dev/null > "/var/log/syslog"
cat /dev/null > "/var/log/wtmp"
echo "Log files have been clear"
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"





