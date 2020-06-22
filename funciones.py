#Creado por Leonardo  Fariña y Mario Lara
#Fecha de creacion 12/06/20 10:46am
#Fecha de modificacion 14/06/20 1:07am
#Version python 3.8.3

#Importaciones

import pickle

#===========================================================================Definicion de funciones
def entradaLocal():
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    colu = input("Ingrese la columna: ")
    return int(colu)
def entradaPiso():
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    pisos = input("Ingrese el piso: ")
    return int(pisos)
def buscarPisoLocal():
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    pisos = input("Ingrese el piso: ")
    locales = input("Ingrese el local: ")
    return int(pisos),int(locales)
def entradaPisLoc():
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    pisos = input("Ingrese cantidad de pisos: ")
    locales = input("Ingrese cantidad de locales: ")
    return int(pisos),int(locales)
def validarArchivo():
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    cuentas = leeBin("Cuentas")
    if cuentas == "Error al leer el archivo: Cuentas":
        pisos,locales = entradaPisLoc()    
        grabaBin("Cuentas",crearEdi(pisos,locales))
    cuentas = leeBin("Cuentas")
    return cuentas
def crearEdi(pisos,locales):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    salida = []
    piso = []
    while pisos > 0:
        while locales > 0:
            piso.append(0)
            locales -= 1            
        salida.append(piso[:])
        pisos -= 1
    return salida
def alquilarLocal(piso,local,edi):
    '''
    solicite el piso y el número de local, si es válido, registre el monto de
    alquiler y avise al usuario el correcto alquiler vía la aplicación, en caso contrario indique
    el problema. (Archivo)

    '''
    piso = piso-1
    local = local-1
    monto = input("Ingrese el monto a cobrar: ")
    edi[piso][local] = monto
    grabaBin("Cuentas",edi)
    return ""
def modificarRenta(piso,local,edi):
    '''
    solicite el piso y el número de local, si el número de local existe en
    ese piso y el monto es diferente de 0, es porque está alquilado, por ende confirme el
    deseo de aumentar o disminuir la renta y si se aprueba, reemplace por el nuevo valor
    especificado por el usuario
    '''
    piso = piso-1
    local = local-1
    if edi[piso][local] != 0:
        elecc = int(input("1-)Aumentar la renta\n2.)Disminuir la renta\nIngrese su elección: "))
        if elecc == 1 or elecc == 2: 
            monto = input("Ingrese el monto a cobrar: ")
            edi[piso][local] = monto
        else:
            return "Por favor ingresar los datos solicitados."           
    else:
        return "No se puede modificar,ya que no esta alquilado."
    grabaBin("Cuentas",edi)
    return "Proceso finalizado satisfactoriamente"
def desalojar(piso,local,edi):
    '''
    solicite el piso y el número de local, si es correcto, existe un ingreso y el
    usuario confirma, permita registrar el monto de ingresos en cero. De lo contrario,
    especifique lo sucedido. (Archivo)

    '''
    piso = piso-1
    local = local-1
    print("El ingreso de este local es de ",edi[piso][local])
    elecc = int(input("¿Existe un ingreso en este local?\n1-)Si\n2.)No\nIngrese su elección: "))
    if elecc == 1:
        monto = input("Ingrese el monto a cobrar: ")
        edi[piso][local] = monto
    elif elecc == 2: 
        return "No se puede desalojar,ya que no esta alquilado."
    else:
        return "Por favor ingresar los datos solicitados."            
    grabaBin("Cuentas",edi)    
    return "Proceso finalizado satisfactoriamente"
def ingresoLocal(piso,local,edi):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    piso = piso-1
    local = local-1
    if edi[piso][local] != 0:
        return "El ingreso de este local es de $"+ str(edi[piso][local])
    return "El local no esta alquilado."
def ingresoPiso(piso,edi):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    local = 1
    total = 0
    for i in edi[piso-1]:
        print("Piso : ",piso)
        print("Local : ",local)
        print("Monto de alquiler ",edi[piso-1][local-1])
        total += int(edi[piso-1][local-1])
        local += 1        
    return "Para un total de ingresos del piso de $" + str(total)
def ingresoColumna(edi):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    piso = 1
    total = 0
    for i in edi:
        piso += 1
        local = 1
        if len(edi) >= piso:
            for e in i:
                print("Piso : ",piso)
                print("Local : ",local)
                print("Monto de alquiler ",edi[piso-1][local-1])
                total += int(edi[piso-1][local-1])
                local += 1        
    return "Para un total de ingresos del piso de $" + str(total)
def sumarColumna(matriz,local):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    piso=0
    suma=0
    indexL = local-1
    for piso in range(len(matriz)):
        print("Piso:",piso+1)
        print("Local",local)
        print("Monto de alquiler",matriz[piso][indexL])
        suma += int(matriz[piso][indexL])
    return "Para un total de ingresos por columna: $"+str(suma)
def ingresoTotal(edi):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''    
    piso = 1
    total = 0
    for i in edi:
        piso += 1
        local = 1
        if len(edi) >= piso:
            for e in i:
                print("Piso : ",piso)
                print("Local : ",local)
                print("Monto de alquiler ",edi[piso-1][local-1])
                total += int(edi[piso-1][local-1])
                local += 1        
    return "Para un total de ingresos del piso de $" + str(total)
def reporteTotal(edi):
    '''
    Funcionalidad:
    Entrada:
    Salida:
    '''
    des = 0
    ocu = 0
    for i in edi:
        for e in i:
            if e == 0:
                des += 1
            else:
                ocu += 1
    porc = des + ocu
    porcDes = round((des * 100)/porc,2)
    porcOcu = round((ocu * 100)/porc,2)
    return "Total de locales alquilados: "+str(ocu)+", para un porcentaje de: "+str(porcOcu)+"%\nTotal de locales desocupados: "+str(des)+", para un porcentaje de: "+str(porcDes)+"%"
def grabaBin(nomArchGrabar,contenido):
    """
    Funcionalidad: Grabar el contenido en un archivo binario
    Entradas:nomArchLeer(str), nombre del archivo a leer,contenido(bin),contendio a grabar
    Salidas: mensaje "Proceso finalizado satisfactoriamente" o mensaje de error
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(contenido,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
        return "Proceso finalizado satisfactoriamente"
    except:
        return "Error al grabar el archivo: "+ nomArchGrabar    
def leeBin(nomArchLeer):
    """
    Funcionalidad: Leer el contenido de un archivo en binario
    Entradas:nomArchLeer(str), nombre del archivo a leer
    Salidas: salida(bin),Contenido del archivo o mensaje de error
    """
    salida = ""
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        salida = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
        return salida
    except:
        return "Error al leer el archivo: "+ nomArchLeer
#===========================================Programa principal























