#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across range() to generate n UUIDs"""

# standard library import
# allows us to generate UUIDs
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4() )   # each time through the loop produce a UUID
