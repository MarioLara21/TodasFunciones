#Creado por Leonardo Fariña y Mario Lara
#Fecha de creación 03/07/2020 8:33am
#Última modificación 05/07/2020 19:44
#Versión 3.8.3
#importación de librerías
import re
#declaración de variables
vuelos=[]
#definición de clases
class Maleta:
    """Definición de Atributos"""
    codigo=""
    peso=0
    tamanno=True
    fragilidad=False
    descripción=""
    estado=0
    """Definición de métodos"""
    """
    Funcionalidad: método constructor= Crea la estructura de la clase Maleta
    Entradas:NA
    Salidas:NA
    """
    def __init__(self):
        self.codigo=""
        self.peso=0
        self.tamanno=True
        self.fragilidad=False
        self.descripcion=""
        estado=0
    def asignarCodigo(self,pcodigo):
        """
        Funcionalidad: codigo
        Entradas: el código del vuelo (alfanum)
        Salidas:Asigna el código del vuelo a la maleta
        """
        self.codigo=pcodigo        
        return
    def asignarPeso(self,ppeso):
        """
        Funcionalidad: peso
        Entradas: el peso de la maleta (int)
        Salidas:Asigna el peso de la maleta
        """
        self.peso=ppeso
        return
    def asignarTamanno(self,ptamanno):
        """
        Funcionalidad: tamaño
        Entradas: el tamaño de la maleta(booleano)(de mano o equipaje)
        Salidas: Asigna el tamaño de la maleta
        """
        self.tamanno=ptamanno
        return
    def asignarFragilidad(self,pfragilidad):
        """
        Funcionalidad: fragilidad
        Entradas: la fragilidad de la maleta(booleano)
        Salidas:Asigna la fragilidad de la maleta
        """
        self.fragilidad=pfragilidad
        return
    def asignarDescripcion(self,pdescripcion):
        """
        Funcionalidad: descripcion
        Entradas: descripción de la maleta(str)
        Salidas:Asigna una descripción de la maleta
        """
        self.descripcion=pdescripcion
        return
    def asignarEstado(self,pestado):
        """
        Funcionalidad: estado
        Entradas: el estado de la maleta (int)(por definir,recibido,entregado,no entregado,perdido,avería)
        Salidas:Asigna el estado de la maleta
        """
        self.estado=pestado
        return
    def indicarDatos(self):
        """
        Funcionalidad: Indica todos los datos de la maleta
        Entradas:
        Salidas:
        """
        print("La maleta",self.codigo,"\nCon el peso:",self.peso,"\nDe tamaño:",self.tamanno,"\nDe fragilidad tipo:",self.fragilidad,"\nCuya descripción es:",self.descripcion,"Estado:",self.estado)
#definición de funciones
#########################################
def validarCodigo(pcodigo):
    """
    Funcionalidad: validar los datos de pedirCodigo
    Entradas: pcodigo=codigo de la maleta
    Salidas: datos validados
    """
    try:
        for maleta in vuelos:
            if pcodigo==maleta.codigo:
                print("La maleta ya se encuentra registrada\nIngrese una nueva por favor.")
                return pedirCodigo()
            else:
                pass
        if pcodigo=="":
            print("Ingrese el código por favor.")
        elif re.match("^\w{4}\d{9}$",pcodigo):
            return pcodigo
        else:
            print("Por favor ingrese un formato válido\nEl formato válido es: 4 carácteres alfanuméricos y el número de cédula")
            return pedirCodigo()

    except:
        print("Por favor ingrese un formato válido\nEl formato válido es: 4 carácteres alfanuméricos y el número de cédula.")
        return pedirCodigo()
def pedirCodigo():
    """
    Funcionalidad: Pedir el código de la maleta
    Entradas:NA
    Salidas:Datos en pantalla
    """
    pcodigo=input("Ingrese el código de la maleta: ")
    return validarCodigo(pcodigo)
########################################################
def validarPeso(ppeso):
    """
    Funcionalidad: Validar los datos para pedirDatos
    Entradas: ppeso= peso de la maleta
    Salidas: datos validados
    """
    try:
        float(ppeso)
        if ppeso=="":
            print("Ingrese el peso por favor.")
        elif not isinstance(ppeso,float):
            print("El peso debe ser un dato de tipo flotante")
        elif ppeso<0.00:
            print("El peso debe ser mayor a 0.00")
        else:
            return ppeso
        pedirPeso()
    except:
        print("Ingrese un dato de tipo flotante")
        return pedirPeso()
def pedirPeso():
    """
    Funcionalidad: Pedir el peso de la maleta
    Entradas:NA
    Salidas:Datos en pantalla
    """
    ppeso=input("Ingrese el peso de la maleta: ")
    return validarPeso(ppeso)
########################################################
def validarTamanno(ptamanno):
    """
    Funcionalidad: Validar los datos de pedirTamanno
    Entradas: ptamanno= tamaño de la maleta
    Salidas: Datos validados
    """
    try:
        bool(ptamanno)
        if ptamanno=="":
            print("Ingrese el tamaño por favor")
        elif not isinstance(ptamanno,bool):
            print("El peso debe ser un dato de tipo booleano")
            return pedirTamanno()
        else:
            return ptamanno
    except:
        print("Ingrese un True o False")
        return pedirTamanno()
def pedirTamanno():
    """
    Funcionalidad: Pedir el tamaño de la maleta
    Entradas:NA
    Salidas:Datos en pantalla
    """
    ptamanno=input("Ingrese el tamaño de la maleta: ")
    return validarTamanno(ptamanno)
########################################################
def validarFragilidad(pfragilidad):
    """
    Funcionalidad: Validar los datos para pedirFragilidad
    Entradas: pfragilidad= Fragilidad de la maleta
    Salidas: Datos validados
    """
    try:
        bool(pfragilidad)
        if pfragilidad=="":
            print("Ingrese la fragilidad por favor.")
        elif not isinstance(pfragilidad,bool):
            print("Ingrese un dato de tipo booleano")
        else:
            return pfragilidad
        pedirFragilidad()
    except:
        print("Ingrese True o False")
        return pedirFragilidad()
def pedirFragilidad():
    """
    Funcionalidad: Pedir la fragilidad de la maleta
    Entradas:NA
    Salidas:Datos en pantalla
    """
    pfragilidad=input("Ingrese la fragilidad de la maleta: ")
    return validarFragilidad(pfragilidad)
########################################################
def validarDescripcion(pdescripcion):
    """
    Funcionalidad: Validar los datos para pedirDescripción
    Entradas: pdescripcion= Descripción de la maleta
    Salidas: Datos validados
    """
    try:
        if pdescripcion=="":
            print("Ingrese una descripción por favor.")
        elif not isinstance(pdescripcion,str):
            print("Ingrese un dato de tipo string")
        elif len(descripcion)<5:
            print("La descripción debe ser mayor a 5 caracteres.")
        else:
            return pdescripcion
        pedirDescripcion()
    except:
        print("Ingrese una breve descripción")
        return pedirDescripcion()
def pedirDescripcion():
    """
    Funcionalidad: Pedir la descripción de la maleta
    Entradas:NA
    Salidas: Datos en pantalla
    """
    pdescripcion=input("Ingrese la descripción de la maleta: ")
    return validarDescripcion(pdescripcion)
########################################################
def validarEstado(pestado):
    """
    Funcionalidad: Validar los datos para pedirEstado
    Entradas: pestado= estado de la maleta
    Salidas: Datos validados
    """
    try:
        int(pestado)
        if pestado=="":
            print("Ingrese un estado por favor.")
        elif not isinstance(pestado,int):
            print("Ingrese un dato de tipo entero")
        elif pestado<0 or pestado>7:
            print("Ingrese un número entre 1 y 6")
        else:
            return pestado
        pedirEstado()
    except:
        print("Ingrese un número de tipo entero")
        return pedirEstado()
def pedirEstado():
    """
    Funcionalidad: Pedir el estado de la maleta
    Entradas:NA
    Salidas:Datos en pantalla
    """
    pestado=input("Ingrese el estado de la maleta: ")
    return validarEstado(pestado)
########################################################
def validarCantidad(num):
    """
    Funcionalidad: Valida los datos para pedirCantidad
    Entradas:num=Cantidad de maletas a registrar
    Salidas: Datos validados
    """
    try:
        int(num)
        if num=="":
            print("Ingrese una cantidad por favor.")
        elif not isinstance(num,int):
            print("Ingrese un dato de tipo entero")
            return pedirCantidad()
        elif num<0:
            print("La cantidad debe ser un número positivo")
            return pedirCantidad()
        else:
            return num
    except ValueError:
        print("Ingrese un dato de tipo entero")
        return pedirCantidad()
    except:
        print("Ingrese un dato de tipo entero positivo")
        return pedirCantidad()
def pedirCantidad():
    """
    Funcionalidad: Pedir la cantidad de maletas a registrar
    Entradas:NA
    Salidas: Datos en pantalla
    """
    num=input("Ingrese la cantidad de maletas a registrar: ")
    return validarCantidad(num)
#####################   Metodos   ###################################
def registrarMaleta(vuelos):
    """
    Funcionalidad: Crear maletas
    Entradas: cantidad de maletas a crear
    Salidas: Maleta creada
    """
    num=pedirCantidad() #Problemas con la validación
    for i in range(num):
        print("Maleta #",i+1)
        nombre=Maleta()
        pcodigo=pedirCodigo()
        nombre.asignarCodigo(pcodigo)
        ppeso=pedirPeso() #Problemas con la validación
        nombre.asignarPeso(ppeso)
        ptamanno=pedirTamanno()
        nombre.asignarTamanno(ptamanno)
        pfragilidad=pedirFragilidad()
        nombre.asignarFragilidad(pfragilidad)
        pdescripcion=pedirDescripcion()
        nombre.asignarDescripcion(pdescripcion)
        pestado=pedirEstado() #Problemas con la validación
        nombre.asignarEstado(pestado)
        vuelos.append(nombre)
        print("Maleta registrada de manera exitosa")
    return 
def eliminarMaleta(codigo):
    """
    Funcionalidad: Eliminar una maleta de la lista
    Entradas: codigo= codigo de la maleta a eliminar
    Salidas: Maleta eliminada
    """
    for maleta in vuelos:
        if codigo==maleta.codigo:
            vuelos.remove(maleta)
        else:
            print("La maleta no se encuentra en el registro")
    return vuelos
def modificarMaleta(maleta):
    """
    Funcionalidad: Modifica los datos de la maleta solicitada (menos el codigo)
    Entradas: maleta a modificar
    Salidas: 
    """
def consultar(dato):
    """
    Funcionalidad: Consulta por maletas tanto por vuelo como por persona
    Entradas:
    Salidas: Datos solicitados en pantalla
    """
def subMenu():
    """
    Funcionalidad: Muestra el submenú de la opción consultar
    Entradas:NA
    Salidas:Datos en pantalla
    """
    print("1.Consultar por avión\n2.Consultar por persona")
    try:
        opcion=int(input("Ingrese la opción seleccionada: "))
        if opcion==1:
            #aqui va el de por avión
        elif opcion==2:
            #aqui va el por persona
        else:
            print("Ingrese una opción que se encuentre en el menú")
        subMenu()
    except ValueError:
        print("Ingrese un dato de tipo entero.")
    except:
        print("Ingrese un dato válido.")
    subMenu()
def menu():
    """
    Funcionalidad:Muestra el menú principal
    Entradas:NA
    Salidas:Datos en pantalla
    """
    print("Bienvenido\nPor favor seleccione una opción del menú\n1.Registrar una maleta\n2.Eliminar una maleta\n3.Modificar una maleta\n4.Consultar por...")
    try:
        opcion=int(input("Ingrese la opción seleccionada: "))
        if opcion==1:
            registrarMaleta(vuelos)
        elif opcion==2:
            eliminarMaleta(codigo)
        elif opcion==3:
            modificarMaleta(maleta)
        elif opcion==4:
            subMenu()
        else:
            print("Ingrese una opción que se encuentre en el menú)
        menu()
    except ValueError:
        print("Ingrese un dato de tipo entero")
    except:
        print("Ingrese un tipo de dato válido")
#menu()
def confirmarSalir():
    """
    Funcionalidad: Pide la confirmación de la salida
    Entradas:NA
    Salidas:Si sale o no
    """
    try:
        print("Está seguro que desea salir?\n\n1.Sí\n2.No")
        opcion=int(input("Ingrese la opción selccionada: "))
        if opcion==1:
            return #Funcion de salir
        elif opcion==2:
            return #Funcion para volver al menú
        else:
            print("Ingrese una opción, ya sea 1 o 2.")
    except ValueError:
        print("Ingrese un dato de tipo entero")
    except:
        print("Ingrese un dato válido")

def confirmarEliminar():
    """
    Funcionalidad: Pide la confirmación de la función para eliminar
    Entradas:NA
    Salidas:Si se borra o no
    """
    try:
        print("Está seguro que desea borrar la maleta?\n\n1.Sí\n2.No")
        opcion=int(input("Ingrese la opción selccionada: "))
        if opcion==1:
            return #Funcion de borrar
        elif opcion==2:
            return #Funcion para volver al menú
        else:
            print("Ingrese una opción, ya sea 1 o 2.")
    except ValueError:
        print("Ingrese un dato de tipo entero")
    except:
        print("Ingrese un dato válido")
    




        
#PP
