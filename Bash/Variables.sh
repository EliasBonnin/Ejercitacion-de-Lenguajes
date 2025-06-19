# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Variables

#!/bin/bash

nombre="Elias"  # Declaramos la variable
edad="26"
Directorio=$(ls) # Guardamos el resultado el ls dentro de una variable
hoy=$(date) # Nos guarda la fecha y hora en el momento donde ejecutamos el script

echo "Hola, Mi nombre es: $nombre."
echo "Tengo $edad."
echo "El username es: $USER"
echo $hoy
