#!/usr/bin/python3

mylist= [1,"2",3,4,5, "Python"]

name= input("What is your name?\n")

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

name= name.capitalize()

#edited to use f-string
#print("Hi " + name + "! Welcome to Day " + mylist[1] + " of " + mylist[5] + " Training!")
print(f"Hi {name}! Welcome to Day {mylist[1]} of {mylist[5]} Training!")
