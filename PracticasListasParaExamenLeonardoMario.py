#Credo por Mario Lara Molina y Leonardo Fariña
#Fecha de creacion:27/05/2020 12:16
#Ultima modificacion:31/05/2020 20:28
#Versión 3.8.3

#Importacion de librerias

#------------------------------------------------------Definicion de funciones

#Reto1
def listar_indices(elemento,lista):
    """
    Funcionalidad:Buscar un elemento en una lista y en una lista retornar los índices en los que se encuentran
    Entradas:elemento(int)=elemento a buscar en la lista, lista(list)=Lista en la que se busca el elemento
    Salidas:indices(list)=Valores de los índices de la lista donde se encuentra el elemento
    """
    indices=[]
    indice=0
    for i  in lista:
        if i==elemento:
            indices.append(indice)
        indice+=1
    return indices
def validar_listar_indices(elemento=None,lista=None):
    """
    Funcionalidad: Validar los datos para la función listar_indices(elemento,lista)
    Entradas:elemento(int)=elemento a buscar en la lista, lista(list)=Lista en la que se busca el elemento
    Salidas: Datos validados para la función listar_indices(elemento,lista)
    """
    if elemento==None:
        return "Debe ingresar un elemento"
    elif lista==None:
        return "Debe ingresar una lista"
    else:
        return listar_indices(elemento,lista)
def mostrar_validar_listar_indices():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función listar_indices(elemento,lista)
    Salidas: Datos en pantalla de la función listar_indices(elemento,lista)
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 1 lista_indices  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1 \nEntradas: elemento=100, lista:[200, 250, 100, 125, 100]\n","Salida:\n",validar_listar_indices(100, [200, 250, 100, 125, 100]),"\n")
    print("Caso2 \nEntradas: elemento='uno', lista: [“dos”, “uno”, “dos”, “tres”, “uno”, “uno”]\n","Salida:\n",  validar_listar_indices("uno", ["dos", "uno", "dos", "tres", "uno", "uno"]),"\n")
    print("Caso3 \nEntradas: elemento= 2, lista:[10, 100, 50]\n","Salida:\n", validar_listar_indices(2, [10, 100, 50]),"\n")
#Reto2
def positivos_negativos(lista):
    """
    Funcionalidad: Separar los números de una lista en positivos y negativos
    Entradas: lista(list)=Lista con únicamente números enteros tanto positivos como negativos
    Salidas: Una lista con dos sublistas, una con los números negativos y otra con los positivos
    """
    positivos=[]
    negativos=[]
    for i in lista:
        if i>=0:
            positivos.append(i)
        else:
            negativos.append(i)
    salida=[positivos,negativos]
    return salida
def validar_positivos_negativos(lista=None):
    """
    Funcionalidad: Validar los datos para la función validar_positivos_negativos(lista)
    Entradas: lista(list)=Lista con números enteros
    Salidas: Datos validados para la función validar_positivos_negativos(lista)
    """
    if lista==None:
        return("Debe ingresar una lista")
    for i in lista:
        if not isinstance(i,int):
            return "La lista debe tener únicamente números enteros"
    return positivos_negativos(lista)
def mostrar_validar_positivos_negativos():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función validar_positivos_negativos
    Salidas: Datos en pantalla de la función validar_positivos_negativos
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 2 positivos_negativos  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1 \nEntradas: lista=[4, -1, 2, 8, -4, -2]\nSalida:\n",validar_positivos_negativos([4, -1, 2, 8, -4, -2]),"\n")
    print("Caso2 \nEntradas: lista=[-1, -4, -2]\nSalida:\n",validar_positivos_negativos([-1, -4, -2]),"\n")
#Reto3
def elimina_espacios(cadena):
    """
    Funcionalidad: Elimina los espacios de una cadena de caracteres
    Entradas: Cadena(str)=Una cadena de carácteres con espacios
    Salidas: Una lista con dos valores, la cadena sin espacios y la cantidad de espacios
    """
    unida_str=[cadena.replace(" ","")]
    espacios= cadena.count(" ")
    return [unida_str,[espacios]]
def validar_elimina_espacios(cadena):
    """
    Funcionalidad: Validar los datos para la función 
    Entradas: cadena(str)=Secuencia de carácteres que ingresan a la función elimina_espacios(cadena) 
    Salidas: Datos validados para la función elimina_espacios(cadena)
    """
    if not isinstance(cadena,str):
        return "Debe ingresar una cadena de tipo string(Entre comillas)"
    else:
        return elimina_espacios(cadena)
def mostrar_validar_elimina_espacios():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función validar_elimina_espacios(cadena)
    Salidas: Datos en pantalla de la función validar_elimina_espacios(cadena)
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 3 elimina_espacios(cadena)  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1\nEntradas:“Hoy es un buen día para ser feliz.”\nSalida:\n",validar_elimina_espacios("Hoy es un buen día para ser feliz."),"\n")
#Reto4
def agrupar(lisEnteros):
    """
    Funcionalidad: Retornar una lista donde cada índice contiene el entero respectivo con los mismos dígitos agrupados según aparezcan de izquierda a derecha
    Entradas: lisEnteros(list),lista de enteros 
    Salidas: salidaV(list), lista donde cada índice contiene el entero respectivo con los mismos dígitos agrupados según aparezcan de izquierda a derecha
    """
    salida = []
    salidaF = ""
    salidaV = []
    index = len(list(lisEnteros))
    cont = 0

    while cont < index :
        listaEval = list(str(lisEnteros[cont]))
        
        for i in listaEval:
            contador = listaEval.count(i)
            while i not in salida:
                while  contador > 0:
                    salida.append(i)
                    salidaF += str(i)
                    contador -= 1
        salidaV.append(int(salidaF))
        salida = []
        salidaF = ""
        cont += 1

    return salidaV
def validar_agrupar(lista=None):
    """
    Funcionalidad: Validar los datos para la función validar_agrupar(lista)
    Entradas: lista(list)=Lista con números enteros
    Salidas: Datos validados para la función validar_agrupar(lista)
    """
    if lista==None:
        return "Debe ingresar una lista"
    for i in lista:
        if not isinstance(i,int):
            return "La lista debe tener únicamente números enteros" 
    return agrupar(lista)
def mostrar_validar_agrupar():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función validar_agrupar
    Salidas: Datos en pantalla de la función validar_agrupar
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 4 agrupar  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1 \nEntradas: lista= [20845224809, 213323]\nSalida:\n",validar_agrupar([20845224809, 213323]),"\n")
    print("Caso2 \nEntradas: lista=[]\nSalida:\n",validar_agrupar([]),"\n")
#Reto5
def provincia(numP,cedula):
    """
    Funcionalidad: Retorna otra lista con las cédulas que pertenecen a la provincia indicada en el dígito de entrada numP
    Entradas: numP(int),recibe un dígito entre 1 y 7 (indica una provincia de Costa Rica),cedula(list) una lista de números de cédula
    Salidas:  salida(list),lista con las cédulas que pertenecen a la provincia indicada
    """
    salida = []
    cont = len(cedula)-1
    while cont >= 0:
        listEval = list(str(cedula[cont]))
        if numP == int(listEval[0]):
            salida.append(cedula[cont])
        cont -= 1
    return salida
def validar_provincia(numP,lista=None):
    """
    Funcionalidad: Validar los datos para la función validar_provincia(lista)
    Entradas: lista(list)=Lista con números enteros
    Salidas: Datos validados para la función validar_provincia(lista)
    """
    if lista==None:
        return "Debe ingresar una lista"
    for i in lista:
        if not isinstance(i,int):
            return "La lista debe tener únicamente números enteros"
    if  numP < 0 or 7 < numP:
        return "ERROR: PROVINCIA DEBE ESTAR ENTRE 1 Y 7"
    return provincia(numP,lista)
def mostrar_validar_provincia():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función validar_provincia
    Salidas: Datos en pantalla de la función validar_provincia
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 5 provincia  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1 \nEntradas: provincia = 2 lista=[123456789, 201340789, 222222222 ,433333333, 511111111,207890456]\nSalida:\n",validar_provincia(2,[123456789, 201340789, 222222222 ,433333333, 511111111,207890456]),"\n")
    print("Caso2 \nEntradas: provincia = 1 lista=[123456789,213456789,222222222,233333333,511111111,207890456]\nSalida:\n",validar_provincia(1,[123456789,213456789,222222222,233333333,511111111,207890456]),"\n")
    print("Caso3 \nEntradas: provincia = 3 lista=[123456789,213456789,222222222,423333333,511111111,207890456]\nSalida:\n",validar_provincia(3,[123456789,213456789,222222222,423333333,511111111,207890456]),"\n")
    print("Caso4 \nEntradas: provincia = 9 lista=[123456789,213456789,222222222,233333333,511111111,207890456]\nSalida:\n",validar_provincia(9,[123456789,213456789,222222222,233333333,511111111,207890456]),"\n")
#Reto6
def lista_numeros(cadenaDeTxt):
    """
    Funcionalidad: Retorna una lista que contenga los números presentes en el string recibido (int and float)
    Entradas: cadenaDeTxt(str), letras con números
    Salidas: salidaFF(list), numeros presentes en el string recibido
    """
    if cadenaDeTxt.isalpha() == True:
        return []
    cont = len(cadenaDeTxt)
    index = 0
    salida = ""
    salidaV = []
    salidaF = []
    while  index < cont:                
        caracterEval = cadenaDeTxt[index]
        if caracterEval.isdigit() == True:
            salida += caracterEval
        
        if  caracterEval == "." and caracterEval != cadenaDeTxt[-1]:
            if (cadenaDeTxt[index-1]).isdigit() == True:
                if(cadenaDeTxt[index+1]).isdigit() == True:
                    salida += caracterEval + cadenaDeTxt[index+1]
                    index += 1
                    
        if cadenaDeTxt[index-1].isdigit() == True and caracterEval.isalpha() == True and caracterEval != "." and caracterEval != cadenaDeTxt[-1]:
            salida += ","

        
        index += 1
    salidaV.append(salida)   
    salida = salida.split(",")
    

    salida = ((((str(salida).replace("'","")).replace("[","")).replace("]","")).strip(",")).split(",")
    salida = [float(x) for x in salida]

    salidaFF = []
    cont = len(salida)
    index = 0
    
    while index < cont:
        if salida[index] > int(salida[index]):
            salidaFF.append(float(salida[index]))
        else:
            salidaFF.append(int(salida[index]))
            
        index += 1


        
    return salidaFF

def validar_lista_numeros(cadena):
    """
    Funcionalidad: Validar los datos para la función lista_numeros 
    Entradas: cadena(str)=Secuencia de carácteres que ingresan a la función lista_numeros
    Salidas: Datos validados para la función lista_numeros
    """
    if not isinstance(cadena,str):
        return "Debe ingresar una cadena de tipo string(Entre comillas)"
    else:
        return lista_numeros(cadena)
    
def mostrar_lista_numeros():
    """
    Funcionalidad: Mostrar los datos en pantalla de la función validar_lista_numeros
    Salidas: Datos en pantalla de la función validar_lista_numeros
    """
    print("▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤  Función 6 lista_numeros  ▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤▤")
    print("Caso1\nEntrada:\"xy225p30ab0g8.9iou1000\"\nSalida:\n",validar_lista_numeros("xy225p30ab0g8.9iou1000"),"\n")
    print("Caso2\nEntrada:\"ab95.8124c76n\"\nSalida:\n",validar_lista_numeros("ab95.8124c76n"),"\n")
    print("Caso3\nEntrada:\"x0.25za10.5\"\nSalida:\n",validar_lista_numeros("x0.25za10.5"),"\n")
    print("Caso4\nEntrada:\"xyz\"\nSalida:\n",validar_lista_numeros("xyz"),"\n")
#----------------------------------------------------Programa principal

#Llamada a las funciones de mostrar
    
mostrar_validar_listar_indices()    
mostrar_validar_positivos_negativos()
mostrar_validar_elimina_espacios()
mostrar_validar_agrupar()
mostrar_validar_provincia()
mostrar_lista_numeros()














    
