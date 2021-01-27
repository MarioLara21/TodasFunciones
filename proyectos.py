#Elaborado por: XyY
#Fecha de creación: 1/11/2019, 8:00am
#Última modificación: 2/11/2019, 11:30 pm
#Versión: 3.5.2

#importación de libreríasp
from BD import *
from funciones import *
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
    listaProyectos=[]
    listaProyectos=leerArchivo()
    while True:
      print("_____________________________")
      print("____Registro de Proyectos____")
      print("1. Registrar proyecto")
      print("2. Asignar nota a un proyecto")
      print("3. Lista de proyectos")
      print("4. Proyectos destacados")
      print("5. Salir")
      print("_____________________________")
      opcion =(input("Indique la opción: "))
      print("\n")
      if opcion == "1":
         registrarProyecto(listaProyectos)

      elif opcion == "2":
         asignarNotaAProyecto(listaProyectos)
         
      elif opcion=="3":
         mostrarListaDeProyectos(listaProyectos)
         
      elif opcion == "4":
         mostrarProyectosDestacados(listaProyectos)
         
      elif opcion == "5":
         listaProyectos=leerArchivo()
         grabarArchivo(listaProyectos)
         print("¡Gracias, adiós!")
         break
      else:
         print("¡Opción inválida!")

#Programa Principal

menu()
