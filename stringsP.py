def elimina_vocales(s):
    vocales="aeiouAEIOUáéíúóÁÉÍÓÚ"
    s_sin_vocales=""
    for letra in s:
        if letra not in vocales:
            s_sin_vocales+=letra
    return s_sin_vocales

a=input("Digite una palabra")
print(elimina_vocales(a))

mensaje="hola mundo"
print (mensaje.capitalize())
