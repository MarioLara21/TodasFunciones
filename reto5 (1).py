#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 13:10pm
#Modificación: 15/03/2020 13:27pm
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def obtenerSumatoria (numP1):
    '''
    Funcionalidad: Devolver la sumatoria Z de i**2 empezando desde 1 hasta numP1
    Entradas: numP1 validado por obtenerSumValid
    Salidas: numSal es la sumatoria Z de i**2 empezando desde 1 hasta numP1
    '''
    numSal=0
    cont=1
    while cont <= numP1:
        if cont <= numP1:
            numSal=(numSal)+(cont**2)
            cont+=1
    return numSal

def obtenerSumValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: ejecucion de la funcion obtenerSumatoria(numP1) con el numero validado
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerSumatoria(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'
    
#Programa Principal

num0=(input("Escriba el número para ver la magia: "))
print(obtenerSumValid(num0))
 
