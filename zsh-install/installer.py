#!/usr/bin/env python3
"""This installer is for installing zsh with oh-my-zsh 
and will include dependency checks and minor customization options
|| Wes Pritchard
"""

####gathering modules
import packagemanager_check as pm_check
import pip
import importlib
#import ansible_runner
##download needed non-builtin modules
def import_3rd_party(package):
    try:
        importlib.__import__(package)
        print("Successfully imported", package)
    except ImportError:
        pip.main(['install', package])

def is_ansible():
    try:
        ansible = os.system("which ansible > /dev/null")
        if ansible == 0:
            print("Ansible is already installed yay!")
        else:
            package = pm_check()
            os.system(f"sudo {package} install ansible -y")
    except:
        print("Uh oh. Spaghetti-o.")

####add customizations
#edit .zshrc to include updated ~/bin PATH
#edit .zshrc to edit default theme
#edit .zshrc to include custom plugins
#download selected plugins
#source .zshrc

### MUST run before defining main()
import_3rd_party(package="ansible_runner")
import ansible_runner
# Needed for packagemanager_check
import_3rd_party(package="distro")

def main():

    pkg_m = pm_check.packagemanager_check()
    playbookpath = f'/home/student/mycode/zsh-install/project/{pkg_m}playbook.yaml'

    if pkg_m == "apt":
        r= ansible_runner.run(playbook=playbookpath, private_data_dir=".")
        print("{}: {}".format(r.status, r.rc))

    elif pkg_m == "yum":
        r= ansible_runner.run(playbook=playbookpath, private_data_dir=".")
        print("{}: {}".format(r.status, r.rc))

    elif pkg_m == "dnf":
        r= ansible_runner.run(playbook=playbookpath, private_data_dir=".")
        print("{}: {}".format(r.status, r.rc))

    else:
        print("Sorry, looks like your distro might not be supported.")

if __name__ == "__main__":
    main()