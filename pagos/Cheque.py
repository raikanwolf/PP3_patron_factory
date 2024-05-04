from pagos.Pago import Pago
'''clase para el pago con cheque'''
class Cheque(Pago):
    def __init__(self):#datos en blanco

        self.__numCheque=""
        self.__entidadBancaria=""

    def transaccion(self):#llenar datos e imprimir
        self.__numCheque=input("ingrese numero de chque: ")
        self.__entidadBancaria=input("entidad bancaria: ")
        print("Pago con cheque realizado")
        print(f"numero de cheque {self.__numCheque}")
        print(f"entidad bancaria de cheque {self.__entidadBancaria}")