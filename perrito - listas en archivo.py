###########################################################
#Elaborado por: Paula Porras Aguilar e Ileana Ortiz López
#Fecha de Realización: 16/01/2018
#Ultima actualización: 16/01/2018 10:23am
###########################################################
import pickle

#El programa define la clase "perro"
class Perro:
    """
    F:Método constructor = Crea la estructura de la clase perro
    E:NA
    S:NA
    """
    def __init__(self,pnombre):
        self.nombre=pnombre
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
        return "El perro: "+self.nombre+", es de la raza: "+self.raza+", su color de pelaje es:"+self.color+" y su edad es:"+self.edad
         
####Programa Principal
caninos=[]
#instaciación de la variable
vnombre=input("Ingrese el nombre del perro: ")
perrito=Perro(vnombre)
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
caninos.append(perrito)
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")


vnombre=input("Ingrese el nombre del perro: ")
perrito2=Perro(vnombre)
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
caninos.append(perrito2)

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

archivo =open("veterinaria","wb")
pickle.dump(caninos,archivo)
archivo.close()

with open("veterinaria","rb") as f:
    print("2. Voy a leer el archivo: veterinaria")
    lista = pickle.load(f)
    print("2. Voy a cerrar el archivo: veterinaria")
lista[0].indicarDatos()
lista[1].indicarDatos()


























        
