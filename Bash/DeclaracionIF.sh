# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Declaraciones "if"

#!/bin/bash

mynum="300"

if [ $mynum -eq 200 ] # -eq significa igual (=)
then
    echo "La condicion es TRUE"
else
    echo "La variable no es 200"
fi

if [ ! $mynum -eq 200 ] # ! niega la condicion haciendo que NO sea igual
then
    echo "La condicion es TRUE"
else
    echo "La variable no es 200"
fi

if [ $mynum -ne 200 ] # -ne quiere decir NO ES IGUAL (!=)
then
    echo "La condicion es TRUE"
fi

if [ -f ~/myfile ]  # f Checkea un archivo
then
    echo "El archivo existe"
else
    echo "El archivo no existe"
fi