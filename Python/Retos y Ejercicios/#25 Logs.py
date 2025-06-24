# Ejercicio 25
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Logs

import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s ",
    handlers=[logging.StreamHandler()])

logging.debug("Mensaje de DEBUG")

logging.info("Mensaje de informacion (INFO)")  # Esta funcionando correctamente

logging.warning("Mensaje de WARNING")  # Algo que no esperabamos sucedio

logging.error("Esto es un ERROR")  # Indica un error mas grave

logging.critical("Esto es un error CRITICAL")  # El error es demasiado grave
