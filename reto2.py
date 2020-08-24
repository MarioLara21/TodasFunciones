#Creado por Leonardo Fariña y Mario Larajry
#Creación: 15/03/2020 10:50am
#Modificación: 15/03/2020 11:20am
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def obtenerPares (numP1):
    '''
    Funcionalidad: Devolver un numero con todos los digitos pares en orden ej:(Ent:1234->Sal:24) 
    Entradas: numP1 validado por obtenerParValid
    Salidas: numSalidaTot es el numero de todos los digitos pares de numP1 en orden ej:(Ent:1234->Sal:24)
    '''
    miDigit=0
    numSal=0
    numSalTot=0
    while numP1!=0:
        miDigit= numP1%10
        if (miDigit%2)==0:
            numSal= (str(miDigit)+str(numSal))
        numP1 = numP1 // 10
    numSalidaTot= int(numSal)//10
    return numSalidaTot

def obtenerParValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numP1 salida de numero que cumplen el requisito de ser un número mayor a 0
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerPares(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'
    
#Programa Principal

num0=(input("Escriba el número para ver la magia: "))
print(obtenerParValid(num0))
 
