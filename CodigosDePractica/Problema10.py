# Dado un número entero x, mostrar sus N primeras potencias.

def Problema7():
    x = int(input("Ingresa un numero entero: "))
    N = int(input("Ingresa la cantidad de potencias que deseas calcular: "))
    
    for i in range(N):
        resultado = x ** i
        print(f"resultado de {x} con exponente {i} es: ", resultado)

Problema7()