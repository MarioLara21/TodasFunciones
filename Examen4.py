#Creado por Mario Lara Molina
#Fecha de creación 05/08/2020
#Última modificación 05/08/2020
#Versión 3.8.3
#Importación de librerias
import pickle
#Declaracion de variables
global registro
registro=[]
#Declaración de clases
class Beca:
    "Definición de atributos"
    nombre=""
    carnet=0
    datos= ["",""]
    estado:False
    "Definición de métodos"
    def __init__(self,pnombre,pcarnet,pdatos,pestado):
        self.nombre=pnombre
        self.carnet=pcarnet
        self.datos=pdatos
        self.estado=pestado
        return
    def setNombre(self,pnombre):
        self.nombre=pnombre
        return
    def setCarnet(self,pcarnet):
        self.carnet=pcarnet
        return
    def setDatos(self,pdatos):
        self.datos=pdatos
        return
    def setEstado(self,pestado):
        self.estado=pestado
        return
    def getNombre(self):
        return self.nombre
    def getCarnet(self):
        return self.carnet
    def getDatos(self):
        return self.datos
    def getEstado(self):
        return self.estado
    def mostrar(self):
        return "El estudiante: "+str(self.getNombre)+"\nCon el carnet: "+str(self.getCarnet)+"\nCon los el celular: "+str(self.getDatos[0])+"\nY el correo: "+str(self.getDatos[1])+"\nPresenta el estado: "+str(self.getEstado)

class Cientifico:
    "Definición de atributos"
    nombreCole=""
    "Definición de métodos"
    def __init__(self,nombre,carnet,datos,estado,pNombCole):
        self.nombreCole=pNombCole
        Beca.__init__(self,nombre,carnet,datos,estado)
        return
    def setNombreCole(self,pNombCole):
        self.nombreCole=pNombCole
        return
    def getNombreCole(self):
        return self.nombreCole
    def mostrar(self):
        return "Proviene del colegio: "+str(self.getNombreCole)+str(Beca.mostrar(self))

class Asistencia:
    "Definición de atributos"
    tipo=1
    "Definición de métodos"
    def __init__(self,nombre,carnet,datos,estado,ptipo):
        self.tipo=ptipo
        Beca.__init__(self,nombre,carnet,datos,estado)
    def setTipo(self,pTipo):
        self.tipo=pTipo
    def getTipo(self):
        return self.tipo
    def mostrar(self):
        return "La beca es de tipo: "+str(self.getTipo(self))+str(Beca.mostrar(self))
#Definición de funciones
#Archivos
def grabaArch(nomArchGrabar,contenido):
    """
    Funcionalidad: Grabar el contenido en un archivo 
    Entradas:nomArchLeer(str), nombre del archivo a leer,contendio a grabar
    Salidas: NA o mensaje de error
    """
    try:
        arch=open(nomArchGrabar,"wb")
        pickle.dump(contenido,arch)
        arch.close()
        return 
    except:
        return "Error al grabar el archivo: "+ nomArchGrabar
def leerArch(nomArchLeer):
    """
    Funcionalidad: Leer el contenido de un archivo 
    Entradas:nomArchLeer(str), nombre del archivo a leer
    Salidas: datos archivo
    """
    salida = ""
    try:
        arch=open(nomArchLeer,"rb")
        salida = pickle.load(arch)
        arch.close()
        return salida
    except:        
        return "Error al leer el archivo: "+ nomArchLeer
def validarArchivo():
    '''
    Funcionalidad: Comprobar que existe el archivo con los datos necesarios
    Entrada:()
    Salida: datos archivo
    '''
    global becas
    archivo = leerArch("Becas")
    if archivo == "Error al leer el archivo: Becas":
        grabaArch("Becas",[])
    archivo = leerArch("Becas")
    becas = archivo
    return archivo

#Primera Parte
def pedirNombre():
    pnombre=input("Ingrese el nombre: ")
    return pnombre
def pedirCarnet():
    pcarnet=input("Ingrese el carnet: ")
    return pcarnet
def pedirDatos():
    pcelular=input("Ingrese el celular: ")
    pcorreo=input("Ingrese el correo: ")
    pdatos=[pcelular,pcorreo]
    return pdatos
def pedirEstado():
    pestado=input("Ingrese el Estado: ")
    return pestado
def pedirNombreCole():
    pNombreCole=input("Ingrese el nombre del colegio: ")
    return pNombreCole
def pedirTipo():
    pTipo=input("Ingrese el tipo de asitencia: ")
    return pTipo
def mostrarTipo(num):
    """
    Funcionalidad: Muestra  el tipo de la Beca
    Entradas: num= Tipo de la Beca
    Salidas: Nombre del tipo
    """
    if int(num) == 1:
        salida = "Horas Estudiante"
    elif int(num) == 2:
        salida = "Horas asistente"
    else:
        salida = "Tutoría Estudiantil"
    return salida
def registrarBeca(op):
    """
    Funcionalidad:
    Entradas: op debe ser 0 si se quiere Cientiico o algo difetente si se quiere Asistencia
    Salidas:
    """
    try:
        pnombre=pedirNombre()
        pcarnet=pedirCarnet()
        pdatos=pedirDatos()
        pestado=pedirEstado()
        if op==0:
            pNombCole=pedirNombreCole()
            nueva=Cientifico(pnombre,pcarnet,pdatos,pestado,pNombCole)
        else:
            pTipo=pedirTipo()
            nueva=Asistencia(pnombre,pcarnet,pdatos,pestado,pTipo)
        registro.append(nueva)
        grabaArch("Becas",registro)
        return 
    except:
        return "Por favor ingrese los datos nuevamente"
def mostrarBecas():
    """
    Funcionalidad:
    Entradas:
    Salidas:
    """
    global registro
    for objeto in registro:
        print(objeto.mostrar())
#Segunda parte
#Desafío 1
def esPar(num):
    """
    Funcionalidad: Verifica si el dígito es par
    Entradas: num= Número entero
    Salidas: Si el número es par o no
    Restricciones: El dato debe ser un número
    """
    if num%2==0:
        return True
    return False

def multPar(num):
    """
    Funcionalidad: Multiplica los números pares de una cifra
    Entradas: num= Número entero
    Salidas: Dígitos pares multiplicados
    Restricciones: El número debe ser entero
    """
    if (num//10)==0:
        if esPar(num)==False:
           return 1*num
        else:
            return num
    else:
        if esPar(num%10)==False:
            return multPar(num//10)
        else:
            return (num%10) * multPar(num//10)
            
def multiplicarDigitosParesDeCifra(num):
    """
    Funcionalidad: Valida el número ingresado
    Entradas: num= Número entero
    Salidas: Dato validado
    Restricciones: El número debe ser entero
    """
    try:
        num=int(num)
        if not isinstance(num,int):
            return "El valor ingresado debe corresponder a un número únicamente"
        elif num<=0:
            return "El valor de análisis debe ser mayor a cero"
        else:
            return "Al multiplicar los valores pares de la cifra numérica da: "+str(multPar(num))
    except:
        return "El valor ingresado debe corresponder a un número únicamente"
#Desafío 2
def separarAux(lista,imp=[],par=[]):
    """
    Funcionalidad: Separa los elementos en índices pares e impares
    Entradas:
    lista= lista con los datos
    imp= lista de números impares
    par= lista de números pares
    Salidas:
    Restricciones: la lista no debe ser vacía
    """
    if lista==[]:
        return [par,imp]
    else:
        if esPar(lista[0])==False:
            imp.append(lista[0])
        else:
            par.append(lista[0])
        return separarAux(lista[1:],imp,par)
def separarElementos(lista):
    """
    Funcionalidad: Valida los datos y llama a la función
    Entradas: lista= lista de elementos
    Salidas: Datos validados y llamado a la función
    Restricciones: la lista no debe ser vacia
    """
    try:
        if not isinstance(lista,list):
            return "Debe ingresar una lista"
        elif lista==[]:
            return "La lista no debe ser nula"
        else:
            return separarAux(lista,imp=[],par=[])
    except:
        return "Los datos deben ser de tipo entero positivo"
#PP
validarArchivo()
leerArch("Becas")
print("Registra cientifico")
registrarBeca(0)
print("Registra asistencia")
registrarBeca(1)
#Printeada de datos
print(multiplicarDigitosParesDeCifra(0))
print(multiplicarDigitosParesDeCifra(12345))
print(multiplicarDigitosParesDeCifra(135))
print(separarElementos([]))
print(separarElementos([1,2,3,4,5]))
print(separarElementos([1,3,5]))
print(separarElementos([2,4]))





















    
