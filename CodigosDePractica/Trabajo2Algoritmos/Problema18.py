# Dado un número natural, mostrar el mayor de sus dígitos.
def Problema14():
    x = int(input("Ingresa un numero natural: "))
    mayor = 0
    
    if x<= 0:
        print("Ingresa un numero natural")
    else:
        while x > 0:
            u_diigito = x % 10
            if u_diigito > mayor:
                mayor = u_diigito
            x //= 10
    
    print("el digito mayor es: ", mayor)

Problema14()