# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Exit Code Ejemplo 2

#!/bin/bash


directorio=/etc

if [ -d $directorio ]
then
    echo "El directorio $directorio existe."
    exit 0
else
    echo "El directorio $directorio no existe."
    exit 1
fi

echo "El exit code para este script un es: $?"
