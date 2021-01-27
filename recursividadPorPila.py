#Creado por Mario Lara y Leonardo Fariña
#Fecha de creación 24/07/2020 14:00 pm 
#Última modificación 24/07/2020 18:24 pm
#Versión 3.8.3
#Importación de librerías


#Definicion de funciones
#--------------------------------------------------
def encontrarCero(num):
    '''
    Entrada: num(int)
    Funcionalidad: Encontrar si tiene un cero
    Salida: True o False
    '''
    if num%10 == 0:
        return True
    elif num > 9:
        return not False and encontrarCero(num//10)
    else:
        return False
def validarNum(num):
    '''
    Entrada: num numero a validar
    Funcionalidad: Validar num para encontrarCero
    Salida: Mensaje de error o encontrarCero(num)
    '''
    try:        
        if not isinstance(num,int):
            return "Debe indicar un número entero."
        num = int(num)
        assert 0 < num
        return encontrarCero(num)
    except:
        return "Debe indicar un número entero mayor a CERO."
def encCero(num):
    '''
    Entrada: num
    Funcionalidad: Llamar a validarNum 
    Salida: salida(bool)
    '''
    salida = validarNum(num)
    return salida
#--------------------------------------------------
def parPorRec(num):
    '''
    Entrada: num(int)
    Funcionalidad: Indicar si al menos hay una cifra par
    Salida: True o False
    '''
    if num%2 == 0:
        return True
    elif num > 9:
        return not False and parPorRec(num//10)
    else:
        return False
def validarPar(num):
    '''
    Entrada: num numero a validar
    Funcionalidad: validar num para parPorRec
    Salida: Mensaje de error o parPorRec(num)
    '''
    try:        
        if isinstance(num,float):
            return "Debe indicar un número entero."
        num = int(num)
        assert 0 < num
        if parPorRec(num) == True:
            return "La cifra numérica, posee al menos un par"
        return "La cifra numérica no posee ningún par."
    except:
        return "El valor ingresado debe corresponder a un número únicamente."
def encontrarPar(num):
    '''
    Entrada: num
    Funcionalidad: Llamar a validarPar
    Salida: salida(bool)
    '''
    salida = validarPar(num)
    return salida
#--------------------------------------------------
def sumPorRec(num):
    '''
    Entrada: num(int)
    Funcionalidad: Sumar las cifras del número
    Salida: El resultado de la suma
    '''
    if num == 0:
        return num
    return num%10 + sumPorRec(num//10)
def validarSum(num):
    '''
    Entrada: num numero a validar
    Funcionalidad: Validar num para sumPorRec
    Salida: Mensaje de error o sumPorRec(num)
    '''
    try:        
        if isinstance(num,float):
            return "Debe indicar un número entero."
        assert 0 < num
        num = int(num)
        return "La suma es de : "+str(sumPorRec(num))
    except:
        return "Debe indicar un número entero."
def hacerSum(num):
    '''
    Entrada: num 
    Funcionalidad: Llamar a validarSum
    Salida: salida(int), la suma de las cifras de num
    '''
    salida = validarSum(num)
    return salida
#--------------------------------------------------
def mulImpPorRec(num,veri=0):
    '''
    Entrada: num(int),veri(int)
    Funcionalidad: Multiplicar las cifras impares de num
    Salida: La multiplicacion de las cifras impares de num
    '''
    if (num%10)%2 != 0:
        veri = 1
        return num%10 * mulImpPorRec(num//10,veri)
    elif num > 9:
        return mulImpPorRec(num//10,veri)
    if veri == 1:
        return 1
    return 0
def validarMulImp(num):
    '''
    Entrada: num numero a validar
    Funcionalidad: Validar num para mulImpPorRec
    Salida: Mensaje de error o mulImpPorRec(num)
    '''
    try:        
        if isinstance(num,float):
            return "Debe indicar un número entero."
        assert 0 < num
        num = int(num)
        return "La multiplicación impar es: "+str(mulImpPorRec(num))
    except:
        return "El valor ingresado debe corresponder a un número únicamente."
def hacerMulImp(num):
    '''
    Entrada: num
    Funcionalidad: Llamar a validarMulImp
    Salida: La multiplicación de las cifras impares de num
    '''
    salida = validarMulImp(num)
    return salida
#--------------------------------------------------
def encontrarGran(num,gran=0):
    '''
    Entrada: num(int),gran(int)
    Funcionalidad: Obtener el digito mas grande de num
    Salida: El digito mas grande de num
    '''
    if num == 0:
        return gran
    if num%10 >= gran:
        newGra = num%10
        return encontrarGran(num//10,newGra)
    return encontrarGran(num//10,gran)
def validarEncGra(num):
    '''
    Entrada: num, numero a validar
    Funcionalidad: Validar num para encontrarGran
    Salida: Mensaje de error o encontrarGran(num)
    '''
    try:        
        if isinstance(num,float):
            return "Debe indicar un número entero."
        assert 0 < num
        num = int(num)
        return "El más grande es: "+str(encontrarGran(num))
    except:
        return "El valor ingresado debe corresponder a un número únicamente."
def pedirNumGran(num):
    '''
    Entrada: num
    Funcionalidad: Llamar validarEncGra
    Salida: El digito mas grande de num
    '''
    salida = validarEncGra(num)
    return salida
#--------------------------------------------------
def encontrarDig(num,dig):
    '''
    Entrada: num(int),dig(int)
    Funcionalidad: Contar cuantas veces esta el digito dig en num
    Salida: La cantidad de veces que el digito dig esta en num
    '''
    if num == 0:
        return 0
    if num%10 == dig:
        return 1 + encontrarDig(num//10,dig)
    return encontrarDig(num//10,dig)
def validarEncDig(num,dig):
    '''
    Entrada: num,numero a validar ,dig, digito a validar
    Funcionalidad: Validar num y dig para encontrarDig
    Salida: Mensaje de error o encontrarDig(num,dig)
    '''
    try:        
        if isinstance(num,float) or isinstance(dig,float):
            return "Debe indicar un número entero."
        assert 0 < num and 0 <= dig < 10
        num = int(num)
        dig = int(dig)        
        return "Digito a buscar :"+str(dig)+" Salida :"+str(encontrarDig(num,dig))
    except:
        return "Ingrese un número y un digito positivo."
def buscarDig(num,dig):
    '''
    Entrada: num,dig
    Funcionalidad: Llamar a validarEncDig
    Salida: La cantidad de veces que el digito dig esta en num
    '''
    salida = validarEncDig(num,dig)
    return salida
#--------------------------------------------------
def formarNumero(num,aum=0):
    '''
    Entrada: num(int),aum(int)
    Funcionalidad: Formar un número con los digitos pares de num
    Salida: Numero con los digitos pares de num
    '''
    if num == 0:
        return 0
    if (num%10)%2 == 0:
        return (num%10)*10**aum +(formarNumero(num//10,aum+1))
    else:
        return formarNumero(num//10,aum)
def validarHacPar(num):
    '''
    Entrada: num, numero a validar
    Funcionalidad: Validar num para formarNumero
    Salida: Mensaje de error o formarNumero(num)
    '''
    try:        
        if isinstance(num,float):
            return "El número debe ser entero."
        num = int(num)
        if num < 0:
            num = num * -1
        return formarNumero(num)
    except:
        return "El número debe ser entero."
def hacerPar(num):
    '''
    Entrada: num
    Funcionalidad: Llamar a validarHacPar
    Salida: Numero con los digitos pares de num
    '''
    salida = validarHacPar(num)
    return salida
#--------------------------------------------------
def esNumeroPrimo(num,veri=2):
    '''
    Entrada: num(int),veri(int)
    Funcionalidad: Verificar si un numero es primo
    Salida: True o False
    '''
    if num == 0:
        return 0
    if num != veri:
        if num%veri == 0:
            return False
    if veri == 9 :
        return True
    return True and esNumeroPrimo(num,veri+1)
def validarPrimo(num):
    '''
    Entrada: num, numero a validar 
    Funcionalidad: Validar num para esNumeroPrimo
    Salida: Mensaje de error o esNumeroPrimo(num)
    '''
    try:        
        if isinstance(num,float):
            return "El número debe ser entero."
        num = int(num)
        assert 1 < num
        
        return esNumeroPrimo(num)
    except AssertionError:
        return "El número debe ser mayor a 1."
    except:
        return "El número debe ser entero."
def verPrimo(num):
    '''
    Entrada: num
    Funcionalidad: Llamar a validarPrimo
    Salida: True o False
    '''
    salida = validarPrimo(num)
    return salida
#--------------------------------------------------
def sumarDigMul(num,dig):
    '''
    Entrada: num(int),dig(int)
    Funcionalidad: Sumar los digitos de num que sean divisibles por dig
    Salida: Suma de todos los digitos de num divisibles por dig
    '''
    if num == 0:
        return 0
    if (num)%dig == 0:
        return num%10 + sumarDigMul(num//10,dig)
    else:
        return sumarDigMul(num//10,dig)
def validarSumDig(num,dig):
    '''
    Entrada: num, numero a validar, dig, digito a validar
    Funcionalidad: Validar num y dig para sumarDigMul
    Salida: Mensaje de error o sumarDigMul(num,dig)
    '''
    try:        
        if isinstance(num,float) or isinstance(dig,float):
            return "Debe indicar un número entero."
        assert 0 < num and 0 < dig < 10
        num = int(num)
        dig = int(dig)        
        return sumarDigMul(num,dig)
    except:
        return "Ingrese un número mayor que cero y un digito positivo."
def sumDigMul(num,dig):
    '''
    Entrada:  num,dig
    Funcionalidad: Llamar a validarSumDig
    Salida: Suma de todos los digitos de num divisibles por dig
    '''
    salida = validarSumDig(num,dig)
    return salida
#--------------------------------------------------
def elevar(num,dig):
    '''
    Entrada: num(int),dig(int)
    Funcionalidad: Elevar a la potencia dig el numero num
    Salida: num a la potencia dig
    '''
    if dig == 0:
        return 1
    return num * elevar(num,dig-1)
def validarElevar(num,dig):
    '''
    Entrada: num,numero a validar,dig,digito a validar
    Funcionalidad: Validar num y dig para elevar
    Salida: Mensaje de error o elevar(num,dig)
    '''
    try:        
        if isinstance(num,float) or isinstance(dig,float):
            return "Debe indicar un número entero."
        assert 0 <= num and 0 <= dig 
        num = int(num)
        dig = int(dig)        
        return elevar(num,dig)
    except:
        return "Ingrese un número entero positivo y un digito entero positivo."
def elevarNum(num,dig):
    '''
    Entrada: num,dig
    Funcionalidad: Llamar a validarElevar
    Salida: num a la potencia dig
    '''
    salida = validarElevar(num,dig)
    return salida


#-------------------------------------------------------------------------------------------Programa Principal

print('''
----------- RETO 1 -----------

>>> encontrarCero(125.2)
'''+str(encCero(125.2))+'''
>>> encontrarCero(-10)
'''+str(encCero(-10))+'''
>>> encontrarCero(0)
'''+str(encCero(0))+'''
>>> encontrarCero(125)
'''+str(encCero(125))+'''
>>> encontrarCero(81254010)
'''+str(encCero(81254010))+'''

----------- RETO 2 -----------

>>> encontrarPar("Hola")
'''+str(encontrarPar("Hola"))+'''
>>> encontrarPar(1357)
'''+str(encontrarPar(1357))+'''
>>> encontrarPar(1234)
'''+str(encontrarPar(1234))+'''

----------- RETO 3 -----------

>>> sumaDeDigitos(12345)
'''+str(hacerSum(12345))+'''

----------- RETO 4 -----------

>>> multiplicaNumImpares(123a)
'''+str(hacerMulImp("123a"))+'''
>>> multiplicaNumImpares(12345)
'''+str(hacerMulImp(12345))+'''
>>> multiplicaNumImpares(246)
'''+str(hacerMulImp(246))+'''

----------- RETO 5 -----------

>>> numeroMasGrande(123a)
'''+str(pedirNumGran("123a"))+'''
>>> numeroMasGrande(4571)
'''+str(pedirNumGran(4571))+'''
>>> numeroMasGrande(333)
'''+str(pedirNumGran(333))+'''

----------- RETO 6 -----------

>>> digitoABuscar(1234567123, 2)
'''+str(buscarDig(1234567123,2))+'''
>>> digitoABuscar(3451233453, 3)
'''+str(buscarDig(3451233453,3))+'''
>>> digitoABuscar(234565, 9)
'''+str(buscarDig(234565, 9))+'''

----------- RETO 7 -----------

>>> formarNumero("Hola¡")
'''+str(hacerPar("123a"))+'''
>>> formarNumero(255.3)
'''+str(hacerPar(255.3))+'''
>>> formarNumero(-2556)
'''+str(hacerPar(-2556))+'''
>>> formarNumero(2552180)
'''+str(hacerPar(2552180))+'''
>>> formarNumero(125)
'''+str(hacerPar(125))+'''
>>> formarNumero(135)
'''+str(hacerPar(135))+'''

----------- RETO 8 -----------

>>> esNumeroPrimo("sd")
'''+str(verPrimo("sd"))+'''
>>> esNumeroPrimo(-25)
'''+str(verPrimo(-25))+'''
>>> esNumeroPrimo(401)
'''+str(verPrimo(401))+'''
>>> esNumeroPrimo(7)
'''+str(verPrimo(7))+'''
>>> esNumeroPrimo(5)
'''+str(verPrimo(5))+'''
>>> esNumeroPrimo(9)
'''+str(verPrimo(9))+'''

----------- RETO 9 -----------

>>> sumarDigitosMultiplos(6,3)
'''+str(sumDigMul(6,3))+'''
>>> sumarDigitosMultiplos(1002,7)
'''+str(sumDigMul(1002,7))+'''
>>> sumarDigitosMultiplos(666,3)
'''+str(sumDigMul(666,3))+'''
>>> sumarDigitosMultiplos(1234,2)
'''+str(sumDigMul(1234,2))+'''

----------- RETO 10 -----------

>>> sumarDigitosMultiplos(5,0)
'''+str(elevarNum(5,0))+'''
>>> sumarDigitosMultiplos(2,4)
'''+str(elevarNum(2,4))+'''
>>> sumarDigitosMultiplos(0,0)
'''+str(elevarNum(0,0))+'''
>>> sumarDigitosMultiplos(5,3)
'''+str(elevarNum(5,3))+'''
''')






