#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 11:23am
#Modificación: 15/03/2020 11:57am
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def obtenerFactorial (numP1):
    '''
    Funcionalidad: Devolver el factorial del numero de entrada 
    Entradas: numP1(digito ingresado por el usuario) validado por obtenerFactorialValid
    Salidas: numSalidaTot es el factorial del numero de entrada numP1
    '''
    numSal=1
    cont=1
    while cont <= numP1:
        if cont <= numP1:
            numSal=numSal*cont
            cont+=1
    return numSal

def obtenerFacValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numP1 salida de un numero que cumplen el requisito de ser un número entero natural
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerFactorial(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'
    
#Programa Principal

num0=(input("Escriba el número para ver la magia(se recomiendan numeros menores a 100): "))
print(obtenerFacValid(num0))
 
