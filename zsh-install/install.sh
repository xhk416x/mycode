#!/bin/bash

sudo apt update && sudo apt install python3-pip ansible -y

sleep 1.5

echo -e '\n**************************************************\n'

sleep 1.5

python3 installer.py