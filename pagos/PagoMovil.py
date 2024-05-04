from pagos.Pago import Pago
''''clase que realiza pago movil'''
class PagoMovil(Pago):
    def __init__(self):#datos en blanco para llenar despues
        self.__banco=""
        self.__cedula=""
        self.__numeroTlf=""
        self.__concepto=""
    def transaccion(self):#llenar datos
        self.__banco=input("ingrese banco: ")
        self.__cedula = input("ingrese cedula: ")
        self.__numeroTlf = input("ingrese numero de telefono: ")
        self.__concepto = input("ingrese cocepto: ")
    #imprimir datos de pago movil
        print("pago movil realizado")
        print(f"banco receptor: {self.__banco}")
        print(f"cedula: {self.__cedula}")
        print(f"numero: {self.__numeroTlf}")
        print(f"concepto: {self.__concepto}")