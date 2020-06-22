#Elaborado por: Gilbert Rodríguez Mejias
#Fecha de creacion: 06/04/20 3:55 p.m
#Ultima modificacion: 16/04/20 12:28 p.m
#Version: 3.8.1

#importar librerias

#Funciones

#----------------------------------Ejercicio 1-------------------------------------#

def cuentaNum( ppalabra):
    """
    Funcionamiento: para obtener la suma de numeros si hay en una palabra
    Entradas:
    -palabra(str): la palabra que ingresa el usuario
    Salidas: la suma de los numeros que se encontraron en esa palabra
    """

    cuenta=0
    for carac in ppalabra:
    	if carac.isdigit():
    		cuenta+=int(carac)
    return cuenta



#----------------------------------Ejercicio 2-------------------------------------#

def cantidadLetras(ppalabra):
    """
    Funcionamiento: para contar la cantidad de vocales(estas una por una) y consonantes que tiene una palabra
    Entradas:
    -palabra(str): la palabra que ingresa el usuario
    Salidas: cantidad de vocales y consonantes de esa palabra
    """

    vocalA=0
    vocalE=0
    vocalI=0
    vocalO=0
    vocalU=0
    consonante=0
    for carac in ppalabra:
        if carac =="a":
            vocalA+=1
        elif carac =="e":
            vocalE+=1
        elif carac =="i":
            vocalI+=1
        elif carac =="o":
            vocalO+=1
        elif carac =="u":
            vocalU+=1
        else:
            consonante+=1

    print("Cantidad de a:", vocalA)
    print("Cantidad de e:", vocalE)
    print("Cantidad de i:", vocalI)
    print("Cantidad de o:", vocalO)
    print("Cantidad de u:", vocalU)
    print("Cantidad de consonantes:", consonante)

    return ""




#----------------------------------Ejercicio 3-------------------------------------#

def invertir(ppalabra):
    """
    Funcionamiento: invertir una palabra
    Entradas:
    -palabra(str): la palabra que ingresa el usuario
    Salidas: la palabra invertida
    """

    indice=len(ppalabra)-1
    inver=""
    while indice >= 0:
        inver+=ppalabra[indice]
        indice-=1
    return inver


def confirmarPalindroma(ppalabra):
    """
    Funcionamiento: encontrar si una palabra es palindroma
    Entradas:
    -el return de la funcion invertir
    Salidas: si la palabra es o no palindroma
    """
    palindroma=""

    if invertir(ppalabra) == ppalabra:
        palindroma= "True"
    else:
        palindroma= "False"

    return palindroma



#----------------------------------Ejercicio 4-------------------------------------#

def reconocerVocales(ppalabra):
    """
    Funcionamiento: reconocer las vocales y eliminarlas de la oracion
    Entradas:
    -palabra(str): la palabra que ingresa el usuario
    Salidas: 
    """
    palabraSinVocales=""
    for letra in ppalabra:
        if letra.lower() not in "aeiou":
            palabraSinVocales+=letra
    return palabraSinVocales




#----------------------------------Ejercicio 5-------------------------------------#
"""
Reutilizar funcion invertir
"""
#----------------------------------Ejercicio 6-------------------------------------#

def cantidadDePalabras(poracion):
    """
    Funcionamiento: contar cuantas palabras hay en una oracion
    Entradas:
    -la oracion ingresa por le usuario
    Salidas: la cantidad de palabras que tiene la oracion
    """
    cantPalabras=1
    for carac in poracion:
        if carac == " ":
            cantPalabras+=1
    return cantPalabras






