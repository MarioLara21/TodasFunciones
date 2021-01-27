#Realizado por: XyY
#Fecha de creación: 15/5/2019 7:45am
#Última actualización: 17/5/2019 8:30pm
#Versión 3.7.2

#Importación de librerías

import pickle
from archivo import *

#Inicialización de la variable global

#Definición de la clase Libro

class Libro:
    """Definición de atibutos"""
    ISBN=""
    nombre=""
    anno=0
    """Definición de métodos"""
    def __init__(self):
        """
        Función: Crea la estructura de la clase libro
        Entrada: N/A
        Salida: N/A
        """
        self.ISBN=""
        self.nombre="xxx"
        self.anno=0
    def setISBN(self,pISBN):
        """
        Función: Asigna el ISBN
        Entrada: pISBN (string)
        Salida: Asigna el ISBN como atributo del libro
        """
        self.ISBN=pISBN
    def setNombre(self,pnombre):
        """
        Función: Asigna el nombre
        Entrada: pnombre (string)
        Salida: Asigna el nombre como atributo del libro
        """
        self.nombre=pnombre
    def setAnno(self,panno):
        """
        Función: Asigna el año
        Entrada: Año (int)
        Salida: Asigna el año como atributo del libro
        """
        self.anno=panno
    def getISBN(self):
        """
        Función: Lee el ISBN
        Entrada: N/A
        Salida: Mostrar el contenido del atributo ISBN
        """
        return self.ISBN
    def getNombre(self):
        """
        Función: Lee el nombre
        Entrada: N/A
        Salida: Mostrar el contenido del atributo nombre
        """
        return self.nombre
    def getAnno(self):
        """
        Función: Lee el año
        Entrada: N/A
        Salida: Mostrar el contenido del atributo año
        """
        return self.anno
    def getDatos(self):
        """
        Función: Imprime los datos
        Entrada: N/A
        Salida: Mostrar el contenido de los atributos
        """
        print("\nISBN: "+self.ISBN)
        print("Nombre: "+self.nombre)
        print("Año: "+str(self.anno))
        return

