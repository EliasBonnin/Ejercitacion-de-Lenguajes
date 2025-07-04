# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Scheduling Jobs (CRON)

#!/bin/bash

logfile=job_results.log

/usr/bin/echo "The script se ejecuto en esta Fecha y Hora $(/usr/bin/date)" > $logfile

# Para acceder a cron usamos el comando "crontab -e"
# Esto nos abre un editor de texto (vscode) para poder empezar a utilizar cron
# El formato que debe seguir es el siguiente m h  dom mon dow command
    # m -> Minuto -- h -> Hora -- dom -> Dia del mes -- mon -> Mes -- dow -> Dia de la Semana -- command -> Comando a ejecutar
    # Ejemplo: 30 1 * * 5 ./Script
    # Minuto 30 - Hora 1 - Dia cualquiera - Mes Cualquiera - Dia 5 (Viernes) - Path del Script

rm $logfile