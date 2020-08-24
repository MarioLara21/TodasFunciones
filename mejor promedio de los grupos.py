#Elaborado por Mario Lara Molina
#Fecha de creación: 09/03/2020 18:48
#Última modificación 10/03/2020 14:24
# Versión: 3.8.1
# Algoritmo para ver el mejor promedio de un grupo

numeroG = 1
mejorG = 1
mejorP = 0
cantidadDeG = int(input("Digite la cantidad de grupos"))
while numeroG <= cantidadDeG :
    i=1
    suma=0
    cantidadE = int(input("Digite la cantidad total de estudiantes"))
    while i <= cantidadE :
        nota = int(input("Ingrese la nota"))
        suma += nota
        i += 1
    promedio= suma/cantidadE
    print("El promedio del grupo es:",promedio)
    if promedio > mejorP :
         mejorP = promedio
         mejorG= numeroG
    numeroG +=1
print("El mejor promedio es:", mejorP , "del grupo" , mejorG)        
