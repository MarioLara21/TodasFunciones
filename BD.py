#Elaborado por: XyY
#Fecha de creación: 6/11/2019, 5:00pm
#Última modificación: 8/11/2019, 7:00 pm
#Versión: 3.5.2


#importación de libreriasBD
import sys 
import pickle

#Definición de funciones

def leerArchivo():
    
    """
    Funcionalidad: Responsable de ver si existe un archivo y si existe, de leerlo.
    Entradas:
    -NA
    Salidas:
    -universidad(lista), lista con los datos de las personas registradas en el paro.
    """
    try:
      universidad=[]
      lista=open("universidad.dat","rb")
      universidad=pickle.load(lista)
      lista.close()
      return universidad
    except:
      universidad=[]
      return universidad

    
def grabarArchivo(x):
    """
    Funcionalidad: Responsable de grabar datos en un diccionario.
    Entradas:
    -x(lista), lista con los datos de las personas registradas en el paro.
    Salidas:
    -universidad(lista), lista con los datos de las personas registradas en el paro.
    """
    lista=open("universidad.dat","wb")
    universidad=x
    pickle.dump(universidad,lista)
    lista.close()
    return universidad
