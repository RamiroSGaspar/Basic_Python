# Dado un número natural x, mostrar su último dígito.
def Problema4():
    x = int(input("Ingresa un numero natural: "))
    
    if x == 0:
        print("Porfavor ingrese un numero natural")
    else:
        utlimo_digito = x % 10
        print(utlimo_digito)

Problema4()