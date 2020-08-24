#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 13:28pm
#Modificación: 15/03/2020 14:49pm
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def convertirABinario (numP1):
    '''
    Funcionalidad: convertir el numero de entrada a binario
    Entradas: numP1 numero entero 
    Salidas: numConBin() numP1 converitdo a numero binario
    '''
    numConBin=0
    while numP1!=0:
        if numP1>0:
            digBin=numP1%2
            numConBin=str(digBin)+str(numConBin)
            numP1=numP1//2
    numConBin=int(numConBin)//10
    return  numConBin


def obtenerSumValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numConBin(numP1)Validado
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return convertirABinario(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'
    
#Programa Principal

num0=(input("Escriba el número para ver la magia: "))
print(obtenerSumValid(num0))
 
