from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads
import sys

# saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# verifying the validity of each ip address in the list
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Calling threads creation function for one or multiple ssh connections
create_threads(ip_list, ssh_connection)