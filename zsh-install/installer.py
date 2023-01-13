#!/usr/bin/env python3
"""This installer is for installing zsh with oh-my-zsh 
and will include dependency checks and minor customization options
|| Wes Pritchard
"""

#### gathering modules
import packagemanager_check as pm_check
import importlib
import os
## pull in env variables
HOME = os.getenv('HOME')
PWD = os.getcwd()
#### install prereqs
os.system("sudo apt update && sudo apt install python3-pip ansible -y")
### pip now added
import pip
## below will download all pip modules in dependencies.txt
import py_mod_deps
## after py_mod_deps installs modules, this will import them  
with open(f"{PWD}/dependencies.txt", "r") as deplist:
    mods = []
    for line in deplist:
        modname= line.strip("\n")
        mods.append(modname)
        modname= py_mod_deps.import_with_auto_install(modname)
    for mod in mods:
        globals()[mod] = importlib.import_module(mod)
    for mod in mods:
        globals()[mod] = importlib.import_module(mod)

def main():

    supported_pkgm = ["apt", "yum", "dnf"]
    #is_ansible()
    pkg_m = pm_check.packagemanager_check()
    #### arg it up here vvvv
    playbookpath = f'{PWD}/project/{pkg_m}playbook.yaml'

    if pkg_m in supported_pkgm:
        ansible_runner.run_command(
            executable_cmd='ansible-playbook',
            cmdline_args=[playbookpath, '--ask-become-pass'],
            host_cwd=PWD,
        )
    else:
        print("Sorry, looks like your distro might not be supported.")

####add customizations
#edit .zshrc to include updated ~/bin PATH
#edit .zshrc to edit default theme
#download selected plugins
#source .zshrc

if __name__ == "__main__":
    main()