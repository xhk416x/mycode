#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list[1]
    print(list1[1])

    list2= ["juniper"]

    list1.extend(list2)

    print(list1)

    list3= ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    list1.append(list3)

    print(list1) 

    print(list1[4][0]) 

main()
