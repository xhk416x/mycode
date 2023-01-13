# #!/usr/bin/env python3
# """This script installs 3rd party pip modules from a file called 'dependencies.txt' """

import importlib
import os
import pip

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])

if __name__ == '__main__':
    os.system("sudo apt update && sudo apt install python3-pip ansible -y")
    with open("dependencies.txt", "r") as foo:
        mods = []
        for line in foo:
            modname= line.strip("\n")
            mods.append(modname)
            import_with_auto_install(modname)
