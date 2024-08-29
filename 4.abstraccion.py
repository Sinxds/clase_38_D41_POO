lista = [4,5,3,67,3,2,1]

lista.sort(reverse=True) #*SORT* es un comportamiento de la lista

print(lista)

print(type(lista))

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self._saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self._saldo}")


cuenta_pepito = CuentaBancaria("Pepito")

cuenta_pepito.mostrar_saldo()

cuenta_pepito.depositar(6000)

cuenta_pepito.retirar(5000)

cuenta_pepito._saldo = 5000000
print(cuenta_pepito._saldo)