from  pagos.Pago import Pago

class Tarjeta(Pago):
    def __init__(self):
        self.__numero=""
        self.__caducidad=""
        self.__VoM=""
    def transaccion(self):
        self.__numero = input("ingrese numero de tarjeta: ")
        self.__caducidad=input("fecha de caducidad mm-aa: ")
        self.__VoM = input("Visa (V) o Master (M): ")
        print("Pago con tarjeta efectuado")
        print(f"numero: {self.__numero}")
        print(f"banco receptor: {self.__caducidad}")
        print(f"tipo de tarjeta: {self.__VoM}")