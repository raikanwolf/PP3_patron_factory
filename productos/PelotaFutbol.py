from productos.Pelota import Pelota


class PelotaFutbol(Pelota):
    def pateada(self):
        print("soy pateada")

    def atrapada(self):
        print("soy atrapada con mano pero solo por un portero, de lo contrario FALTA")