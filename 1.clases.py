numero = 5


print(type(numero))

cadena = "cadena"

print(type(cadena))

lista = [1,2,3,4]

print(type(lista))



# Por convención las clases comienzan con letra Mayúscula inicial
# *self* es una representación de la misma clase
class Animal:
    def __init__(self, nombre, raza, especie, disponible = True):
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        self.disponible = disponible

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, estoy disponible para adopción"
        

perro_pepito = Animal("Pepito", "Pastor Alemán", "Perro")
gato_juanito = Animal("Juanito", "Pelo corto", "Gato")

print(perro_pepito)
print(type(perro_pepito))

print(perro_pepito.nombre)
print(gato_juanito.nombre)

perro_pepito.nombre = "Pepín"

print(perro_pepito)

print(perro_pepito.saludar())

def c_status():
    c_nombre = input
    n_status = input("ingrese status de la mascota")
    if n_status == "disponible":
        Animal.disponible == True
    else:
         Animal.disponible == False

def saludar(self):
        if self.adoptar:
            return f"hola mi nombre es {self.nombre}, soy un {self.especie} {self.raza} de color {self.color}, y estoy disponibre para adopcion"
        else:
            return f"hola mi nombre es {self.nombre}, soy un {self.especie} {self.raza} de color {self.color}, y estoy feliz con la familia que me adopto"
        

c_status