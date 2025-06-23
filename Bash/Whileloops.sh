# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# While Loops

#!/bin/bash

myvar=1

while [ $myvar -le 5 ]
do
    echo $myvar
    myvar=$((myvar +1 ))
    sleep 0.5
done

sleep 1
clear

while [ -f ~/testfile  ]
do
    echo "En la $(date), el archivo existe"
    sleep 5
done

echo  "En la $(date), el archivo no existe.  Saliendo."