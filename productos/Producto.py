class Producto():
    def __init__(self, nombre, codigo, descripcion, precio):
        self._nombre=nombre
        self._codigo=codigo
        self._descripcion=descripcion
        self._precio=precio

    def getNombre(self):
        return self._nombre
    def getCodigo(self):
        return self._codigo
    def getDescripcion(self):
        return self._descripcion
    def getPrecio(self):
        return self._precio

def verProductosDisponibles():
    print("\t** :Productos Disponibles: **")
    print("\t\tpelota de beisbol")
    print("\t\tpelota de futbol")
    print("\t\tbate")

