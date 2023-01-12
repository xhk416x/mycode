#!/usr/bin/env python3
"""This installer is for installing zsh with oh-my-zsh 
and will include dependency checks and minor customization options
|| Wes Pritchard
"""

####gathering modules
#import platform
#import os
#import subprocess
import distro
import ansible_runner as a_run

####distro data. needs be in a separate file **future
debian= ["debian", "ubuntu", "mint"]
rhel= ["rhel", "fedora"]

#check for os 
def distrocheck():
    if distro.id() in debian or distro.like() in debian:
        print("Debian-like detected. Using apt.")
        return "debian"
    elif distro.id() in rhel or distro.like() in rhel:
        print("Sorry, not supported yet")
        return "rhel"

####install dependencies
def deb_deps():
    playbookpath= "./playbooks/debplaybook.yaml"
    r= a_run.run(playbook=playbookpath, private_data_dir=".")
    print("{}: {}".format(r.status, r.rc))

def rhel_deps():
    playbookpath= "./playbooks/rhelplaybook.yaml"
    r= a_run.run(playbook=playbookpath, private_data_dir=".")
    print("{}: {}".format(r.status, r.rc))

#sudo apt update
#sudo apt install -y zsh fonts-powerline

####add customizations
#edit .zshrc to include updated ~/bin PATH
#edit .zshrc to edit default theme
#edit .zshrc to include custom plugins
#download selected plugins
#source .zshrc

def main():
    if distrocheck() == debian:
        deb_deps()


if __name__ == "__main__":
    main()