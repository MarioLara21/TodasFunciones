#Creado por: Mario Lara Molina
#Fecha de creacion: 29/04/2020 10:50
#Ultima modificacion: 29/04/2020 11:50
#Version 3.8.2

#Explicacion de las variables
"""
RNO= es una variable que indica la lluvia caida en la region norte en el mes i(1=<1>=12)
RCE= es una variable que indica la lluvia caida en la region central en el mes i(1=<1>=12)
RSU= es una variable que indica la lluvia caida en la region sur en el mes i(1=<1>=12)
i= variable tipo entero, representa la variable de control del ciclo
ARNO,ARCE,ARSU= Variables de tipo real. Acumulan las lluvias caidas en las regiones norte,centro y sur
MERSU= Variable de tipo real. Almacena el menor registro mensual de la region sur.Como se trata de localizar
un minimo, al principio se inicializa con un valor muy elevado.
MES= Variable de tipo entero. Almacena el mes con menores con menores lluvias en la region sur
RNO,RCE y RSU= Variables de tipo real.
PRORCE= Variable de tipo real. Almacena el promedio anual de las lluvias caidas en la region centro.
"""
def lluvias():
    #PP
        ARNO=0
        ARCE=0
        ARSU=0
        MERSU=500000
        i=1
        MES=1
       
        while i <= 12:
            try:
                RNO=int(input("Ingrese las lluvias en las zona norte:"))
                RCE=int(input("Ingrese las lluvias en las zona central:"))
                RSU=int(input("Ingrese las lluvias en las zona sur:"))
            except ValueError:
                print("Ingrese solo numeros enteros")
            ARNO+=RNO
            ARCE+=RCE
            ARSU+=RSU

            if RSU>MERSU:
                MERSU = RSU
                MES = i
            i+=1
            
        PRORCE =(ARCE/12)
        print("PROMEDIO REGION CENTRO:", PRORCE,"MES CON MENOR LLUVIA REG.SUR:",MES,"REGISTRO DEL MES:",MERSU)

        if ARNO>ARCE:
           if ARNO>ARSU:
               print("LA REGION CON MAYOR LLUVIA ES LA REGION NORTE")
           else:
               print("LA REGION CON MAYOR LLUVIA ES LA REGION SUR")

        else:
           if ARCE>ARSU:
               print("LA REGION CON MAYOR LLUVIA ES LA REGION CENTRO")
           else:
               print("LA REGION CON MAYOR LLUVIA ES LA REGION SUR")

               
lluvias()
            


    
    

