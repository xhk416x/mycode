#!/usr/bin/env python3
"""old mcdonald had a farm"""

import pyinputplus as pinp

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farmnames= []
farmnum= 0
farmcount= []

#adds numbered list to farmcount based on number of farms in farms
while farmnum < len(farms):
    farmcount.append(farmnum)
    farmnum += 1

for farm in farmcount:
    farmnames.append(farms[farm]["name"])

choice= pinp.inputMenu(farmnames, numbered=True)

print(choice)
