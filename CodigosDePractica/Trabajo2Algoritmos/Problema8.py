# Dado un número natural x, sumar todos sus dígitos. Mostar la suma obtenida.

def Problema5():
    x = int(input("Ingresa un numero natural: "))
    ac = 0
    
    if x <= 0:
        print("Ingresa un numero natural porfavor")
    else:
        while x > 0:
            digito = x % 10
            ac += digito
            x //= 10
        print("resultado de la suma de todos los digitos: ",ac)

Problema5()
            