try:
    n1=float(input("Numerador: "))
    n2=float(input("Denominador: "))
    resultado=n1/n2
    print ("Resultado ", resultado)
except ValueError:
    print ("Debe dar solo números")
except ZeroDivisionError:
    print ("Intenta dividir por cero")
except:
    print("Se dieron otras excepciones")

