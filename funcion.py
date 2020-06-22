#Creado por: Gilbert Rodríguez Mejias y Raúl Sanabria Marroquín
#Fecha de creación: 16/03/2020 1:00p.m
#Última modificacion: 05/06/2020 5:46p.m
#Version 3.8.1

#Importacion de librerias

#--------------------------------------------Funcion 1----------------------------------------------------#
def formarNumeroInverso(pnumA,pnumB,pnumC):
    """
    funcionalidad: monstrar los numeros que se ingresan al inverso
    Entradas:
    -numA: el primer numero(int) que se ingresa
    -numB: el segundo vnumero(int) que se ingresa
    -numC: el tercero numero(int) que se ingresa
    Salidas:
    - un numero(int)
    """
    if pnumB==0 and pnumC==0:
        resul=pnumA
    elif pnumC==0:
        resul=(pnumB*10**1)+pnumA
    else:
        resul=(pnumC*10**2)+(pnumB*10**1)+pnumA
    return resul

#--------------------------------------------Funcion 2----------------------------------------------------#:
def obtenerPares(pn):
    """
    funcionalidad: obtener si el numero es par o impar
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Slidas:
    -Ture si el numero es par
    -False si el numero no es par
    """
    if pn%2 ==0:
        return True
    else:
        return False


def ordenarPares(pnum):
    """
    funcionalidad: ordenar los numeros q son pares
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Slidas:
    -resul: los numeros(int) pares que estaban en el numero ingresado
    """
    elevar=0
    resul=0
    while pnum !=0:
        if obtenerPares(pnum%10):
            resul+=(pnum%10)*(10**elevar)
            elevar+=1
        pnum//=10
    return resul
        
#--------------------------------------------Funcion 3----------------------------------------------------#
def obtenerFactorial(pnum):
    """
    funcionalidad: obtener el factorial de el numero dado
    Entradas:
    -num: el numero(int) que ingresa el usuario
    Salidas:
    -resul: El factorial del numero ingresado
    """
    resul=1
    for pnum in range(1,pnum+1):
        resul*=pnum   
    return resul

#--------------------------------------------Funcion 4----------------------------------------------------#
def obtenerCantidades(pnum):
    """
    funcionalidad: acumular los numeros impares
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Salidas:
    -resul: loa numeros impares 
    """
    elevar=0
    resul=0
    while pnum !=0:
        if obtenerPares(pnum%10)==False:
            resul+=(pnum%10)*(10**elevar)
            elevar+=1
        pnum//=10
    return resul

#--------------------------------------------Funcion 5----------------------------------------------------#
def obtenersumatoria(pnum):
    """
    funcionalidad: obtener la sumatoria de el numero dado
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Salidas:
    sumatoria de el numero
    """
    i=1
    resul=0
    while pnum!=0:
       if i<=pnum:
           resul+=i**2
           i+=1
       else:
            return resul
    
#--------------------------------------------Funcion 6----------------------------------------------------#
def convertirABinario(pnum):
    """
    funcionalidad: convertir el numero(int) ingresado a binario
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Salidas:
    numero en binario 
    """
    binario=""
    while pnum // 2 != 0:
        binario = str(pnum % 2) + binario
        pnum = pnum // 2
    return str(pnum) + binario

#--------------------------------------------Funcion 7----------------------------------------------------#
def invertirNumero(pnum):
    """
    funcionalidad: hacer el inverso del numero(int) ingresado
    Entradas:
    -num: el numero(int) que ingresa el usuario 
    Slidas:
    -resul: eñ inverso del numero ingresado
    """
    indice=len(str(pnum))-1
    invertir=0
    while indice>=0:
            invertir+=(pnum%10)*10**indice
            pnum//=10
            indice-=1
    return invertir

#--------------------------------------------Funcion 8----------------------------------------------------#
def obtenerMayor(pnum):
        """
        funcionalidad: obtener los numeros mayores
        Entradas:
        -pnum: el numero(int) que ingresa el usuario 
        Slidas:
        -el numero mayor
        """
        mayor=0
        while pnum > 0:
                num=pnum%10
                if num > mayor:
                        mayor=num
                pnum=pnum//10
        return mayor

def obtenerMenor(pnum):
        """
        funcionalidad: obtener los numeros menores
        Entradas:
        -pnum: el numero(int) que ingresa el usuario 
        Slidas:
        -el numero menor
        """
        menor=10
        while pnum > 0:
                num=pnum%10
                if num < menor:
                        menor=num
                pnum=pnum//10
        return menor

def obtenerDiferencia(pnum):
        """
        funcionalidad: obtener la diferencia entre el numero mayor y menor
        Entradas:
        -pnum: el numero(int) que ingresa el usuario 
        Slidas:
        -la difere4ncia
        """
        diferencia=obtenerMayor(pnum)-obtenerMenor(pnum)
        return diferencia

#--------------------------------------------Funcion 9----------------------------------------------------#
def convertirBinarioADecimal(pnum):
        """
        funcionalidad: cinvertir de binario a decimal
        Entradas:
        -pnum: el numero(int) que ingresa el usuario, este en  binario
        Slidas:
        -el numero representado en decimal 
        """
        decimal=0
        exponente=0
        num=0
        while pnum>0:
                decimal+=(pnum%10)*2**exponente
                exponente+=1
                pnum=pnum//10

        return decimal

#--------------------------------------------Funcion 10---------------------------------------------------#
def convertirDecimalAOctal(pnum):
        """
        funcionalidad: convertir de decimal a octal
        Entradas:
        -pnum: el numero(int) que ingresa el usuario
        Slidas:
        -el numero representado en octal 
        """
        octal=0
        exponente=0
        num=0
        while pnum>0:
                octal+=(pnum%8)*10**exponente
                exponente+=1
                pnum=pnum//8
        return octal

#--------------------------------------------Funcion 11---------------------------------------------------#
def palidromo(pnum):
        """
        funcionalidad: obtener si un numero es palindromo o no
        Entradas:
        -pnum: el numero(int) que ingresa el usuario
        Slidas:
        -True si el numero es palindromo
        -False si el numero no es palindromo 
        """
        palindromo=""
        if invertirNumero(pnum)==pnum:
                palindromo= "True"
        else:
                palindromo= "False"

        return palindromo

#--------------------------------------------Funcion 12---------------------------------------------------#
def diferencia(pnum1, pnum2):
    """
    funcionalidad: obtener los numeros que están en el primer número pero no en el
	segundo número
    Entradas:
    -pnum1: el numero(int) que ingresa el usuario, este se compara con el segundo
    -pnum1: el numero(int) que ingresa el usuario, este sera con el cual se 
    compare el primer numero
    Slidas:
    -Los digitps que estan en el primer numero y no en el segundo
    """
    pnum1=str(pnum1)
    pnum2=str(pnum2)
    nuevoNum=""
    for num in pnum1:
            if num not in pnum2:
                    nuevoNum+=num
    if nuevoNum=="":
            return print(False)
    return nuevoNum

#--------------------------------------------Funcion 13---------------------------------------------------#
def obtenerAnnosBisiestos(pnum1,pnum2):
	"""
	funcionalidad: obtener los annos bisiestos de un determinado rango
	Entradas:
	-pnum1: el numero(int) que ingresa el usuario, el anno inicial
	-pnum1: el numero(int) que ingresa el usuario, el anno final 
	Salidas:
	-Los annos bisiestos
	-No hay annos bisiestos
	"""
	bisiestos=""
	for i in range(pnum1,pnum2+1):
		if annosBisiestos(i):
			bisiesto+=str(i)+"\n"
	if bisiestos=="":
		return print("No hay años bisiestos")
	return bisiestos

def annosBisiestos(anno):
	"""
	funcionalidad: obtener los annos bisiestos de un determinado rango
	Entradas:
	-pnum1: el numero(int) que ingresa el usuario, el anno inicial
	-pnum1: el numero(int) que ingresa el usuario, el anno final 
	Slidas:
	-Los annos bisiestos
	-No hay annos bisiestos
	"""
	if anno%4==0:
		return True
	else:
		return False














    
