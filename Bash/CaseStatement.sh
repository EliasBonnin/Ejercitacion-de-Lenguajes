# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Case Statement

#!/bin/bash

echo "Cual es tu distribucion de linux favorita?"

echo "1 - Arch"
echo "2 - CentOS"
echo "3 - Debian"
echo "4 - Mint"
echo "5 - Ubuntu"
echo "6 - Otro...\n"

read distro;

case $distro in 
    1) echo "Arch is rolling release.";;
    2) echo "CentOS is a popular server." ;;
    3) echo "Debian is a community distribution." ;;
    4) echo "Mint is a popular on desktops and laptops." ;;
    5) echo "Ubuntu is popular on both servers and computers.";;
    6) echo "There are many distributions out there.";;
    *) echo "No se eligio una opcion correcta."
esac
