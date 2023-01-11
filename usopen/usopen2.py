#!/usr/bin/env python3
## USOpen Tournament Switch Checker -- 2018.05.01

''' usopen.py
This script is being designed to provide the following automated tasks:
- ping check the router (import os)
- login check the router (import netmiko)
- determine if interfaces in use are up (import netmiko)
- Apply new configuration (import netmiko) # NEW

The IPs and device type should be made available via an Excel spreadsheet
'''

import os
import csv

import bootstrapper ## NEW

# python3 -m pip install netmiko
from netmiko import ConnectHandler

## retrieve data set from excel
def get_csv(fileloc):

    d= {} # start with an empty dictionary we will fill up

    with open(fileloc, "r") as foo:
        for row in csv.DictReader(foo):
            # first value of row == {'hostname': 'sw-1', 'driver': 'arista_eos'}
            keypair= {row['hostname']: row['driver']}
            # first value of keypair == {'sw-1': 'arista_eos'}
            d.update(keypair)

    return d # return the completed dictionary -> {'sw-1': 'arista_eos', 'sw-2': 'arista_eos'}

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    # if there were no errors with ping command, response = 0
    # if there WERE errors, response > 0
    if response == 0:
        return True

    else:
        return False


## Check interfaces - Issue "show ip int brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        # attempt to open a connection to this switch
        open_connection = ConnectHandler(device_type=dev_type,
                                         ip=dev_ip,
                                         username=dev_un,
                                         password=dev_pw)

        # send a command to the switch; record the ouput in "my_command" var
        my_command = open_connection.send_command("show ip int brief")

    except:
        # if an error occurs, the value of "my_command" will say it failed
        my_command = "** ISSUING COMMAND FAILED **"

    finally:
        # no matter what, this function will return "my_command"
        return my_command


## Login to router - SSH Check with Netmiko class ConnectHandler
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        # attempt to make a connection to the switch
        open_connection = ConnectHandler(device_type=dev_type,
                                         ip=dev_ip,
                                         username=dev_un,
                                         password=dev_pw)

        # if connection was made with no errors, function returns TRUE 
        return True

    except:
        # if error occurred while making connection, function returns FALSE
        return False

def main():

    # Determine where *.xls input is; 
    # note that pressing 'enter' without typing anything has a default value
    file_location = input("Host file location [Press ENTER for default: 'host_list.csv']\n>") or "host_list.csv"

    # "entry" is now a dictionary returned from get_csv() function above
    entry = get_csv(file_location)

    # Use a loop to check each device for SSH accessability
    print("\n***** BEGIN SSH CHECKING *****")
    for switchip in entry:
        if login_router(f"{entry[switchip]}",   # check if function returns TRUE or FALSE
                        switchip,
                        "admin",
                        "alta3"):

            # if function returned true, print connectivity is UP
            print("\n\t**HOST: - " + switchip + " - SSH connectivity UP\n")

        else:
            # if function returned false, print connectivity is DOWN
            print("\n\t**HOST: - " + switchip + " - SSH connectivity DOWN\n")

    # Use a loop to check each device for ICMP responses
    print("\n***** BEGIN ICMP CHECKING *****")
    for switchip in entry:
        if ping_router(switchip):             # check if function returns TRUE or FALSE
            # if func returned TRUE:
            print("\n\t**HOST: - " + switchip + " - responding to ICMP\n")

        else:
            # if func returned FALSE:
            print("\n\t**HOST: - " + switchip + " - NOT responding to ICMP\n")

                                              # Use a loop to check each device for ICMP responses
    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for switchip in entry:
        # pass values needed to make connection into interface_check() function
        # function will save its output to the "result" var
        result= interface_check(f"{entry[switchip]}",
                                switchip,
                                "admin",
                                "alta3")
        print("\n" + result)

    ## Determine if new config should be applied && if so apply new config
    print("\n***** NEW BOOTSTRAPPING CHECK *****")

    ynchk = input("\nWould you like to apply a new configuration? y/N \n>") or "n"

    if ynchk.lower() in ["y", "yes"]:
        conf_loc = input("\nEnter name of new config file. \n>")
        conf_ip = input("\nHostname of the device to be configured? \n>")

        if bootstrapper.bootstrapper(f"{entry[switchip]}",
                                     switchip,
                                     "admin",
                                     "alta3",
                                     conf_loc):

            # if function returns TRUE            
            print("\nNew configuration applied!")

        else:
            # if function returns FALSE (there was an error)
            print("\nProblem in applying new configuration!")

if __name__ == "__main__":
    main()
