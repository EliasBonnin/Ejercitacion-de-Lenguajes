# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Instalar Package "htop"

#!/bin/bash

comando=htop #Path de htop si estuviera instalado

if command -v $comando # Verificamos si esta instalado htop
then
    echo "$comando existe!"
else
    echo "$comando no existe, instalandolo..."
    sudo apt update && sudo apt install -y $comando  
fi

$comando

    # && Anida los comandos
    # -y No me preguntes si quiero o no solo hacelo