from pagos.Pago import Pago
class Transferencia(Pago):
    def __init__(self):
        self.__numCuenta=""
        self.__cedula=""
        self.__beneficiario=""
        self.__concepto=""
    def transaccion(self):
        self.__numCuenta = input("ingrese numero de cuenta: ")
        self.__beneficiario=input("ingrese nombre completo del benefiiario")
        self.__cedula = input("ingrese cedula: ")
        self.__concepto = input("ingrese cocepto: ")
        print("transferencia exitosa")
        print(f"banco beneficiario: {self.__beneficiario}")
        print(f"cedula: {self.__cedula}")
        print(f"numero de cuenta: {self.__numCuenta}")
        print(f"concepto: {self.__concepto}")