class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre.upper()
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            print("Modificando el valor")
            self.__nombre = nuevo_nombre.capitalize()
        else:
            print("Error está vacío")
            
carlitos = Persona("Carlos Oviedo")

carlitos.nombre = "pedro"

print(carlitos.nombre)