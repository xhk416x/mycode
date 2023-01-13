# #!/usr/bin/env python3
# """This script installs 3rd party pip modules"""

import importlib
import os

def install_file(package: str):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", package], shell=False)

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
        print("try")
    except ImportError:
        # pip.main(['install', package])
        print("******************pre-install***************")
        install_file(package)
        print("******************post-install***************")
    print("pre-return")
    return importlib.import_module(package)

if __name__ == '__main__':
    os.system("sudo apt update && sudo apt install python3-pip ansible -y")
    with open("dependencies.txt", "r") as foo:
        mods = []
        for line in foo:
            modname= line.strip("\n")
            mods.append(modname)
            import_with_auto_install(modname)