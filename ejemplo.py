class Animal:
    def __init__(self, nombre, especie, raza, color, disponible = True):
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        self.color = color
        self.disponible = disponible
    
    def saludar(self):
        if self.disponible:
            return f"hola mi nombre es {self.nombre}, soy un {self.especie} {self.raza} de color {self.color}, y estoy disponibre para adopcion"
        else:
            return f"hola mi nombre es {self.nombre}, soy un {self.especie} {self.raza} de color {self.color}, y estoy feliz con la familia que me adopto"
        
    def adoptar(self):
        if self.disponible:
            self.disponible = False
        else:
            self.disponible = True
 
perrp_pepito = Animal("pepito", "perro", "paston aleman", "gris/negro")
gato_juanito = Animal("juanito", "gato", "angora", "blanco")

print(perrp_pepito.nombre)
print(gato_juanito.nombre)
 
perrp_pepito.nombre = "Pepin"
 
print(perrp_pepito.nombre)
 
print(gato_juanito.saludar())
 
gato_juanito.adoptar()
print()
 
print(gato_juanito.saludar())
 
gato_juanito.adoptar()
print()
print(gato_juanito.saludar())