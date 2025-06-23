# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Ejemplos de Exit Code

#!/bin/bash

directorio=/noexiste

if [ -d $directorio ]
then
    echo $?
    echo "El directorio $directorio existe."
else
    echo $?
    echo "El directorio $directorio no existe."
fi

echo "El exit code para este script un es: $?"

