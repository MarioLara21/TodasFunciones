#Elaborado por: AAAA
#Fecha de creación: 23/10/2019, 8:00am
#Última modificación: 26/10/2019, 11:00 pm
#Versión: 3.5.2

#importación de librerias
import sys 
import pickle
import re

#Definición de funciones

def leerArchivo():
    """
    Funcionalidad: Responsable de ver si existe un archivo ysi existe, de leerlo.
    Entradas:
    -NA
    Salidas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    """
    try:
        dicc={}
        paro=open("listParo.dat","rb")
        dicc=pickle.load(paro)
        paro.close()
        return dicc
    except:
        dicc={}
        return dicc
    
def grabarArchivo(x):
    """
    Funcionalidad: Responsable de grabar datos en un diccionario.
    Entradas:
    -x(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -dicc(dicc), diccionario con los datos de las personas registradas en el paro.
    """
    paro=open("listParo.dat","wb")
    dicc=x
    pickle.dump(dicc,paro)
    paro.close()
    return dicc

def registrarPersona(dicc):
    """
    Funcionalidad: Responsable de registrar a una persona en la lista del paro.
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario el estado de su pedido.
    -dicc(dicc), diccionario con los datos de las personas registradas en el paro.
    """
    print("~~~~~~~~")
    print ("1.TEC")
    print ("2.UCR")
    print ("3.UNA")
    print ("4.UNED")
    print ("5.UTN")
    u=(input("Digite su universidad de procedencia: "))
    
    if u=="1":
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo=(input ("Digite el tipo de persona: "))
        if tipo=="1":
            iden=input("Digite su carnet(10 dígitos): ")
            if identETecAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="2":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="3":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        else:
            print("¡Opción inválida!")
            dicc=leerArchivo()
            registrarPersona(dicc)
            
  
    elif u=="2":
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo=(input ("Digite el tipo de persona: "))
        if tipo=="1":
            iden=input("Digite su carnet: ")
            if identEUCRAux(iden)==True:
                nombre=input("Digite su nombre completo([A|B]6 dígitos): ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="2":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="3":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        else:
            print("¡Opción inválida!")
            dicc=leerArchivo()
            registrarPersona(dicc)
            
    elif u=="3":
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo=(input ("Digite el tipo de persona: "))
        if tipo=="1":
            iden=input("Digite su carnet(6 dígitos): ")
            if identEUNAAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="2":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        elif tipo=="3":
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        else:
            print("¡Opción inválida!")
            registrarPersona(dicc)
            
    elif u=="4":
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo=(input ("Digite el tipo de persona: "))
        opcionesCorrectas=["1","2","3"]
        if tipo in opcionesCorrectas:
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        else:
            print("¡Opción inválida!")
            dicc=leerArchivo()
            registrarPersona(dicc)
            
    elif u=="5":
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo=(input ("Digite el tipo de persona: "))
        opcionesCorrectas=["1","2","3"]
        if tipo in opcionesCorrectas:
            iden=input("Digite su número de identificación(9 dígitos): ")
            if cedulaAux(iden)==True:
                nombre=input("Digite su nombre completo: ")
                datos=[nombre,u,tipo]
                dicc[iden]=datos
                print ("------------")
                print ("¡Registrado!")
                print ("------------")
                grabarArchivo(dicc)
                return dicc
            else:
                dicc=leerArchivo()
                registrarPersona(dicc)
        else:
            print("¡Opción inválida!")
            dicc=leerArchivo()
            registrarPersona(dicc)
            
    else:
        print("¡Opción inválida!")
        dicc=leerArchivo()
        print(dicc)
        registrarPersona(dicc)

def actualizarDatos(dicc):
    """
    Funcionalidad: Responsable de actualizar los datos una persona en la lista del paro.
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario el estado de su pedido.
    -dicc(dicc), diccionario con los datos de las personas registradas en el paro.
    """
    carne=input("Digite la identificación de la persona a analizar: ")
    if carne in dicc:
        print("~~~~~~~~")
        print ("1.TEC")
        print ("2.UCR")
        print ("3.UNA")
        print ("4.UNED")
        print ("5.UTN")
        u=(input("Digite la universidad: "))
        print ("--------------------")
        print ("1. Estudiante")
        print ("2. Administrativo")
        print ("3. Docente")
        tipo= (input ("Digite el tipo de persona: "))
        nombre=input("Digite su nombre completo: ")
        datos=[nombre,u,tipo]
        dicc[carne]=datos
        grabarArchivo(dicc)
        print ("-------------")
        print ("¡Actualizado!")
        print ("-------------")
        return dicc
    else :
        print ("No hay registro de esta identificación.")
        return ""

    
#Funciones de reportes

def reporteE(u, dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes según una universidad.  
    Entradas:
    -u(string), número de universidad.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes según una universidad.
    """
    llaves= list (dicc.keys())
    i=0
    while i<len(llaves):
        iden=llaves[i]
        if dicc[iden][1]==u:
            if dicc[iden][2]=="1":
                print (iden, "-", dicc[iden][0])
                i=i+1
            else:
                i=i+1
        else:
            i=i+1
    return""

def reporteA(u, dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes según una universidad.  
    Entradas:
    -u(string), número de universidad.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes según una universidad.
    """
    llaves= list (dicc.keys())
    i=0
    while i<len(llaves):
        iden=llaves[i]
        if dicc[iden][1]==u:
            if dicc[iden][2]=="2":
                print (iden, "-", dicc[iden][0])
                i=i+1
            else:
                i=i+1
        else:
            i=i+1
    return""

def reporteD(u, dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes según una universidad.  
    Entradas:
    -u(string), número de universidad.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes según una universidad.
    """
    llaves= list (dicc.keys())
    i=0
    while i<len(llaves):
        iden=llaves[i]
        if dicc[iden][1]==u:
            if dicc[iden][2]=="3":
                print (iden, "-", dicc[iden][0])
                i=i+1
            else:
                i=i+1
        else:
            i=i+1
    return""


              
def reporteETEC(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes del Tec.  
    Entradas:
    -"1"(string), número de universidad del Tec.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes del Tec.
    """
    print ("*****")
    print ("ESTUDIANTES")
    reporteE("1", dicc)
    return""

def reporteATEC(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes del Tec.  
    Entradas:
    -"1"(string), número de universidad del Tec.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes del Tec.
    """
    print ("*****")
    print ("ADMINISTRATIVOS")
    reporteA("1", dicc)
    return""

def reporteDTEC(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes del Tec.  
    Entradas:
    -"1"(string), número de universidad del Tec.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes del Tec.
    """
    print ("*****")
    print ("DOCENTES")
    reporteD("1", dicc)
    return""

def reporteEUNA(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes de la UNA.  
    Entradas:
    -"3"(string), número de universidad de la UNA.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes de la UNA.
    """
    print ("*****")
    print ("ESTUDIANTES")
    reporteE("3", dicc)
    return""

def reporteAUNA(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes de la UNA.  
    Entradas:
    -"3"(string), número de universidad de la UNA.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes de la UNA.
    """
    print ("*****")
    print ("ADMINISTRATIVOS")
    reporteA("3", dicc)
    return""
            
def reporteDUNA(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes de la UNA.  
    Entradas:
    -"3"(string), número de universidad de la UNA.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes de la UNA.
    """
    print ("*****")
    print ("DOCENTES")
    reporteD("3", dicc)
    return""

def reporteEUCR(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes de la UCR.  
    Entradas:
    -"2"(string), número de universidad de la UCR.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes de la UCR.
    """
    print ("*****")
    print ("ESTUDIANTES")
    reporteE("2", dicc)
    return""

def reporteAUCR(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes de la UCR.  
    Entradas:
    -"2"(string), número de universidad de la UCR.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes de la UCR.
    """
    print ("*****")
    print ("ADMINISTRATIVOS")
    reporteA("2", dicc)
    return""

def reporteDUCR(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes de la UCR.  
    Entradas:
    -"2"(string), número de universidad de la UCR.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes de la UCR.
    """
    print ("*****")
    print ("DOCENTES")
    reporteD("2", dicc)
    return""

def reporteEUNED(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes de la UNED.  
    Entradas:
    -"4"(string), número de universidad de la UNED.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes de la UNED.
    """
    print ("*****")
    print ("ESTUDIANTES")
    reporteE("4", dicc)
    return""

def reporteAUNED(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes de la UNED.  
    Entradas:
    -"4"(string), número de universidad de la UNED.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes de la UNED.
    """
    print ("*****")
    print ("ADMINISTRATIVOS")
    reporteA("4", dicc)
    return""  

def reporteDUNED(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes de la UNED.  
    Entradas:
    -"4"(string), número de universidad de la UNED.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes de la UNED.
    """
    print ("*****")
    print ("DOCENTES")
    reporteD("4", dicc)
    return""

def reporteEUTN(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes de la UTN.  
    Entradas:
    -"5"(string), número de universidad de la UTN.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes de la UTN.
    """
    print ("*****")
    print ("ESTUDIANTES")
    reporteE("5", dicc)
    return""

def reporteAUTN(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de administrativos manifestantes de la UTN.  
    Entradas:
    -"5"(string), número de universidad de la UTN.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los administrativos manifestantes de la UTN.
    """
    print ("*****")
    print ("ADMINISTRATIVOS")
    reporteA("5", dicc)
    return""

def reporteDUTN(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de docentes manifestantes de la UTN.  
    Entradas:
    -"5"(string), número de universidad de la UTN.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los docentes manifestantes de la UTN.
    """
    print ("*****")
    print ("DOCENTES")
    reporteD("5", dicc)
    return""

def reporteTEC(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes del Tec.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes del Tec.
    """
    print ("-------------TEC---------------")
    reporteETEC(dicc)
    reporteATEC(dicc)
    reporteDTEC(dicc)
    print ("_______________________________")
    return ""

def reporteUNA(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes del UNA.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes del UNA.
    """
    print ("-------------UNA---------------")
    reporteEUNA(dicc)
    reporteAUNA(dicc)
    reporteDUNA(dicc)
    print ("________________________________")
    return ""

def reporteUCR(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes del UCR.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes del UCR.
    """
    print ("-------------UCR---------------")
    reporteEUCR(dicc)
    reporteAUCR(dicc)
    reporteDUCR(dicc)
    print ("_______________________________")
    return ""

def reporteUNED(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes del UNED.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes del UNED.
    """
    print ("-------------UNED---------------")
    reporteEUNED(dicc)
    reporteAUNED(dicc)
    reporteDUNED(dicc)
    print ("_______________________________")
    return ""

def reporteUTN(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes del UTN.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes del UTN.
    """
    print ("-------------UTN---------------")
    reporteEUTN(dicc)
    reporteAUTN(dicc)
    reporteDUTN(dicc)
    print ("_______________________________")
    return ""

def reporte(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes, administrativos y docentes manifestantes de todas las universidades.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los manifestantes de todas las universidades.
    """
    print ("_______________________________")
    reporteTEC(dicc)
    reporteUCR(dicc)
    reporteUNA(dicc)
    reporteUNED(dicc)
    reporteUTN (dicc)
    return""

def estudiantesPorUniversidad(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte de estudiantes manifestantes de todas las universidades.  
    Entradas:
    -"1"(string), número de universidad del Tec.
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario los datos de los estudiantes manifestantes de todas las universidades.
    """
    print ("_______________________________")
    print ("-------------TEC---------------")
    reporteETEC(dicc)
    print ("-------------UCR---------------")
    reporteEUCR(dicc)
    print ("-------------UNA---------------")
    reporteEUNA(dicc)
    print ("-------------UNED---------------")
    reporteEUNED(dicc)
    print ("-------------UTN---------------")
    reporteEUTN(dicc)
    print ("_______________________________")
    return""


    
def manifestantes(dicc):
    """
    Funcionalidad: Responsable de indicar el reporte la cantidad de estudiantes, administrativos y docentes manifestantes de todas las universidades.  
    Entradas:
    -dicc(diccionario), diccionario con los datos de las personas registradas en el paro.
    Salidas:
    -String que le indica al usuario la cantidad de manifestantes de todas las universidades.
    """
    tec=0
    una=0
    ucr=0
    uned=0
    utn=0
    llaves=list(dicc.keys())
    i=0
    while i<len(llaves):
        iden=llaves[i]
        if dicc[iden][1]=="1":
            tec=tec+1
            i=i+1
        elif dicc[iden][1]=="2":
            ucr=ucr+1
            i=i+1
        elif dicc[iden][1]=="3":
            una=una+1
            i=i+1
        elif dicc[iden][1]=="4":
            uned=uned+1
            i=i+1
        elif dicc[iden][1]=="5":
            utn=utn+1
            i=i+1
    total=tec+ucr+una+uned+utn
    print("___________________________________")
    print("~ Del TEC hay "+str(tec)+" manifestantes ~")
    print ("~ De la UCR hay "+str(ucr)+" manifestantes ~")
    print ("~ De la UNA hay "+str(una)+" manifestantes ~")
    print ("~ De la UNED hay "+str(uned)+" manifestantes ~")
    print ("~ De la UTN hay "+str(utn)+" manifestantes ~")
    print("~ En total hay "+str(total)+" manifestantes ~")
    print("___________________________________")
    return""
              
    
# Validaciones

def identETecAux(num):
    """
    Funcionalidad: Responsable de validar el número de identificación de los estudiantes del Tec.  
    Entradas:
    -num(string), número de identificación del estudiante.
    Salidas:
    -String que le indica al usuario si el carnet el válido o no.
    -True(bool)
    -False(bool)
    """
    if re.match("^(20)(01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19)\d{6}$", num):
        return True
    else:
        print("Número de carné inválido.")
        return False

def identEUCRAux(num):
    """
    Funcionalidad: Responsable de validar el número de identificación de los estudiantes de la UCR.  
    Entradas:
    -num(string), número de identificación del estudiante.
    Salidas:
    -String que le indica al usuario si el carnet el válido o no.
    -True(bool)
    -False(bool)
    """
    if re.match("^[A|B]\d{5}$", num):
        return True
    else:
        print("Número de carné inválido.")
        return False

def identEUNAAux(num):
    """
    Funcionalidad: Responsable de validar el número de identificación de los estudiantes de la UNA.  
    Entradas:
    -num(string), número de identificación del estudiante.
    Salidas:
    -String que le indica al usuario si el carnet el válido o no.
    -True(bool)
    -False(bool)
    """
    if re.match("^(01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19)\d{4}$", num):
        return True
    else:
        print("Número de carné inválido.")
        return False

def cedulaAux(num):
    """
    Funcionalidad: Responsable de validar el número de identificación de una persona.  
    Entradas:
    -num(string), número de identificación de una persona.
    Salidas:
    -String que le indica al usuario si el carnet el válido o no.
    -True(bool)
    -False(bool)
    """
    if re.match("^\d{9}$", num):
        return True
    else:
        print("Número de cédula inválido.")
        return False
