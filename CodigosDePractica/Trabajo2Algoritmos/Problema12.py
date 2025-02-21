# Dado un número natural x, mostrar todos sus divisores

def Problema9():
    x = int(input("Ingresa un número natural: "))
    divisores = []
    
    # se usa un bucle for, con la variable de control i, y el rango empieza desde 1
    # hasta la raiz cuardada de x, esta decicion se hizo para que el bucle no sea haga
    # tan largo ocupando recursos y respetando una caracteristica de los algoritmos,
    # que sean optimo y factible. De todas formas se obtienen todos los divisores.
    for i in range(1, int(x ** 0.5) + 1): 
        if x % i == 0:  # Se obtiene el primer divisor en una iteración
            divisores.append(i)
            if i != x // i: # Se encuentra el divisor par del anterior
                divisores.append(x // i)

    divisores.sort()

    print("Los divisores de", x, "son:", divisores)
    
Problema9()