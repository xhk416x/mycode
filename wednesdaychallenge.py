#!/usr/bin/python3

number= 2

name= input("What is your name?\n")

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

name= name.capitalize()

#edited to use f-string
#print("Hi " + name + "! Welcome to Day " + mylist[1] + " of " + mylist[5] + " Training!")
print(f"Hi {name}! Welcome to Day {number} of Python Training!")

#import protection. Will not run main() unless file is run directly
if __name__ == "__main__":
    main()
