import re
#Cantidad de materias
def conseguirCantidad():
    reintCantidad = True
    while reintCantidad:
        try:
            cantidad= int(input("Ingrese la cantidad de materias que cursó: "))
            assert 0 < cantidad <= 10
            reintCantidad = False
        except AssertionError:
            print("El minimo de materias posibles es 1 y el máximo 10")
        except:
            print("Ingrese un número valido de materias cursadas")
    return cantidad

#Nombres de las materias
def conseguirNombres(cantidad):
    materias = []
    for i in range(0,cantidad):
        invalido = True
        while invalido:
            print("Materia número ", i+1)
            cursoN = input("Ingrese el nombre del curso: ").lower()
            agregar = validarIntroTaller(cursoN)
            if not agregar in materias:
                materias.append(agregar)
                invalido = False
            else:
                print("Esa materia ya fue registrada")
    return materias
    
def validarIntroTaller(cursoN):
        if re.match(r"(intro|introducción|introduccion|intro a progra|introduccion a progra|introducion a la programacion|introducción a la progra|introducion a la programacion|introducción a la progra|)$",cursoN):
            return "INTRODUCCIÓN A LA PROGRAMACIÓN"
        elif re.match(r"(taller|taller de progra|taller progra|taller de programacion|taller de programación)$",cursoN):
            return "TALLER DE PROGRAMACIÓN"
        else:
            return cursoN.upper()
        
#Notas obtenidas       
def conseguirNotas(materias,cantidad):
    suma = 0
    notas = []
    for j in range(0,cantidad):
        print("Nota en", materias[j])
        reintNota = True
        while reintNota:
            try:
                nNota= int(input("Ingrese la nota obtenida: "))
                assert 0 <= nNota <= 100
                notas.append(nNota)
                suma +=  nNota
                reintNota = False
            except AssertionError:
                print("Ingrese un número entre 0 y 100")
            except:
                print("Ingrese un número valido de nota obtenida")
    promedio = suma//cantidad
    return notas, promedio
def obtenerCandidato():
    while True:
        candidato = input("Ingrese su nombre: ")
        if re.match((r"\w\D"),candidato):
            return candidato
        print("Nombre invalido")
def definirAplica():
    nombre = obtenerCandidato()
    cant = conseguirCantidad()
    cursos = conseguirNombres(cant)
    calificaciones,ponderado = conseguirNotas(cursos,cant)
    (cursos,cant)
    if "INTRODUCCIÓN A LA PROGRAMACIÓN" in cursos:
        if "TALLER DE PROGRAMACIÓN" in cursos:
            if calificaciones[cursos.index("INTRODUCCIÓN A LA PROGRAMACIÓN")> 80]:
                if calificaciones[cursos.index("TALLER DE PROGRAMACIÓN")> 80]:
                    if ponderado > 70:
                        
                        print("""
            El candidato """+ nombre +"""
            tiene un promedio de: """, ponderado,"""
            Una nota en introducción a la programación de: """,calificaciones[cursos.index("INTRODUCCIÓN A LA PROGRAMACIÓN")],"""
            Una nota en taller de programación de: """,calificaciones[cursos.index("TALLER DE PROGRAMACIÓN")],"""
            Por ende puede ser asistente de la profesora.
                             """)
                        
                    else:
                        print(nombre+" no puede ser asistente porque su ponderado es menor que 70")
                else:
                    print(nombre+" no puede ser asistente porque su nota en Introducción a la programación es menor que 80")
            else:
                print(nombre+" no puede ser asistente porque su nota en Introducción a la programación es menor que 80")
        else:
            print(nombre+" no puede ser asistente porque no llevó Taller de programación")
    else:
        print(nombre+" no puede ser asistente porque no llevó Introducción a la programación")
    
definirAplica()
