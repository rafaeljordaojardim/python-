import paramiko
import os.path
import time
import sys
import re

# checking username/password file
# Prompting user for input - USERNAME/PASSWORD FILE

user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

# verifying the validity of the USERNAME/PASSWORD FILE
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

# Checking commands file
# Prompting user for input - COMMANDS FILE
cmd_file = input("\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

# Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :) \n")
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()

# open SSHv2 connection to the device
def ssh_connection(ip):

    global user_file
    global cmd_file

    # creating SSH CONNECTION
    try:
        # DEFINE SSH PARAMETERS
        selected_user_file = open(user_file, "r")

        # starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the username from the file
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

         # starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading password
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n") 

        # login into devide
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys
        # do not use in production! The default would be rejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # connect to the devide using username and password
        session.connect(ip.rstrip("\n"), username = username, password = password)

        # Start an interactuve shell session on the router
        connection = session.invoke_shell()

        # seting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        # starting from the beginning of the file
        selected_cmd_file.seek(0)

        # Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        # closing the user file
        selected_user_file.close()

        # closing cmd file
        selected_cmd_file.close()

        # checking command output for IOS syntax erros
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at leat one IOS syntax error on the device {} :(".format(ip))
        else:
            print("\n DONE for device {} :)\n".format(ip))

        # test for reading command output
        print(str(router_output)+"\n")

        #closing the connection
        session.close()
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")