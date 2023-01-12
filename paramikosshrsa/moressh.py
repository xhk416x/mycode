#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko
import csv

## retrieve data set from excel
def get_csv(fileloc):

    d= [] # start with an empty list we will fill up

    with open(fileloc, "r") as host_list:
        for row in csv.DictReader(host_list):
            # first value of row == {'user': 'bender', 'ip': '10.10.2.3'}
            # here's the issue-- keypair needs to be a key and a value, but this is just one long string
            keypair= {"user": row["user"], "ip": row["ip"]}
            # first value of keypair == {'sw-1': 'arista_eos'}
            d.append(keypair)

    return d # return the completed dictionary -> {'sw-1': 'arista_eos', 'sw-2': 'arista_eos'}


def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = []
    try:
        fileloc = input("Where is the connection file located?") or "creds.csv"
        credz = get_csv(fileloc)
        print(credz)
    except:
        print("That file doesn't seem quite right. Try again.")
        exit()

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection credz
    for cred in credz:
        
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("user") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("user"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("user") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("user"))

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()
