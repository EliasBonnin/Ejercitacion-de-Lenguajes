# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# For Loops

#!/bin/bash

for i in {1..5}
do
    echo $i
    sleep 0.5
done

echo "Se termino el loop for, estamos afuera"
sleep 0.5
clear

for file in ~/logfiles/*.log  # Busca los archivos en logiles, y que estos terminen .log
do
    tar -czvf $file.tar.gz $file # crea un file compressed 
done

