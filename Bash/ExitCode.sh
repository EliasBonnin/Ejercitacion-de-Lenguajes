# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Exit Code

#!/bin/bash

package=htop

sudo apt install $package  >> package_install_results.log

if [ $? -eq 0 ]
then
    echo "La instalacion de $package fue exitosa"
    echo "Nuevo comando:"
    which $package
else
    echo "La instalacon de $package no fue exitosa"
fi 
