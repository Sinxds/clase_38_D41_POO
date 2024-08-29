def saludar():
    print("Hola mundo 1")   # Cada vez que ejecutamos funciones que sean igual, la primera se pierde

def saludar():
    print("Hola mundo 2")   # La segunda es la que prevalece



saludar()  # resultado -> Hola Mundo 2


class Perro():
    def hablar(self):
        print("Guau")
        

class Gato():
    def hablar(self):
        print("Meow")

class Canario():
    def hablar(self):
        print("Pio pio")


perro = Perro()
gato = Gato()
canario = Canario()


perro.hablar()



animales = [perro, gato, canario]


for animal in animales:
    animal.hablar()