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

# Extras


class Usuario_Sesion:

    instancia = None

    id = str = None
    nombre_usuario = str = None
    nombre = str = None
    email = str = None

    def __new__(cls):
        if not cls.instancia:
            cls.instancia = super(Usuario_Sesion, cls).__new__(cls)

        return cls.instancia

    def set_usuario(self, id, nombre_usuario, nombre, email):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.nombre = nombre
        self.email = email

    def get_usuario(self):
        return print(f"{self.id}, {self.nombre_usuario}, {self.nombre}, {self.email}")

    def borrar_usuario(self):
        self.id = None
        self.nombre_usuario = None
        self.nombre = None
        self.email = None


Sesion1 = Usuario_Sesion()
Sesion1.set_usuario(1, "pedrito", "elias", "carlostrinidad@gmail.com")
print(Sesion1.get_usuario())


Sesion2 = Usuario_Sesion()
print(Sesion2.get_usuario())

Sesion3 = Usuario_Sesion()
print(Sesion3.borrar_usuario())
print(Sesion3.get_usuario())
