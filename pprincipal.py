#Elaborado por: AAAA
#Fecha de creación: 23/10/2019, 8:00am
#Última modificación: 26/10/2019, 11:00 pm
#Versión: 3.5.2

#importación de librerías
from ffunc import *
import pickle
import re

#Definición de funciones

def menu():
    """
    Funcionalidad: Responsable de pedir al usuario la opción.
    Entradas:
    -num(string) opción.
    Salidas:
    -String que le indica al usuario lo que pidió.
    """
    a=0
    dicc={}
    while a==0:
        dicc=leerArchivo()
        print("\n")
        print("___________________________________________")
        print("___________________Paro____________________")
        print("1. Registrar Persona")
        print("2. Actualizar información de una persona")
        print("3. Reporte")
        print("4. Estudiantes por universidad")
        print("5. Cantidad de manifestantes")
        print("6. Salir")
        print("___________________________________________")
        num=input("Digite una opción: ")
        if num=="1":      
            registrarPersona(dicc)
        elif num=="2":
            actualizarDatos(dicc)
        elif num=="3":
            reporte(dicc)
        elif num=="4":
            estudiantesPorUniversidad(dicc)
        elif num=="5":
            manifestantes(dicc)
        elif num=="6":
            a=1
            print("¡Adiós!")
            print("___________________________________________")
            return""
        else:
            print("¡Opción inválida!")
    return""

#Programa Principal
menu()
