# Ejercicio 25
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Logs

import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s ",
    handlers=[logging.StreamHandler()])

logging.debug("Mensaje de DEBUG")

logging.info("Mensaje de informacion (INFO)")  # Esta funcionando correctamente

logging.warning("Mensaje de WARNING")  # Algo que no esperabamos sucedio

logging.error("Esto es un ERROR")  # Indica un error mas grave

logging.critical("Esto es un error CRITICAL\n")  # El error es demasiado grave


# Extra

class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, nombre: str, descripcion: str):
        tiempo_inicio = time.time()
        if nombre not in self.tasks:
            self.tasks[nombre] = descripcion
            logging.info(f" Tarea Agregada: {nombre}.")
        else:
            logging.warning(f"Se ha intentado agregar una tarea que ya existe {nombre}.")
        tiempo_fin = time.time()
        self._print_time(tiempo_inicio, tiempo_fin)

    def del_task(self, nombre: str):
        tiempo_inicio = time.time()
        if nombre in self.tasks:
            del self.tasks[nombre]
            logging.info(f"Se ha eliminado la tarea correctamente {nombre}.")
        else:
            logging.error(f"Se esta intentando eliminar una tarea que no existe, {nombre}.")
        tiempo_fin = time.time()
        self._print_time(tiempo_inicio, tiempo_fin)

    def list_tasks(self):
        tiempo_inicio = time.time()
        if self.tasks:
            logging.info("Se va a imprimir la lista de tareas.")
            for nombre, descripcion in self.tasks.items():
                print(f"{nombre}, {descripcion}")
        else:
            logging.info("No existen tareas")
        tiempo_fin = time.time()
        self._print_time(tiempo_inicio, tiempo_fin)

    def _print_time(tiempo_inicio, tiempo_fin):
        logging.debug(f"Tiempo de ejecucion {tiempo_fin - tiempo_inicio} segundos.")


tareas = TaskManager()

tareas.add_task("Pan", "Comprar pan duro")
tareas.add_task("Bash", "Estudiar Bash")
tareas.add_task("Bash", "Estudiar Bash")
tareas.list_tasks()
tareas.del_task("Bash")
tareas.del_task("Bash")
tareas.list_tasks()
