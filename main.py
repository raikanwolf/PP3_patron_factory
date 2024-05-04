
from Cliente import Cliente
from datetime import date
from productos.Producto import verProductosDisponibles

#import os

''' ver si se puede borrar lo que aparece en pantalla
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

'''

'''esta funcion ejecuta la opcion solicitada por el usuario'''
def menu(op,colaClientes):

    #borrarPantalla()
    if(op==1):
        n=int(input("cuantos clientes desea crear?: "))

    #creamos n clientes y se agregan a la cola
        for i in range(n):
            nombre = input("Ingrese su primer nombre: ")
            apellido = input("Ingrese su primer apellido: ")
            cedula = input("Ingrese su cedula de identidad, sin espacios ni puntos: ")

            print("ingrese fecha de nacimiento segun los datos que se le pidan")
        #datos para la fecha de nacimiento
            dia = int(input("dia: "))
            mes = int(input("mes: "))
            year = int(input("año: "))

            fecha = date(year, mes, dia)
            genero = input("ingrese su genero M o F: ").upper()
        #con los datos obtenidos se construye cliente y luego se agrega a la cola
            c=Cliente(nombre, apellido, cedula, fecha.strftime('%d/%m/%Y'), genero)
            colaClientes.append(c)
            print("\tCliente entro en cola")

        input("-presione ENTER tecla para continuar-")

#opcion para atender a los clientes
    elif(op==2):#si la cola esta vacia, continuamos sin  hacer nada
        if (not colaClientes):
            input("no hay clientes en cola, presione una tecla para continuar")
        else:
            i=0
            while(colaClientes):
                #el primer cilente de la cola decide su caja
                cliente=colaClientes[i]
                caja=cliente.decideCada()

                if(caja.getNumero()==1):
                    caja.atiendeCliente(cliente)
                    colaClientes.pop(i)
                    print(f" cliente C.I.: {cliente.getCedula()} salio de la cola")
                elif (caja.getNumero() == 2):
                    caja.atiendeCliente(cliente)
                    colaClientes.pop(1)
                    print(f" cliente C.I.: {cliente.getCedula()} salio de la cola")
                elif (caja.getNumero() == 3):
                    caja.atiendeCliente(cliente)
                    colaClientes.pop(2)
                    print(f" cliente C.I.: {cliente.getCedula()} salio de la cola")
#ver productos disponibles en el inventario
    elif(op==3):
        verProductosDisponibles()
        input("-presione ENTER para continuar-")




if __name__ == '__main__':
    '''menu de opciones'''
    op=0
    colaClientes=[]
    while(op!=4):

        print("\t.:GESTION DE TIENDA:.")
        print("acciones disponibles")
        print("1-Crear Clientes")
        print("2-Atender cliente en caja")
        print("3-ver productos disponibles")
        print("4-salir")

        op=int(input("ingrese el numero de opcion: "))
        print("\n")
        if(op!=4):
            menu(op,colaClientes)

