# Dado un número natural x, determinar si es capicúa.

def Problema6():
    x = int(input("Ingresa un numero natural: "))
    original = x
    reverso = 0
    
    if x <= 0:
        print("Ingresa un numero natural profavor")
    else:
        while x > 0:
            digito = x % 10
            reverso = reverso * 10 + digito
            x //= 10
        
        if original == reverso:
            print("es capicua")
        else:
            print("no es capicua")

Problema6()