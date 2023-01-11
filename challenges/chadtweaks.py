#!/usr/bin/env python3
"""old mcdonald had a farm"""

import pyinputplus as pinp

farmnames= ["NE Farm", "W Farm", "SE Farm"]

choice= pinp.inputMenu(farmnames, numbered=True)

print(choice)
#print(farms.__len__())
# for ag in farms[choice]: 
#     print(ag)

