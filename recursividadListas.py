#Creado por Mario Lara y Leonardo Fariña
#Fecha de creación 29/07/2020 11:00 am 
#Última modificación 30/07/2020 23:12 
#Versión 3.8.3
#Definicion de funciones
#-------------------------------------------------- reto 1
def insert_dAux(ele,sigEle,lista,res=[]):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    Restriciones:
    """
    if lista==[]:
        return res
    else:
        if lista[0]==ele:

            res+=[ele]+[sigEle]
            return insert_dAux(ele,sigEle,lista[1:],res)
        else:
            res.append(lista[0])
            return insert_dAux(ele,sigEle,lista[1:],res)
        
def insert_d(ele,sigEle,lista):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    Restriciones:
    """
    try:
        if not isinstance(lista,list):
            return "Debe ingresar una lista como tercer elemento"
        else:
            return insert_dAux(ele,sigEle,lista,res=[])
    except:
        return ""
#-------------------------------------------------- reto 2
def alternada(lista,resultado="Hola",index=0,largo=0):
    '''
    Entrada: lista(list) lista que tiene numeros
    Funcionalidad: Averiguar si los numeros estan intercalados par, impar o viceversa.
    Salida: True o False
    '''
    if lista == []:
        return True
    if lista[index]%2 == 0:
        if resultado == True:            
            return False
        resultado = True
        return alternada(lista[1:],resultado,largo)
    else:
        if resultado == False:
            return False
        resultado = False
        return alternada(lista[1:],resultado,largo)

def validarAlterna(lista):
    '''
    Entrada: lista(list) a validar
    Funcionalidad: Validar num para alternada
    Salida: Mensaje de error o alternada(lista)
    '''
    try:        
        if lista == []:
            return "Debe indicar un lista no nula."
        return alternada(lista)
    except:
        return "Debe indicar un lista no nula."


#-------------------------------------------------- reto 3
def separarAux(lista,imp=[],par=[],cont=0):
    """
    Funcionalidad: Separa los elementos en índices pares e impares
    Entradas:
    lista= lista con los datos
    imp= lista de índices impares
    par= lista índices pares
    cont= contador numérico
    Salidas:
    Restricciones: la lista no debe ser vacía
    """
    if lista==[]:
        return [imp,par]
    else:
        if (cont%2)==0:
            par.append(lista[0])
            cont+=1
            return separarAux(lista[1:],imp,par,cont)
        else:
            imp.append(lista[0])
            cont+=1
            return separarAux(lista[1:],imp,par,cont)
def separar(lista):
    """
    Funcionalidad: Valida los datos y llama a la función
    Entradas: lista= lista de elementos
    Salidas: Datos validados y llamado a la función
    Restricciones: la lista no debe ser vacia
    """
    try:
        if not isinstance(lista,list):
            return "Debe ingresar una lista"
        elif lista==[]:
            return "La lista no debe estar vacía"
        else:
            return separarAux(lista,imp=[],par=[],cont=0)
    except:
        return "Los datos deben ser de tipo entero positivo"
#-------------------------------------------------- reto 4
def replicar(lista,replica,salida,index=0):
    '''
    Entrada: lista(list),replica(int)
    Funcionalidad: Replicar cada elemento de la lista las veces replica
    Salida: Lista con los elementos replicados
    '''
    if index == 0:
        index = replica
    if lista == []:
        return salida
    if replica > 0:
        salida.append(lista[0])
        return replicar(lista,replica-1,salida,index)
    else:
        return replicar(lista[1:],index,salida,index)


def validarReplicar(lista,replica):
    '''
    Entrada: lista(list) y replica(int) a validar
    Funcionalidad: Validar lista y replica para replicar
    Salida: Mensaje de error o replicar(lista,replica,[])
    '''
    try:        
        if lista == []:
            return "Debe indicar un lista no nula."
        return replicar(lista,replica,[])
    except:
        return "Debe indicar un lista no nula."

#-------------------------------------------------- reto 5
def listaAscendente(lista,res=True,ant=0):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    Restricciones:
    """
    if lista==[]:
        return res
    else:
        if lista[0]<ant:
            res=False
            return res
        else:
            ant=lista[0]
            return listaAscendente(lista[1:],res,ant)
        
def listaAscendenteAux(lista):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    Restricciones:
    """
    try:
        if not isinstance(lista,list):
            return "Debe ingresar una lista"
        elif lista==[]:
            return "La lista no debe estar vacía"
        else:
            return listaAscendente(lista,res=True,ant=0)
    except:
        return "Debe ingresar una lista con datos de tipo entero"
#-------------------------------------------------- reto 6
def split(ele,lista,salida=[],lis=[]):
    '''
    Entrada: ele,lista(list)
    Funcionalidad: Dividir en listas cada vez que en la lista se encuentra ele elemento ele
    Salida: Lista con las listas
    '''
    if lista == []:
        if lis != []:
            salida.append(lis)
        return salida
    if lista[0] == ele:        
        salida.append(lis)
        return split(ele,lista[1:],salida,[])
    lis.append(lista[0])
    return split(ele,lista[1:],salida,lis)

#-------------------------------------------------------------------------------------------Programa Principal

print('''
----------- RETO 1 -----------

>>> insert_d("x","y",["a","b","c","x","d","e"])
'''+str(insert_d("x","y",["a","b","c","x","d","e"]))+'''

>>> insert_d(4,5,[1,2,3,4,6,7,4,8])
'''+str(insert_d(4,5,[1,2,3,4,6,7,4,8]))+'''


----------- RETO 2 -----------

>>> alternada([2,5,8,7,10])
'''+str(validarAlterna([2,5,8,7,10]))+'''

>>> alternada([1,2,3,4,6])
'''+str(validarAlterna([1,2,3,4,6]))+'''

>>> alternada([1,2,3,4,5])
'''+str(validarAlterna([1,2,3,4,5]))+'''

>>> alternada([])
'''+str(validarAlterna([]))+'''

----------- RETO 3 -----------

>>> separar(["a","b","c","d","e"])
'''+str(separar(["a","b","c","d","e"]))+'''

----------- RETO 4 -----------

>>> replicar([1,3,3,7],2)
'''+str(validarReplicar([1,3,3,7],2))+'''

>>> replicar(["h",9],4)
'''+str(validarReplicar(["h",9],4))+'''

>>> replicar(["hola",123],3)
'''+str(validarReplicar(["hola",123],3))+'''

----------- RETO 5 -----------

>>> listaAscendenteAux([2,4,5,6,7])
'''+str(listaAscendenteAux([2,4,5,6,7]))+'''

>>> listaAscendenteAux([8,7,2,4,5])
'''+str(listaAscendenteAux([8,7,2,4,5]))+'''

----------- RETO 6 -----------

>>> split('x',[])
'''+str(split('x',[],[],[]))+'''

>>> split('x',[1,4,7,'x',1,2,3])
'''+str(split('x',[1,4,7,'x',1,2,3],[],[]))+'''

>>> split('x',[1,4,7,'x','x',1,2,3])
'''+str(split('x',[1,4,7,'x','x',1,2,3],[],[]))+'''

>>> split('x',[1,4,7,'x','x','x',1,2,3])
'''+str(split('x',[1,4,7,'x','x','x',1,2,3],[],[]))+'''

>>> split('x',[1,4,7,'x','x','x',1,2,3,'x'])
'''+str(split('x',[1,4,7,'x','x','x',1,2,3,'x'],[],[]))+'''
''')






