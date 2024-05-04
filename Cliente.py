from caja.caja import Caja
from productos.Pedido import Pedido

from productos.FabricaProductos import FabricaProductos
'''clientes que realizaran pedidos y pagos'''
class Cliente():
    def __init__(self, nombre,apellido,cedula,f_nacimiento, genero):#constructor
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__f_nacimiento = f_nacimiento
        self.__genero = genero
        self.__pedidoRealizado=False #si realizo un pedido
        self.__pedido=Pedido()
        self.__atendido=False #si fue atendido
#El cliente escribira el nombre del producto, los productos se crean a partir de una fabrica que retorna instancias
#los productos retornados se guardan en la lista, se confirma si e cliente termino su pedido
    def realizaPedido(self):
        fabricaProductos=FabricaProductos()
        while(not self.__pedidoRealizado):
            nombreProducto=input("escriba el nombre producto para agregarlo a la lista: ").lower()
            n=int(input(f"¿Cuantos(as) {nombreProducto} desea?->"))

            for i in range(n):#pedimos que se creen los productos
                self.__pedido.agregaProducto(fabricaProductos.crearProducto(nombreProducto))


        #esta parte determina si un cliente termino o no su pedido
            SN=input("Termino su pedido? S o N: ").upper()

            if(SN=="S"):
                self.__pedidoRealizado=True
            elif(SN=="N"):
                print ("continue")
            else:
                error=True
                while(error):
                    print("opcion no valida")
                    SN=input("Termino su pedido? S o N: ").upper()
                    if (SN == "S"):
                        self.__pedidoRealizado = True
                        error=False
                    elif (SN == "N"):
                        print("continue")
                        error = False
        return self.__pedido

#funcion donde el cliente decide la caja desocupada a la cual ir
    def decideCada(self):
        caja1 = Caja(1)
        caja2 = Caja(2)
        caja3 = Caja(3)
        if (caja1.getOcupada() == False):
            print(f"el cliente entro en la caja {caja1.getNumero()}")
            caja1.setOcupada(True)
            caja1.atiendeCliente(self)
            caja1.setOcupada(False)
            return caja1

            # sacar cliente de cola
            #quizas devolver un true o false dependiendo si fue atendido o no
        elif (caja2.getOcupada() == False):
            print(f"el cliente entro en la caja {caja2.getNumero()}")
            caja2.setOcupada(True)
            caja2.atiendeCliente(self)
            caja2.setOcupada(False)
            return caja2
        elif (caja3.getOcupada() == False):
            print(f"el cliente entro en la caja {caja3.getNumero()}")
            caja3.setOcupada(True)
            caja3.atiendeCliente(self)
            caja3.setOcupada(False)
            return caja3
        else:
            print("clientes esperando por caja")
#getters y setters de los atributos de cliente
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCedula(self):
        return self.__cedula
    def setAtendido(self,atendido):
        self.__atendido=atendido
    def getAtendido(self):
        return self.__atendido
    def getPedido(self):
        #cadFecha="fecha "+self.__pedido.getFecha().strftime('%d/%m/%Y')+"\n"
        return self.__pedido
