class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola mi nombre es {self.nombre}"
    
class Perro(Animal):
    def __init__(self, nombre, pelaje):
        super().__init__(nombre)
        self.pelaje = pelaje

    def saludar(self):
        return f"¡Hey!, estoy disponible. Me llamo {self.nombre}, mucho gusto"
    
class Canario(Animal):
    def __init__(self, nombre, plumaje):
        super().__init__(nombre)
        self.plumaje = plumaje

    def saludar(self):
        return f"¡Hey!, estoy disponible. Me llamo {self.nombre}, mucho gusto"

pepito = Perro("Pepito", "Corto")


piolin = Canario("Piolín", "Largo")

piolin.plumaje


#DRY -> DONT REPEAT YOURSELF
#SOLID -> HACER UN CODIGO MANTENIBLE, ESCALABLE