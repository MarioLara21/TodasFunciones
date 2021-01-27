#Creado por Leonardo Fariña y Mario Lara
#Fecha de creación 03/07/2020 8:33am
#Última modificación 05/07/2020 19:05
#Vesión 3.8.3
#Importación de librerías
import os
from funciones import *

#Definición de funciones
def confirmarSalir(vuelos):
    """
    Funcionalidad: Pide la confirmación de la salida
    Entradas:NA
    Salidas:Si sale o no
    """
    try:
        print("Está seguro que desea salir?\n\n1.Sí\n2.No")
        opcion=int(input("Ingrese la opción selccionada: "))
        if opcion==1:
            print("Gracias por utilizar nuestros servicios.")
            os._exit(1)
            return
        elif opcion==2:
            return menu(vuelos)
        else:
            print("Ingrese una opción, ya sea 1 o 2.")
            return confirmarSalir(vuelos)
    except ValueError:
        print("Ingrese un dato de tipo entero")
        return confirmarSalir(vuelos)
    except:
        print("Ingrese un dato válido")
        return confirmarSalir(vuelos)
def confirmarEliminar(vuelos):
    """
    Funcionalidad: Pide la confirmación de la función para eliminar
    Entradas:NA
    Salidas:Si se borra o no
    """
    try:
        print("Está seguro que desea borrar la maleta?\n\n1.Sí\n2.No")
        opcion=int(input("Ingrese la opción selccionada: "))
        if opcion==1:
            return eliminarMaleta(vuelos)
        elif opcion==2:
            return menu(vuelos)
        else:
            print("Ingrese una opción, ya sea 1 o 2.")
            return confirmarEliminar(vuelos)
    except ValueError:
        print("Ingrese un dato de tipo entero")
        return confirmarEliminar(vuelos)
    except:
        print("Ingrese un dato válido")
        return confirmarEliminar(vuelos)
def subMenu(vuelos):
    '''
    Funcionalidad:Desplegar un SubMenu con las opciones de consultar
    Entrada:()
    Salida: La accion de la opcion seleccionada
    '''
    try:
        opcion = int(input("\n    1- Maletas por vuelo\n    2- Maletas por persona\n\nIngrese su elección:"))
        assert 0 < opcion < 3
        if opcion == 1:
            pedirVuelo(vuelos)                 
        elif opcion == 2:
            pedirPers(vuelos)
        else:
            return "Por favor ingrese los datos solicitados."
    except:
        print("\nIngrese un número del 1 al 2 por favor.")
        return subMenu(vuelos)
    
def menu(vuelos):
    '''
    Funcionalidad:Desplegar un menu con las opciones de la tarea
    Entrada:()
    Salida: La accion de la opcion seleccionada
    '''    
    try:        
        opcion = int(input("\n1- Registrar equipajes\n2- Eliminar equipaje\n3- Modificar equipaje\n4- Consultar\n5- Salir\n\nIngrese su elección:"))
        assert 0 < opcion < 6
        if opcion == 1:
            registrarMaleta(vuelos)                
        elif opcion == 2:
            confirmarEliminar(vuelos)
        elif opcion == 3:
            modificarMaleta(vuelos)            
        elif opcion == 4:
            subMenu(vuelos)            
        elif opcion == 5:            
            confirmarSalir(vuelos)
        menu(vuelos)
    except AssertionError:
        print("\nDebe insertar un número del 1 al 5.")
        menu(vuelos)
    except:
        print("\nDebe insertar un número.")
        menu(vuelos)
    
#=====================Programa principal
vuelos = []        
menu(vuelos)


















