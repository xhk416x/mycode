#!/usr/bin/python3
## Try a real world test with getpass

## import Paramiko so we can talk SSH
import paramiko # allows Python to ssh
import os # low level operating system commands
import getpass # we need this to accept passwords

def movethemfiles(dir, dest, conn):
    ## iterate across the files within directory
    for x in os.listdir(dir): # iterate on directory contents
      if not os.path.isdir(dir+x): # filter everything that is NOT a directory
        print(dir + x)
        print(dest + x)
        conn.put(dir+x, dest+x) # move file to target location


def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port of bender
    
    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password=getpass.getpass()) # notice the password references getpass
    
    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    # ## copy our firstpasswd.py script to bender
    # sftp.put("file_to_move.txt", "file_to_move.txt") # move file to target location home directory
    
    #try:
    dir= input("Choose a source for files to be sent")
    dest= input("Choose a destination for the files")
    ##move them files
    movethemfiles(dir, dest, sftp)
    #except:
    #    print("Oops, something wasn't right about that.")

    ## close the connection
    sftp.close() # close the connection
if __name__ == "__main__":
    main()
