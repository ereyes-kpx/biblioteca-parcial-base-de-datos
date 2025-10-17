class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id_usuario = id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_id_usuario(self):
        return self.__id_usuario

    def __str__(self):
        return f"Usuario: {self.__nombre} (ID: {self.__id_usuario})"