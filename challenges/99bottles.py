"""99 bottles of beer for loop"""

import time

try:
    bottles = input("How many bottles do you have on your wall? (No more than 100 please)\n")
    bottles = int(bottles)
    if bottles > 100:
        print("Whoa there, you don't have that many bottles on your wall.")
    elif bottles > 0 < 100:
        for count in range(-1,bottles):
            print(f"{bottles} of beer on the wall!! {bottles} of beeeeeer!")
            print(f"Take one down, pass it around. {bottles} of beer on the wall.")
            bottles -= 1           
except:
    print(f"That wasn't a number! I can't count down from {bottles}")

    
