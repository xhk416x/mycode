#!/bin/bash

sudo apt update && sudo apt install python3-pip -y && sudo apt install ansible -y

sleep 1.5

echo -e '\n**************************************************\n'

python3 installer.py