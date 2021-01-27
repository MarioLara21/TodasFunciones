#Elaborado por: XyY
#Fecha de creación: 6/11/2019, 5:00pm
#Última modificación: 8/11/2019, 7:00 pm
#Versión: 3.5.2


#importación de libreriasc
import sys

#Definición de clases

class Persona:
    
    def __init__(self,ced,nombre,ti):
        self.cedula=ced
        self.nombre=nombre
        self.tipo=ti

    def asignarTipo(self,ptipo):
        self.tipo = ptipo
        
    def obtenerTipo(self):
        return self.tipo

    def asignarNombre(self,pnombre):
        self.nombre = pnombre
        
    def obtenerNombre(self):
        return self.nombre

    def asignarCedula(self,pcedula):
        self.cedula = pcedula

    def obtenerCedula(self):
        return self.cedula

    def mostrar(self):
        print ("Cédula: "+str(self.cedula))
        print ("Nombre: "+self.nombre)
        print ("Tipo: "+self.tipo)
        
#Objetos con Herencia Simple
        
class Estudiante(Persona):
    def __init__(self,ced,nombre,carnet,carrera):
        self.carnet=carnet
        self.carrera=carrera
        Persona.__init__(self,ced,nombre,"Estudiante")

    def asignarCarnet(self,pcarnet):
        self.carnet = pcarnet

    def obtenerCarnet(self):
        return self.carnet

    def asignarNombre(self,pnombre):
        self.nombre = pnombre

    def obtenerNombre(self):
        return self.nombre

    def asignarCedula(self,pcedula):
        self.cedula = pcedula

    def obtenerCedula(self):
        return self.cedula

    def asignarTipo(self,ptipo):
        self.tipo = ptipo
        
    def obtenerTipo(self):
        return self.tipo
    
    def mostrar(self):
        Persona.mostrar(self)
        print ("Número de carnet: "+str(self.carnet))
        print ("Carrera: "+self.carrera)

        
class Funcionario(Persona):
    
    def __init__(self,ced,nombre,sal,puesto):
        self.salario=sal
        self.puesto=puesto
        Persona.__init__(self,ced,nombre,"Funcionario")

    def asignarNombre(self,pnombre):
        self.nombre = pnombre

    def obtenerNombre(self):
        return self.nombre

    def asignarPuesto(self,ppuesto):
        self.puesto = ppuesto

    def obtenerPuesto(self):
        return self.puesto

    def asignarCedula(self,pcedula):
        self.cedula = pcedula

    def obtenerCedula(self):
        return self.cedula

    def asignarTipo(self,ptipo):
        self.tipo = ptipo

    def obtenerTipo(self):
        return self.tipo

    def mostrar(self):
        Persona.mostrar(self)
        print ("Salario: "+str(self.salario))
        print ("Puesto: "+self.puesto)
