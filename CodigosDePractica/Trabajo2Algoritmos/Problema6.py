# Dado un número natural x, contar la cantidad de dígitos que posee.

# Aclaración, en el mismo programa doy la opcion de eleccion al usuario de que metodo elegir
# para obtener los resultados, la primera opcion es mediante elementos que ofrece Python
# como lenguaje de progración. Pero la segunda opcion se realizo mediante un algoritmo, que
# tiene compatiblidad con otros lenguajes de programación.

def Problema3_Opcion1():
    x = int(input("Ingresa un numero natural: "))
    
    if x <= 0:
        print("Ingresa una numero natural")
    else:
        cantidad_de_digitos = len(str(abs(x))) # Se usa funciones de Python
        print("Cantidad de digitos: ", cantidad_de_digitos)
        

def Problema3_Opcion2():
    x = int(input("Ingresa un numero natural: "))
    
    contador = 0
    if x <= 0:
        print("Ingresa un numero natural profavor")
    else:
        while x > 0:
            x //= 10
            contador += 1
        print("Cantidad de digitos", contador)

a = int(input("Elige las dos opciones, introduzca el numero de la opción: "))
if a == 1:
    Problema3_Opcion1()
elif a == 2:
    Problema3_Opcion2()