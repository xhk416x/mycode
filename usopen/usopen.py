#!/usr/bin/env python3
## USOpen Tournament Switch Checker -- 2018.05.01
''' usopen.py
This script is being designed to provide the following automated tasks:
- ping check the router (import os)
- login check the router (import netmiko)
- determine if interfaces in use are up (import netmiko)
- Apply new configuration (import netmiko) # not yet built

The IPs and device type should be made available via an Excel spreadsheet

'''
import os

## pyexcel and pyexce-xls are required for our program to execute
# python3 -m pip install --user pyexcel
# python3 -m pip install --user pyexcel-xls
import pyexcel

# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

## retrieve data set from excel
def retv_excel(par):
    d = {}
    # create a record object that is an open excel sheet
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        # adds a new hostname and driver key:value pair to our dictionary
        d.update( { record['hostname'] : record['driver'] } )
    return d # return the completed dictionary

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False


## Check interfaces - Issue "show ip int brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, \
          username=dev_un, password=dev_pw)
        my_command = open_connection.send_command("show ip int brief")       
    except:
        my_command = "** ISSUING COMMAND FAILED **"
    finally:
        return my_command


## Login to router - SSH Check with Netmiko class ConnectHandler
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, \
          username=dev_un, password=dev_pw)
        return True        
    except:
        return False

## Main function - This is the code that runs our functions
def main():

    ## Determine where *.xls input is
    file_location = input("\nWhat is the file you'd like to use? ")

    ## Entry is now a local dictionary containing hostname(key):driver(value)
    entry = retv_excel(file_location)

    ## Use a loop to check each device for SSH accessability
    print("\n***** BEGIN SSH CHECKING *****")
    for x in entry.keys():
        if login_router(str(entry[x]), x, "admin", "alta3"):
            print("\n\t**HOST: - " + x + " - SSH connectivity UP\n")
        else:
            print("\n\t**HOST: - " + x + " - SSH connectivity DOWN\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN ICMP CHECKING *****")
    for x in entry.keys():
        if ping_router(x):
            print("\n\t**HOST: - " + x + " - responding to ICMP\n")
        else:
            print("\n\t**HOST: - " + x + " - NOT responding to ICMP\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for x in entry.keys():
        print("\n" + interface_check(str(entry[x]), x, "admin", "alta3"))

## Call main()
main()