# Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.

def Problema4():
    x = int(input("Ingresa un numero natural: "))
    pares = 0
    impares = 0
    
    if x <= 0:
        print("Ingrese un numero natural porfavor")
    else:
        while x > 0:
            u_digito = x % 10
            if u_digito % 2 == 0:
                pares += 1
            else:
                impares += 1
            x //= 10
            
    print("Cantidad de numeros pares: ", pares)
    print("Cantidad de numeros impares: ", impares)

Problema4()
    