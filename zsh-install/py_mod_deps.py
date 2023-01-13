# #!/usr/bin/env python3
# """This script installs 3rd party pip modules"""

import pip
import importlib

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    return importlib.import_module(package)
    
    # with open("dependencies.txt", "r") as foo:
    #     mods = []
    #     for line in foo:
    #         modname= line.strip("\n")
    #         mods.append(modname)
    #         modname= import_with_auto_install(modname)
    #     for mod in mods:
    #         globals()[mod] = importlib.import_module(mod)

if __name__ == '__main__':
    with open("dependencies.txt", "r") as foo:
        mods = []
        for line in foo:
            modname= line.strip("\n")
            mods.append(modname)
            modname= import_with_auto_install(modname)
        print(mods)
        for mod in mods:
            globals()[mod] = importlib.import_module(mod)
        print(globals())
        ansible_runner.run()
