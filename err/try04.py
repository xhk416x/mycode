#!/usr/bin/python3
"""try except else and finally | Alta3 Research"""

# python standard library
import uuid

# generate a UUID based on the host id, sequence number, and current time
# simulating a ticketed job number
ticket = uuid.uuid1()

try: # try to do this
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()
except: # if any errors occurred
    x = 'General error with obtaining configuration file!'
else: # if there were no errors
    x = 'Switch config file found.'
finally: # in all cases, write out what happened to a log file
    with open("try04.log", "a") as zlog:
        print('\n\nWriting results of routine to log file')
        print(ticket, " - ", x, file=zlog)
