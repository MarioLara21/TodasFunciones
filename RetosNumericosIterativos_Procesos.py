#Hecho por Leonardo Fariña
#Fecha de creacion 02/05/2020 21:38 pm
#Fecha de modificacion 03/05/2020 15:39 pm

#Version de python 3.8.2
#Estaes mi libreria de los retos numericos iterativos
#Estas son sus funciones
'''
help(diferenciaEntreValores)
help(convertBinADecim)
help(convertDecimAOctal)
help(numPalind)
help(diferenciaDigitos)
help(bisiestos)
'''

#Funciones

def diferenciaEntreValoresEntrSalid():
    '''
    Entradas : Entrada y salida
    Funcionalidad : Ingresar un numero y llamar a la funcion diferenciaEntreValoresValida con ese numero e imprimir
    Salida :"El número mayor es: ",mayor,", El número menor es: ",menor,", La diferencia es: ",mayor - menor
    '''
    
    numIns = input("Ingrese un numero: ")
    mayorYmenor = diferenciaEntreValoresValida(numIns)

    print("llego")
    return print("El número mayor es: ",mayorYmenor[0],", El número menor es: ",mayorYmenor[1],", La diferencia es: ",mayorYmenor[0]-mayorYmenor[1])
     
    

def diferenciaEntreValoresValida(numero):
    '''
    Entradas : numero (cualquier cosa)
    Funcionalidad : Validar que numero es un entero y llamar a la funcion diferenciaEntreValores
    Salida : Error o diferenciaEntreValores
    '''
    while True:
        try:
            
            numeroValidado = int(numero)        
            assert numeroValidado > 9

            return diferenciaEntreValores(numeroValidado)
        
        except ValueError:        
            print("Debe ingresar un número entero")      
            diferenciaEntreValoresEntrSalid()    
        except AssertionError:        
            print("Debe ingresar un número entero")        
            diferenciaEntreValoresEntrSalid()
        except :        
            print("Debe ingresar un número con más de dos dígitos")
            diferenciaEntreValoresEntrSalid()
        return 4,2


def diferenciaEntreValores(numero):
    '''
    Entradas : Numero mayor a 9
    Funcionalidad : Ingresar un numero, decir cual es el digito mayor,el menor y la diferencia entre el mayor y el menor
    Salida : (mayor,menor) devuelve una tupla
    '''
    listDeNum = str(numero)
    contDeIter =  len(listDeNum) - 1
    
    while contDeIter >= 0:
        
        if listDeNum[contDeIter] == max(listDeNum):
            mayor = int(listDeNum[contDeIter])

        elif listDeNum[contDeIter] == min(listDeNum):
            menor = int(listDeNum[contDeIter])
        contDeIter -= 1
    
    return mayor,menor
   


def convertBinADecim(numero):
    '''
    Entradas : Numero en binario
    Funcionalidad : Ingresar un numero binario y convertirlo a decimal
    Salida : "Su número convertido a decimal es: " numEnDec
    '''
    try:
        
        #Creamos una lista de nuestro numero
        listDeNum = list(numero)
        
        #Hacemos un contador con la cantidad de digitos de nuestro numero
        contDeIter =  int(len(listDeNum) - 1)

        #Variables de nuestro numEnDec y la potencia 
        numEnDec = 0
        potencia = 0

        #Iteramos en nuestro contador
        while contDeIter >= 0:

            #Si el numero es diferente a 1 o 0 no es binario
            if (int(listDeNum[contDeIter]) != 1)and(int(listDeNum[contDeIter]) != 0) :
                print("Debe ingresa un número en binario.")
                numIns = input("Ingrese un número binario: ")
                convertBinADecim(numIns)
                return

            #Si el numero es 1, se suma 2 por la potencia
            if int(listDeNum[contDeIter]) == 1:
                numEnDec += (2**potencia)
                
            potencia += 1
            contDeIter -= 1
            
        print("Su número convertido a decimal es: ",numEnDec)
        
        return
    
    except ValueError:
        
        print("Debe ingresar un número entero")
        numIns = input("Ingrese un numero binario: ")
        convertBinADecim(numIns)
        
        return
    
    except:
        
        print("Debe ingresar un número binario")
        numIns = input("Ingrese un numero binario: ")
        convertBinADecim(numIns)
        
        return

def convertDecimAOctal(numero):
    '''
    Entradas : Numero en decimal entero positivo
    Funcionalidad : Ingresar un numero y convertirlo a octal
    Salida : "Su número convertido a octal es: " numEnOct
    '''
    try:
        #Variable de nuestro numero(para que no se enrede)
        numAconv = int(numero)

        #Verificamos que sea >= 0
        assert numAconv >= 0
                
        numEnOct = ""

        #Iteramos en el numero      
        while numAconv >= 0:
                            
            residuo = numAconv % 8
            cociente = numAconv // 8

            #Le sumamos el residuo 
            numEnOct = str(residuo) + numEnOct
            
            numAconv = cociente

            #Salimos del while
            if numAconv == 0:
                numAconv -=1   
            
        print("Su número convertido a octal es: ", str(numEnOct))
        
        return
    
    except ValueError:
        
        print("Debe ingresar un número entero")
        numIns = input("Ingrese un numero: ")
        convertDecimAOctal(numIns)
        
        return

    except AssertionError:

        print("Debe ingresar un número mayor o igual a 0")
        numIns = input("Ingrese un numero: ")
        convertDecimAOctal(numIns)
        
        return
        
    except:
        
        print("Debe ingresar un número")
        numIns = input("Ingrese un numero: ")
        convertDecimAOctal(numIns)
        
        return

def numPalind(numero):
    '''
    Entradas : Numero enteros positivos mayores a 9
    Funcionalidad : Ingresar un numero y verificar si es palíndromo
    Salida : "Su numero es palíndromo" o "Su numero no es palíndromo" 
    '''
    try:
        #Le asignamos una variable a nuestro numero(para que no se enrede)
        numAconv = numero

        #Verificamos que sea mayor a 9
        assert int(numAconv) > 9

        #Creamos una lista con nuestro numero
        listDeNum = list(numAconv)

        #Creamos un contador con la cantidad de digitos
        contadItera = int(len(listDeNum)) - 1
                
        numeroPalin = ""

        #Iteramos en nuestro contador
        while contadItera >= 0:
            
            #Damos vuelta el numero entregado
            numeroPalin += str(listDeNum[contadItera])
            
            contadItera -= 1

        #Salidas   
        if numero == numeroPalin:
            print("Su numero es palíndromo")
        else:
            print("Su numero no es palíndromo")
            
        return
        
    except ValueError:
        
        print("Debe ingresar un número entero")
        numIns = input("Ingrese un numero: ")
        numPalind(numIns)
        
        return
    
    except AssertionError:
        
        print("Debe ingresar un número mayor a 9")
        numIns = input("Ingrese un numero: ")
        numPalind(numIns)
        
        return

    except:
        
        print("Debe ingresar un número")
        numIns = input("Ingrese un numero: ")
        numPalind(numIns)
        
        return




def diferenciaDigitos(numero,numero2):
    '''
    Entradas : Numero y numero2 (numeros enteros)
    Funcionalidad : Recibe dos números enteros positivos y retorna otro número que corresponde a aquellos dígitos que están en el primer número pero no en el segundo número
    Salida : "Dígitos diferentes:",numConDif o "No tiene digitos diferentes" 
    '''
    try:
        #Primero le damos unas variables a los numeros ingresados(para que no se enreden con otras cosas)
        numAconv = numero
        numAconv2 = numero2

        #Verificamos que sean mayores o iguales a 0
        assert int(numero) > 0
        assert int(numero2) > 0

        #Creamos la listas para poder comparar los digitos del 2° numero con el 1° numero
        listDeNum = list(numAconv)
        listDeNum2 = list(numAconv2)

        #Creamos un contador para cada numero y poder elegir un elemento de nuestro numero(en este caso yo voy del mas grande al mas chico)
        contadItera = int(len(listDeNum)) - 1
        contadItera2 = int(len(listDeNum2)) - 1

        #Variable donde guardamos nuestro primer numero        
        numConDif = str(numero)

        #Iteramos la cantidad de caracteres de nuestro segundo numero        
        while contadItera2 >= 0 :
            
            contadItera = int(len(listDeNum)) - 1

            #Iteramos la cantidad de caracteres de nuestro primer numero 
            while contadItera >= 0:

                #Nos fijamos si los valores coinciden(si un elemento del segundo numero coincide con uno del primer numero)
                if listDeNum[contadItera] == listDeNum2[contadItera2]:
                    
                    #Con replace remplazamos el numero que aparece en el primer numero 
                    digitoAsacar = str(listDeNum[contadItera])
                    numConDif = numConDif.replace(digitoAsacar,"")
                                    
                contadItera -= 1
    
            contadItera2 -= 1

        #Salidas    
        if numConDif == "":
            print("No tiene digitos diferentes")
        else:
            print("Dígitos diferentes:",numConDif)
            
        return

        
    except ValueError:
        
        print("Debe ingresar números enteros")
        numIns = input("Ingrese el primer numero: ")
        numIns2 = input("Ingrese el segundo numero: ")
        diferenciaDigitos(numIns,numIns2)
        
        return
    
    except AssertionError:
        
        print("Debe ingresar números mayor a 0")
        numIns = input("Ingrese el primer numero: ")
        numIns2 = input("Ingrese el segundo numero: ")
        diferenciaDigitos(numIns,numIns2)
        
        return
    
    except:
        
        print("Debe ingresar números")
        numIns = input("Ingrese el primer numero: ")
        numIns2 = input("Ingrese el segundo numero: ")
        diferenciaDigitos(numIns,numIns2)
        
        return


def bisiestos(añoI , añoFi):
    '''
    Entradas : añoI Y añoF(numeros enteros)
    Funcionalidad : Ingresar un año de inicio y un año final y calcular los años bisiestos entre esos años
    Salida : "Años bisiestos: " ,años bisiestos O "No hay años bisiestos"
    '''
    try:
        #Definimos variables con los años (para no enredarlos)
        año = int(añoI)
        añoF = int(añoFi)

        #Verificamos que el año de inicio sea menor que el año final
        assert año < añoF

        #Variable de confirmacion de año bisiesto y una lista donde se guardaran los años bisiestos(esto se hace por comodidad,si quisiera usar esa lista en el futuro)
        confirm = False               
        listAñoBis = []

        #Iteramos sobre la cantidad de años iniciales y le vamos sumando 1 hasta el año final       
        while año <= añoF:
            
            confirma = (año / 4)
            
            #Corroboramos que sea divisible por 4
            if confirma == (año//4) :
                listAñoBis.append( "                   "+ str(año)+"\n")
                confirm = True
            
            año += 1
            
        #Confirmamos si se detectaron años bisiestos
        if confirm == True:
            print("               Años bisiestos: ")
            print("".join(listAñoBis))
        else:
            print("No hay años bisiestos")
            
        return
    
    except ValueError:
        
        print("Debe ingresar años")
        numIns = input("Año de inicio: ")
        numIns2 = input("Año final: ")
        bisiestos(numIns,numIns2)
        
        return
    
    except AssertionError:
        
        print("Ingrese un año de inicio menor que el año final")
        numIns = input("Año de inicio: ")
        numIns2 = input("Año final: ")
        bisiestos(numIns,numIns2)
        
        return
    
    except:
        
        print("Ingrese un año de inicio menor que el año final o diferente")
        numIns = input("Año de inicio: ")
        numIns2 = input("Año final: ")
        bisiestos(numIns,numIns2)
        
        return



