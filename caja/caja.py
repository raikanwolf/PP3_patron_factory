
from pagos.Efectivo import Efectivo
from pagos.Pago import Pago
from pagos.PagoMovil import PagoMovil
from pagos.Tarjeta import Tarjeta
from pagos.Cheque import Cheque
from pagos.Transferencia import Transferencia

'''caja que atiende a los clientes y maneja pagos'''
class Caja():
    def __init__(self,n):
        self.__ocupada=False
        self.__numero=n
        self.__tasa=0

    def getNumero(self):
        return self.__numero

    def getOcupada(self):
        return self.__ocupada
    def setOcupada(self,ocupando):
        self.__ocupada=ocupando
#calculos de costos en bolivares y en dolares
#costo en bolivares suma los precios individuales de los pedidos con sus impuestos
    def calCostoBolivares(self, pedido, costo):
        for i in range(pedido.getNumArticulos()):
            costo+=pedido.getPrecio()+(pedido.getPrecio()*0.16)
        return costo
#costo en dolares recibe el pago en bolivares y calcula con la tasa
    def calCostoDolares(self, pago):
        self.__tasa=float(input("tasa del dia: "))
        costoDolares=pago/self.__tasa
        return costoDolares
#factura con los pedidos
    def generaFactura(self, pedido):
        print(" fecha: "+pedido.getFecha()+"\n"+pedido.verProductos())
#metodo que atiende a los clientes
    def atiendeCliente(self, cliente):
        if (cliente):
            self.setOcupada(True)
            nombre = cliente.getNombre()
            apellido = cliente.getApellido()
            cedula = cliente.getCedula()
            pedido = cliente.realizaPedido() #aqui el cliente realiza su pedido
            print(f"\n cliente: {nombre} {apellido} C.I.: {cedula}")#se imprime datos
            self.generaFactura(pedido)
            #print(pedido.getCadPrecio()+"bs")

            pago=round(self.calCostoBolivares(pedido,0),3)
            pagoDolares=self.calCostoDolares(pago).__round__(2)
            print(f" total: {pago} bs=={pagoDolares}$")
            input("presione ENTER para continuar")
    #se realiza el pago a eleccion
            self.efectuarPago(pago, pagoDolares)

            cliente.setAtendido(True)
            input("presione ENTER tecla para continuar")
#metodoque efecta el pago
    def efectuarPago(self,monto,montoDolares):
        Pago(monto)

        print("1-efectivo")
        print("2-tarjeta")
        print("3-transferencia")
        print("4-pago movil")
        print("5-cheque")

        pagoEfectuado=False

        while(pagoEfectuado==False):
            op = int(input("seleccione metodo de pago: "))
            if(op==1):
                efectivo = Efectivo(montoDolares)
                efectivo.transaccion()
                pagoEfectuado=efectivo.getPagoEfectuado()
            elif(op==2):
                tarjeta = Tarjeta()
                tarjeta.transaccion()
                pagoEfectuado = tarjeta.getPagoEfectuado()
            elif (op == 3):
                transferencia = Transferencia()
                transferencia.transaccion()
                pagoEfectuado = transferencia.getPagoEfectuado()
            elif (op == 4):
                pagoMovil = PagoMovil()
                pagoMovil.transaccion()
                pagoEfectuado = pagoMovil.getPagoEfectuado()
            elif (op == 5):
                cheque = Cheque()
                cheque.transaccion()
                pagoEfectuado = cheque.getPagoEfectuado()
            else:
                print("opcion no valida")
