import pip
import importlib

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    return importlib.import_module(package)


if __name__ == '__main__':
    with open("dependencies.txt", "r") as foo:
        for line in foo:
            modname= line.strip("\n")
            ok= import_with_auto_install(modname)
    ok.run()    

    # this works... the variable "ok" is now the module object
    # this means there can only be one module with this setup, but this is cool
