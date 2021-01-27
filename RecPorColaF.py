#Creado por Leonardo Fariña y Mario Lara
#Fecha de creación 29/07/2020 8:15 am
#Última modificación 30/07/2020 2:46 am
#Versión 3.8.3
#Declaración de funciones
#-----------------------------------------
#Reto 1
def cantDigAux(num,dig,res=0):
    """
    Funcionalidad: Busca la cantidad de veces que se repite dig en num
    Entradas:
    num= número entero donde se va a buscar el dígito
    dig= dígito a buscar en el num
    Salidas: Cantidad de veces que se repite dig en num
    Restricciones: todos los datos deben ser enteros positivos
    """
    if num==0:
        return res
    elif (num%10)==dig:
        return cantDigAux(num//10,dig,res+1)
    else:
        return cantDigAux(num//10,dig,res)
    
def cantDig(num,dig):
    """
    Funcionalidad: Valida los datos y llama a la función
    Entradas:
    num= número entero donde se va a buscar el dígito
    dig= dígito a buscar en el num
    Salidas: Datos validados y llamada a la función
    Restricciones: ambos datos deben ser números enteros  positivos
    """
    try:
        if not isinstance(num,int):
            return "La cifra numérica debe ser de tipo entero"
        elif not isinstance(dig,int):
            return "El dígito debe ser de tipo entero"
        elif num<0:
            return "El número debe ser únicamente positivo"
        elif dig<0 or dig>9:
            return "El dígito debe ser mayor a cero y menor o igual a nueve"
        else:
            return cantDigAux(num,dig)
    except:
        return "Los datos deben ser números enteros positivos"

#-----------------------------------------
#Reto 2
def sumarNumImp(num,num2):
    '''
    Entrada: num(int),num2(int)
    Funcionalidad: Sumar numeros impares en un intervalo
    Salida: Suma de impares en el intervalo [num,num2]
    '''
    if num > num2:
        return 0
    elif num%2 != 0:
        return num + sumarNumImp(num+1,num2)
    else:
        return sumarNumImp(num+1,num2)
    
def sumarNumImpAux(num,num2):
    '''
    Entrada: num y num2 numeros a validar
    Funcionalidad: Validar num y num2 para sumarNumImp
    Salida: Mensaje de error o sumarNumImp(num,num2)
    '''
    try:        
        if not isinstance(num,int) or not isinstance(num2,int):
            return "A y B deben ser números enteros."
        if num > num2:
            return "B debe ser mayor o igual a A"
        num = int(num)
        num2 = int(num2)
        return sumarNumImp(num,num2)
    except:
        return "A y B deben ser números enteros."
    
#-----------------------------------------
#Reto 3
def esBinarioAux(num,res=False):
    """
    Funcionalidad: Verifica si la cifra es binaria 
    Entradas: num= Número binario
    Salidas: True o False
    Restricciones: el número debe de ser binario
    """
    if (num//10)==0:
        if (num%10)==0 or (num%10)==1:
            res=True
            return res
        else:
             res=False
             return res
    elif (num%10)==0 or (num%10)==1:
        return esBinarioAux(num//10,True)
    else:
        res=False
        return res
    
def esBinario(num):
    """
    Funcionalidad: Valida los datos y llama a la función
    Entradas: num= Número binario
    Salidas: Datos validados y llamada a la función
    Restricciones: el número debe de ser binario
    """
    try:
        if not isinstance(num,int):
            return "El número debe ser de tipo entero"
        elif num<0:
            return "El número debe ser positivo"
        else:
            return esBinarioAux(num)
    except:
        return "El número debe ser de tipo entero positivo"

#-----------------------------------------
#Reto 4
def sumarNumAnnoB(num,num2):
    '''
    Entrada: num(int),num2(int)
    Funcionalidad: Sumar la cantidad de años bisiestos en un intervalo
    Salida: La cantidad de años bisiestos en el intervalo [num,num2]
    '''
    if num > num2:
        return 0
    elif num%4 == 0 and not num%100==0 or num%400==0:        
        return 1 + sumarNumAnnoB(num+1,num2)
    else:
        return sumarNumAnnoB(num+1,num2)
    
def sumarNumAnnoBAux(num,num2):
    '''
    Entrada: num y num2 numeros a validar
    Funcionalidad: Validar num y num2 para sumarNumAnnoB
    Salida: Mensaje de error o sumarNumAnnoB(num,num2)
    '''
    try:        
        if not isinstance(num,int) or not isinstance(num2,int):
            return "Los años deben ser números enteros mayores a 0."
        if num > num2:
            return "El año de finalizacion debe ser mayor o igual al año de inicio."
        num = int(num)
        num2 = int(num2)
        assert num > 0 and num2 > 0
        return sumarNumAnnoB(num,num2)
    except:
        return "Los años tienen que ser números enteros mayores a 0."

#-----------------------------------------
#Reto 5
def colonizarAux(gen,genPrim=0,parejas=9):
    """
    Funcionalidad: Indica la cantidad de personas en la generación
    Entradas:
    gen= generación a la que se debe llegar
    genPrim= Primera gen
    parejas= Parejas que se forman en la primer gen
    Salidas: Cantidad de personas en la gen
    Restricciones: Los datos deben ser enteros positivos
    """
    if genPrim==0:
        parejas=parejas*3
        if genPrim==gen:
            return parejas
        else:
            return colonizarAux(gen,genPrim+1,parejas)
    else:
        parejas=((parejas-1)//2)*3
        if genPrim==gen:
            return parejas
        else:
            return colonizarAux(gen,genPrim+1,parejas)
        
def colonizar(gen):
    """
    Funcionalidad: Valida los datos y llama a la función
    Entradas: gen= Generación que se desea buscar
    Salidas: Datos validados y llamado a la función
    Restricciones: gen debe ser de tipo entero y positivo
    """
    try:
        if not isinstance(gen,int):
            return "El número de la generación debe ser de tipo entero"
        elif gen<0:
            return "El número de la generación debe ser positivo"
        else:
            return colonizarAux(gen)
    except:
        return "El número debe ser un dato de tipo entero positivo"

#-----------------------------------------
#Datos en pantalla
print('''
----------- RETO 1 -----------

>>> cantDig(Hola,5)
''',cantDig("Hola",5),'''

>>> cantDig(95,Hola)
''',cantDig(95,"Hola"),'''

>>> cantDig(123456123456,25)
''',cantDig(123456123456,25),'''

>>> cantDig(123456123456,9)
''',cantDig(123456123456,9),'''

>>> cantDig(112233112233,1)
''',cantDig(112233112233,1),'''

----------- RETO 2 -----------

>>> sumarNumerosImparesEnIntervalo("Hola",25.3)
''',sumarNumImpAux("Hola",25.3),'''

>>> sumarNumerosImparesEnIntervalo(5,0)
''',sumarNumImpAux(5,0),'''

>>> sumarNumerosImparesEnIntervalo(-5,5)
''',sumarNumImpAux(-5,5),'''

>>> sumarNumerosImparesEnIntervalo(0,7)
''',sumarNumImpAux(0,7),'''

>>> sumarNumerosImparesEnIntervalo(2,125)
''',sumarNumImpAux(2,125),'''

----------- RETO 3 -----------

>>> esBinario(Hola)
''',esBinario("Hola"),'''

>>> esBinario(1001019)
''',esBinario(1001019),'''

>>> esBinario(5679)
''',esBinario(5679),'''

>>> esBinario(0)
''',esBinario(0),'''

>>> esBinario(10101)
''',esBinario(10101),'''

----------- RETO 4 -----------

>>> contarCantidadDeAnnosBisiestos("Hola",1)
''',sumarNumAnnoBAux("Hola",1),'''

>>> contarCantidadDeAnnosBisiestos(50,10)
''',sumarNumAnnoBAux(50,10),'''

>>> contarCantidadDeAnnosBisiestos(1500,1836)
''',sumarNumAnnoBAux(1500,1836),'''

>>> contarCantidadDeAnnosBisiestos(2000,2025)
''',sumarNumAnnoBAux(2000,2025),'''
----------- RETO 5 -----------

>>> colonizar(0)
''',"colonizar(0)= ",colonizar(0),'''

>>> colonizar(1)
''',"colonizar(1)= ",colonizar(1),'''

>>> colonizar(2)
''',"colonizar(2)= ",colonizar(2),'''

>>> colonizar(3)
''',"colonizar(3)= ",colonizar(3),'''

>>> colonizar(4)
''',"colonizar(4)= ",colonizar(4),'''
''')


    
