from datetime import date

class Pedido():
    def __init__(self):
        self.__fecha=date.today()
        self.__listaProductos=[]
        self.__cadCodigo=""
        self.__cadNombre = ""
        self.__cadPrecio =0
        self.__numArticulos=0
#setter
    def setDatos(self,cadCodigo, cadNombre, cadPrecio):
        self.__cadCodigo = cadCodigo
        self.__cadNombre = cadNombre
        self.__cadPrecio = cadPrecio
#getters
    def getNumArticulos(self):
        return self.__numArticulos
    def getCadCodigo(self):
        return self.__cadCodigo
    def getCadNombre(self):
        return self.__cadNombre
    def getPrecio(self):
        return self.__cadPrecio
    def getFecha(self):
        return self.__fecha.strftime('%d/%m/%Y')
#agregamos producto a la lista
    def agregaProducto(self, producto):
        self.__listaProductos.append(producto)
#recorremos la lista para ver los productos, retornamos una cadena con los datos
    def verProductos(self):
        cad=""
        i=0
        for producto in self.__listaProductos:
            i+=1
        #tomamos los datos del productos para poder usarlos despues
            self.setDatos(producto.getCodigo(), producto.getNombre(), producto.getPrecio())
            cad+=" articulo "+producto.getCodigo()+" "+producto.getNombre()+" "+"bs: "+str(producto.getPrecio())+"\n"
            self.__numArticulos=i

        return cad



