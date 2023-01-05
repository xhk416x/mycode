#!/usr/bin/env python3
"""Script to determine which Disney park a user should visit"""
#Variables
hs = 0
mk = 0
e = 0
ak = 0

whyq= {
        "question" : "Why are you going to disney?",
        "1" :"Rides",
        "2": "Characters",
        "3" : "Food",
        "4" : "Not sure???",
}
dressupq= {
        "question" : "If you had to dress up as a Disney character, which of the following most applies to you?",
        "1" : "Pixar Character",
        "2" : "Prince/Princess",
        "3" : "What are you talking about? I just came here for the food.",
        "4" : "A Navi (Avatar)",
}
souvenirq= {
        "question" : "What souvenir are you most likely to buy?",
        "1" : "LightSaber",
        "2" : "Mickey Ears",
        "3" : "PINS! Time to get trading!",
        "4" : "Stuffed Animal",
}
rideq= {
        "question" : "Which ride are you most excited to ride?",
        "1" : "Rise of the Resistance",
        "2" : "Space Mountain",
        "3" : "Frozen Ever After",
        "4" : "Flight of Passage",
}
parklist= [hs, mk, e, ak]
dictlist = [whyq, dressupq, souvenirq, rideq]
qcount = 0

def main():
#ask question
    global qcount
    global hs
    global mk
    global e
    global ak

    print(dictlist[qcount]["question"])
    print(f"A. {dictlist[qcount]['1']}")
    print(f"B. {dictlist[qcount]['2']}")
    print(f"C. {dictlist[qcount]['3']}")
    print(f"D. {dictlist[qcount]['4']}")
    
    answer= input(">>> ")
    answer= answer.lower()
    #evaluate answer
    if answer not in ["a", "b", "c", "d"]:
        print("Not a valid response. Don't you want to go to Disney World??")
    #add counter
    else:
        if answer == "a":
            hs += 1
            qcount += 1
        elif answer == "b":
            mk += 1
            qcount += 1
        elif answer == "c":
            e += 1
            qcount += 1
        elif answer == "d":
            ak += 1
            qcount += 1
    

#loop 
#determine final results

print("Which Disney World park should you go to??")
while qcount <=3:
    main()

if mk > ak and mk > e and mk > hs:
    print("You should go to the Magic Kindgom!")
elif ak > mk and ak > e and ak > hs:
    print("You should go to the Animal Kindgom!")
elif e > mk and e > ak and e > hs:
    print("You should go to Epcot!")  
elif hs > mk and hs > e and hs > ak:
    print("You should go to Hollywood Studios!")
else:
    print("It looks like you don't have a clear preference. You should start at Epcot for the great food.")
