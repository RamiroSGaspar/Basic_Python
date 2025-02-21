# Solución al problema 2, multiplicar A con B
def Problema2():
    p1 = int(input("Ingresa un número: "))  # A
    p2 = int(input("Ingresa el siguiente número: "))  # B
    p3 = 0  # Acumulador del resultado
    p4 = 0  # Contador
    
    # La A se suma por sí misma la cantidad de veces que de vuelta el bucle
    while p4 < p2:  # La cantidad de veces que se va a iterar es la misma que el número multiplicador
        p3 += p1  # Y el resultado de cada suma se guarda en la 3era pizarra
        p4 += 1  
    
    print(f"El número {p1} x {p2} = {p3}") 

Problema2()
