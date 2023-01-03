#!/usr/bin/env python3
"""Asks what the users name and day of the week it is. Then prints hello message"""

#Define the chal13 function
def chal13():
    #Saves user input as NAME
    NAME = input("Please tell me your name: ")
    #Saves user input as DOW (day of week)
    DOW = input("Also, what is the day of the week today?")
    #print("Hello, ", NAME, "!", " Happy ", DOW, "!", sep="")
    print(f"Hello, {NAME}! Happy {DOW}!")
#Calls chal13 function
chal13()
