#Elaborado por: XyY
#Fecha de creación: 6/11/2019, 5:00pm
#Última modificación: 8/11/2019, 7:00 pm
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
    universidad=[]
    universidad=leerArchivo()
    a=0
    while a==0:
        universidad=[]
        universidad=leerArchivo()
        print ("__________________________________")
        print ("_______________Menú_______________")
        print ("1. Registrar Estudiante")
        print ("2. Registrar Funcionario")
        print ("3. Mostrar lista de estudiantes")
        print ("4. Mostrar Estudiante")
        print ("5. Mostrar Lista de funcionarios")
        print ("6. Mostrar Lista de Docentes")
        print ("7. Salir")
        print ("__________________________________")
        num=(input("Digite una opción: "))
        print ("\n")
        if num=="1":
            registrarEstudiante(universidad)
        elif num=="2":
            registrarFuncionario(universidad)
        elif num=="3":
            listaEst(universidad)
        elif num=="4":
            mostrarEstudiante(universidad)
        elif num=="5":
            listaFunc(universidad)
        elif num=="6":
            listaDoc(universidad)
        elif num=="7":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida!")


#Programa principal
menu()
