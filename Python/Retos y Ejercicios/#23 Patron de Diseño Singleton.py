# Ejercicio 23
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

class Singleton:

    instancia = None

    def __new__(cls):
        if not cls.instancia:
            cls.instancia = super(Singleton, cls).__new__(cls)

        return cls.instancia


singletone = Singleton()
print(singletone)
singletone1 = Singleton()
print(singletone1)
