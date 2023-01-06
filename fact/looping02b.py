#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")

# no need to close our file - closed automatically
