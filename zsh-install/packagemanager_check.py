#!/usr/bin/env python3
"""check for dnf or apt"""

import os

def packagemanager_check():
    try:
        apt = os.system("which apt > /dev/null")
        dnf = os.system("which dnf > /dev/null")
        yum = os.system("which yum > /dev/null")
        pacman = os.system("which pacman > /dev/null")
        if apt == 0:
            return "apt"
        elif dnf == 0:
            return "dnf"
        elif yum == 0:
            return "yum"
        elif pacman == 0:
            return "pacman"
    except:
        print("Uh oh. Spaghetti-o.")

if __name__ == "__main__":
    main()