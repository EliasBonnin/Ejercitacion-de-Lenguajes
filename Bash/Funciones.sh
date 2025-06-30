# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Funciones

#!/bin/bash

release_file=/etc/os-release
logfile=/var/log/updater.log
errorlog=/var/log/updater_errors.log

check_estado() {  # Creamos una funcion que representa el mostar el error si el estado no se cumple
    if [ $? -ne 0 ]
    then
        echo "Un error ocurrio, checkea archivo $errorlog"
    fi
}

if grep -q "Arch" $release_file
then
    # The host is based on Arch, run de pacman command
    sudo pacman -Syu 1>>$logfile 2>>$errorlog
    check_estado
fi

if grep -q "Pop" $release_file || grep -q "Ubuntu" $release_file
then
    # The host is based on Debian or Ubuntu
    # Run the apt version of the command
    sudo apt update 1>>$logfile 2>>$errorlog
    check_estado
    
    sudo apt dist-upgrade -y 1>>$logfile 2>>$errorlog
    check_estado
fi