# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Universal Update

#!/bin/bash

release_file=/etc/os-release

if grep -q "Arch" $release_file
then
    # The host is based on Arch, run de pacman command
    sudo pacman -Syu
fi

if grep -q "Pop" $release_file || grep -q "Ubuntu" $release_file
then
    # The host is based on Debian or Ubuntu
    # Run the apt version of the command
    sudo apt update
    sudo apt dist-upgrade
fi

