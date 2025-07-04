# Ejercicios de Bash
# Videos de la serie: de Learn Linux TV "Bash Scripting for Beginners"

# Scheduling Jobs

#!/bin/bash

logfile=job_results.log

echo "The script se ejecuto en esta Fecha y Hora $(date)" > $logfile

# Se puede ejecutar usando el comando at
# Ejemplo
    # at 15:30 -y -f ./SchedulingJobs
    # Este comando se ejecutara al hora establecida ya que no le especificamos una fecha.
    # at 15:30 081624 -y -f ./SchedulingJobs (Mes-Dia-Anio)
    # Podemos agregar una fecha para los comandos se ejecuten en esa fecha.
# Con el comando "atq" Podemos ver la lista de comandos para ejecutarse.
# Con el comando "atrm (Numero de referncia)" podemos remover los comandos.

rm $logfile