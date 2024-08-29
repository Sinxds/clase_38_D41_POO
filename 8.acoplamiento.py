class Motor:
    def encender(self):
        print("Encendiendo el motor")

class Motor2:
    def encender(self):
        print("Encendiendo el motor")
        
class Vehiculo:
    def __init__(self, motor):
        self.motor = motor

    def partir(self):
        self.motor.encender()
        print("Vehículo partiendo...")


motor1 = Motor()
motor2 = Motor2()

vehiculo1 = Vehiculo(motor1)
vehiculo2 = Vehiculo(motor2)


vehiculo1.partir()


###############

class Motor:
    def encender(self):
        print("Encendiendo el motor")

class Vehiculo:
    def __init__(self, motor):
        self.motor = Motor()

    def partir(self):
        self.motor.encender()
        print("Vehículo partiendo...")


vehiculo1 = Vehiculo(motor1)

vehiculo1.partir()