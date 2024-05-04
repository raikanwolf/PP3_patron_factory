'''clase para padre para los pagos'''
class Pago():
    def __init__(self, montoPagar):
        self._montoPagar=montoPagar
    def transaccion(self):
        pass
    def getMonto(self):
        return self._montoPagar
    def getPagoEfectuado(self):
        return True