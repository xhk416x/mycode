# #!/usr/bin/env python3
# """This script installs 3rd party pip modules"""

# import pip
import importlib
def install_file(package: str):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "--no-index", "--find-links", "whlFolder", package], shell=True)
def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
        print("try")
    except ImportError:
        # pip.main(['install', package])
        install_file(package)
        print("except")
    # print("pre-return")
    # return importlib.import_module(package)

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
