# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Security Backup

#!/bin/bash

# Check to make sure the user entered exactly two arguments.
if [ $# -ne 2 ] 
then
    echo "Usage: Backup.sh <source_directory> <target_directory>"
    echo "Please try again."
    exit 1
fi

# Check to see if rsync is installed
if ! command -v rsync > /dev/null 2>&1 
    # Usamos command -v para ver si tenemos rsync instalado en el sistema.
    # La ultima parte al no querer saber el contenido, lo que hacemos es mandarlo a dev/null 
then
    echo "The script requires rsync to be installed."
    echo "Please use your distribution's package manager to install it and try again."
    exit 2
fi

# Capture the current date, and store in the format: YYYY-MM-DD
current_date=$(date +%Y-%m-%d) 
#Creamos una variable con un formato especifico. En este caso la salida de date

rsync_options="-avb --backup-dir $2/current_date --delete"
# Son los comandos que pondriamos manaualmente en un rsync


$(which rsync) $rsync_options $1 $2/current >> backup_$current_date.log