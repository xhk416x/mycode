#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:    # we never created a list of lines to store in memory
        #print and end without a newline
        print(svr, end="")

# no need to close our file - closed automatically
