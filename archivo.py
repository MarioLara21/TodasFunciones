#Realizado por: XyY
#Fecha de creación: 24/5/2019 9:10 pm
#Última actualización: 6/6/2019 4:40 pm
#Versión 3.7.2

#Importación de librerías
import pickle

#Definición de funciones

def graba(parchivo,plista):
    """
    Función: Grabar la lista ingresada en un archivo
    Entrada: Nombre del archivo (string) y la lista (list)
    Salida: Archivo con modificaciones
    """
    try:
        f=open(parchivo,"wb")
        print("Se grabará el archivo:",parchivo)
        pickle.dump(plista,f)
        print("Se cerrará el archivo:",parchivo)
        f.close()
    except:
        print("Error al grabar el archivo:",parchivo)
    return

def lee(parchivo):
    """
    Función: Cargar (leer) la información almacenada en el archivo
    Entrada: Archivo a solicitar
    Salida: Lista con el contenido del archivo (list)
    """
    try:
        f=open(parchivo,"rb")
        print("Se leerá el archivo:",parchivo)
        lista=pickle.load(f)
        print("Se cerrará el archivo:",parchivo)
        f.close()
        return lista
    except:
        print("Error al leer el archivo:",parchivo)
        return [] #Modificado para que en caso de que el archivo no exista devuelva una lista vacía


    
   


