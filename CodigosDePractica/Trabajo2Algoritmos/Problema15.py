# Dada una lista de N números enteros x, calcular su promedio. Mostrar el resultado.

def Problema11():
    N = int(input("Ingresa un la cantidad de espacios para la lista: "))
    lista = []
    total = 0
    
    if N <= 0:
        print("Ingresa un numero correcto")
    else:
        for i in range(1, N + 1):
            x = int(input("Ingresa un numero entero: "))
            lista.append(x)
            total += x
        
        lista.sort()
        print(lista)
        
        promedio = total / N
        print("El promedio de los numeros de la lista es: ", promedio)
    
Problema11()