# Dado un número natural x, mostrar todos sus dígitos del menos 
# significativo al más significativo.

def Problema2():
    x = int(input("Ingresa un numero natural: "))
    
    if x == 0:
        print("Porfavor Ingresa un numero natural")
    else:
        while x > 0:
            digito_menos_significativo = x % 10
            print(digito_menos_significativo)
            x = x // 10

Problema2()