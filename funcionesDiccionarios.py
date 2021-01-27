#Elaborado por: AAAA
#Fecha de creación: 8/5/2019 7:45am
#Última modificación: 9/5/2019 5:00pm
#Versión: 3.7.2

#Importación de diccionarios
import pickle

#Funciones Globales
diccItems={}
#Definición de Funciones

def grabarArchivo(pnombreArchivo,plista):
    """
    Función: Graba el diccionario en el archivo seleccionado
    Entradas: Nombre del archivo(binario), lista(diccionario)
    Salidas: Grabación del archivo (binario)
    """
    try:
        print("Se va a abrir el archivo: ", pnombreArchivo)
        access=open(pnombreArchivo,"wb")
        print("Se va a grabar el archivo: ", pnombreArchivo)
        pickle.dump(plista,access)
        print("Se va a cerrar el archivo: ", pnombreArchivo)
        access.close()
    except:
        print("Error al grabar el archivo: ", pnombreArchivo)
    return

def leerArchivo(pnombreArchivo):
    """
    Función: Cargar y leer datos del archivo seleccionado
    Entradas: Nombre del archivo (binario)
    Salidas: NA
    """
    try:
        print("Se va a abrir el archivo: ", pnombreArchivo)
        f=open(pnombreArchivo,"rb")
        print("Se va a leer el archivo: ", pnombreArchivo)
        pickle.load(f)
        print("Se va a cerrar el archivo: ", pnombreArchivo)
        f.close()
    except:
        return{}
    return

def agregarItem(diccItems):
    """
    Función: Añadir los datos de un producto a un diccionario
    Entradas: pcodigo(alphanumérico), pnombre(str),pingredientes(str),pprecio(int)
    Salidas: diccItems(diccionario)
    """
    try:
        pcodigo = input("Por favor, ingrese el código del producto. Ejm (MDXX)")
        pnombre = input("Por favor, ingrese el nombre del producto.")
        pingredientes = input("Por favor, ingrese los ingredientes del producto.") 
        pprecio = int(input("Por favor, ingrese el precio del producto (en colones)."))
        datosItem=[pnombre,pingredientes,pprecio]
        diccItems[pcodigo] = datosItem
        grabarArchivo("inventario.py",diccItems)
        return diccItems
    except:
        return print ("Error al ingresar el producto, asegurese de ingresar solo números enteros para el precio")
def eliminarItem(diccItems,pcodigo):
    """
    Función: Eliminar un item específico
    Entradas: diccItems(diccionario),pcodigo(str)
    Salidas: diccItems(diccionario)
    """
    try:
        del(diccItems[pcodigo])
        grabarArchivo("inventario.py",diccItems)
        print("Se ha eliminado el producto:",pcodigo)
    except:
        return print("Error al eliminar el producto. Asegurese de que el código que digitó sea el correcto")
    
    
def mostrarItem(diccItems,pcodigo):
    """
    Función: Mostrar un item específico del diccionario
    Entradas: diccItems(diccionario),pcodigo(str)
    Salidas: pcodigo(str), pnombre(str),pingredientes(str),pprecio(str)
    """
    try:
        if pcodigo in diccItems:
            infoproducto=diccItems[pcodigo]
            print("Código:",pcodigo)
            print("Nombre:",infoproducto[0])
            print("Ingredientes:",infoproducto[1])
            print("Precio",infoproducto[2])
            print ("-------------------")
    except:
        return print("Error al encontrar el producto. Asegurese de que el código que digitó sea el correcto")
    
    return

def mostrarTodosItems(diccItems):
    """
    Función: Mostrar todos los items del diccionario
    Entradas: diccItems(diccionario)
    Salidas: diccItems(diccionario),pcodigo(str), pnombre(str),pingredientes(str),pprecio(str)
    """
    pllaves=list(diccItems.keys())
    try:
       for llave in pllaves:
            mostrarItem(diccItems,llave)
    except:
        print("No hay productos registrados")
            
    


    
