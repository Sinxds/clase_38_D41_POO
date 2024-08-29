class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self.__saldo = saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")


cuenta_pepito = CuentaBancaria("Pepito")


cuenta_pepito.__saldo = 6000000000000000
