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

    print(dictlist[qcount]["question"])
    print(f"1. {dictlist[qcount]['1']}")
    print(f"2. {dictlist[qcount]['2']}")
    print(f"3. {dictlist[qcount]['3']}")
    print(f"4. {dictlist[qcount]['4']}")
    
    answer= input()
    #answer= int(answer)
    #evaluate answer
    if answer not in ["1","2","3","4"]:
        pass
        print("Not a valid response. Don't you want to go to Disney World??")
    #add counter
    else:
        if answer == "a":
                hs
        dictlist[qcount][answer -1] += 1
        qcount += 1




#loop 
#determine final results

print("Which Disney World park should you go to??")
while qcount <=3:
  main()
print(mk, ak, e, hs)
