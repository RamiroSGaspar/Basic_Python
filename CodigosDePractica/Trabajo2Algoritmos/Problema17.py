# Dadas dos listas de números A y B, indicar si el mayor de la lista A se encuentra en la lista B.

def Problema13():
    N1 = int(input("Ingresa la cantidad de elementos para la lista A: "))
    N2 = int(input("Ingresa la cantidad de elementos para la lista B: "))
    A = []
    B = []
    
    if N1 <= 0 or N2 <= 0:
        print("Ingrese un número correcto para los espacios en las listas.")
    
    print("Llenando lista A:")
    for i in range(N1):
        x = int(input("Ingresa un número para A: "))
        A.append(x)
        
    print("Llenando lista B:")
    for i in range(N2):
        y = int(input("Ingresa un número para B: "))
        B.append(y)
        
    mayor_A = max(A)
    if mayor_A in B:
        print(f"El mayor de la lista A, que es {mayor_A}, se encuentra en la lista B.")
    else:
        print(f"El mayor de la lista A, que es {mayor_A}, NO se encuentra en la lista B.")

Problema13()
