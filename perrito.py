###########################################################
#Elaborado por: Paula Porras Aguilar e Ileana Ortiz López
#Fecha de Realización: 16/01/2018
#Ultima actualización: 16/01/2018 10:23am
###########################################################

#El programa define la clase "perro"
class Perro:
    """Definición de Atributos"""
    nombre=""
    raza=""
    color=""
    edad=0
    """Definición de métodos"""
    """
    F:Método constructor = Crea la estructura de la clase perro
    E:NA
    S:NA
    """
    def __init__(self):
            
        self.nombre=""
        self.raza=""
        self.color=""
        self.edad=0
    """
    F:NombrePerro,
    E:el nombre del perro (string)
    S:Asigna un nombre al atributo nombre del perro
    """    
    def asignarNombre(self,pnombre):
        self.nombre=pnombre
    """
    F:RazaPerro,
    E:la raza del perro (string)
    S:Asigna la raza al atributo raza del perro
    """    
    def asignarRaza(self,praza):
        self.raza=praza
    """
    F:EdadPerro,
    E:la edad del perro (int)
    S:Asigna la edad al atributo edad del perro
    """
    def asignarEdad(self,pedad):
        self.edad=pedad
    """
    F:ColordePelo,
    E:el codigo del color del perro (int)
    S:Asigna el color del pelo al atributo color del perro
    """    
    def asignarColor(self,pcolor):
        if pcolor==1:
            self.color="Negro"
        elif pcolor==2:
            self.color="Blanco"
        elif pcolor==3:
            self.color= "Gris"
        elif pcolor==4:
            self.color= "Cafe"
        else:
            self.color= "Combinado"
    """
    F:IndicaDatos,
    E:NA
    S:Muestra el contenido de los atributos del objeto
    """    
    def indicarDatos(self):
         return "El perro: "+self.nombre+", es de la raza: "+self.raza+",su color de pelaje es:"+self.color+" y su edad es:"+self.edad
         
####Programa Principal
#instaciación de la variable
perrito=Perro()
vnombre=input("Ingrese el nombre del perro: ")
perrito.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo: "))
perrito.asignarColor(vcolor)
print(perrito.indicarDatos())
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

perrito2=Perro()
vnombre=input("Ingrese el nombre del perro: ")
perrito2.asignarNombre(vnombre)

vraza=input("Ingrese la raza del perro: ")
perrito2.asignarRaza(vraza)

vedad=input("Ingrese la edad del perro: ")
perrito2.asignarEdad(vedad)

print("---COLORES DE PELAJE---")
print("1-Negro")
print("2-Blanco")
print("3-Gris")
print("4-Café")
print("5-Combinado")
vcolor=int(input("Digite el número correspondiente al color del pelo del perro: "))
perrito2.asignarColor(vcolor)

print(perrito2.indicarDatos())

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
























        
