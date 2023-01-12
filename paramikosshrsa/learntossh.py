#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Issuing commands across a SSH channel"""

import os

## import paramiko so we can talk SSH
import paramiko

## shortcut issuing commands to remote
def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

    ############# IF YOU WANT TO CONNECT USING UN/PW ################
    #sshsession.connect(server, username=username, password=password)
    ############## IF USING KEYS ####################################

    ## mykey is our private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ## if we never went to this SSH host, add the fingerprint to the known host file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ## creds to connect
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    ## a simple list of commands to issue across our connection
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    ## cycle through our commands and issue them on the far end
    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))

main()
