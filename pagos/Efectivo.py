from pagos.Pago import Pago

class Efectivo(Pago):

    def __init__(self, montoDolares):

        self.__dolares=montoDolares



    def transaccion(self):

        print("seleccione: ")
        print("1-pagar en bolivares")
        print("2-pagar en dolares")
        op=input()
        if(op==1):
            print(f"el cliente pago {self.__dolares*self.tasa}bs")
        else:
            print(f"el cliente pago{self.__dolares}$")
        