def saludar():
    print("Hola mundo!")    #<----- Esto no se hace porque limita la función


def saludar2():
    return "jaslsakjsa"



class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumen(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor} Cantidad de páginas: {self.paginas}"
    # Este metodo no debería pertenecer a esta clase. Deberia pertenecer a la clase carrito
    def agregar_al_carro(self):
        return f"Libro {self.titulo} agregado al carro"

libro1 = Libro("Nuevo libre", "Nuevo autor", 500)


libro1.autor  # 
            # comportamiento

def mostrar_mensaje_consola():


# principio de responsabildiad -> solid