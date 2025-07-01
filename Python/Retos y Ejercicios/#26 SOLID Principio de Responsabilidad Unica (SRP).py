# Ejercicio 25
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# SRP

# Manera Incorrecta

class Usuario:  # Al tener responsabilidad de guardado y email, al cambiar una de ellas afectaria la clase

    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email

    def guardar_usuario(self):
        pass

    def enviar_email(self):
        pass


# Manera Correcta

class Usuarios:

    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email


class UsuarioRepo:

    def guardar_usuario(self, user):
        pass


class EmailServicio:

    def enviar_email(self, email, mensaje):
        pass
