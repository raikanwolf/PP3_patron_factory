
from productos.Bate import Bate
from productos.PelotaFutbol import PelotaFutbol
from productos.PelotaBeisbol import PelotaBeisbol

class FabricaProductos():
    #a partir del producto solicitado, se crea un objeto del inventario
    def crearProducto(self, producto):
        if(producto=="bate"):
            return Bate("bate", "001", "bate para golpear pelotas", 70.0)
        elif(producto=="pelota de beisbol"):
            return PelotaBeisbol("pelota de beisbol", "002", "pelota para jugar beisbol", 50.0)
        elif(producto=="pelota de futbol"):
            return PelotaFutbol("pelota de futbol", "003", "pelota para jugar futnol", 60.0)
        else:
            return None

