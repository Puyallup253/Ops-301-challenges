#!/usr/bin/env python3
# Script Name:                 code challenge 7
# Author:                       Robert Gillespie
# Date of latest revision:      6/12/2023
# # Purpose: Use Psutil to fetch system information.



import psutil

# # Time spent by normal processes executing in user mode
user_time = psutil.cpu_times().user

# # Time spent by processes executing in kernel mode
kernel_time = psutil.cpu_times().system

# # Time when system was idle
idle_time = psutil.cpu_times().idle

# # Time spent by priority processes executing in user mode
priority_user_time = psutil.cpu_times().nice

# # Time spent waiting for I/O to complete
io_wait_time = psutil.cpu_times().iowait

# # Time spent for servicing hardware interrupts
hardware_interrupt_time = psutil.cpu_times().irq

# # Time spent for servicing software interrupts
software_interrupt_time = psutil.cpu_times().softirq

# # Time spent by other operating systems running in a virtualized environment
virtual_os_time = psutil.cpu_times().guest

# # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
virtual_cpu_time = psutil.cpu_times().guest_nice

# Print the fetched information
print("User time:", user_time)
print("Kernel time:", kernel_time)
print("Idle time:", idle_time)
print("Priority user time:", priority_user_time)
print("I/O wait time:", io_wait_time)
print("Hardware interrupt time:", hardware_interrupt_time)
print("Software interrupt time:", software_interrupt_time)
print("Virtual OS time:", virtual_os_time)
print("Virtual CPU time:", virtual_cpu_time)
