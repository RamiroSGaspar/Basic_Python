# Dada una lista ordenada de N números x, indicar si hay elementos repetidos.

def Problema12():
    N = int(input("Ingresa la cantidad de espacios para la lista: "))
    lista = []
    numVisto = 0
    listaRepetidos = []
    
    if N <= 0:
        print("Ingresa un numero correcto para los espacios en la lista")
    else:
        for i in range(1, N + 1):
            x = int(input("Ingresa un numero: "))
            lista.append(x)
            lista.sort() # Se ordena la lista para que la comparacion sea con el anterior elemento,
                         # durante el bucle.
        
        # Bucle se inicia desce 1 hasta la cantidad de elementos en la lista
        # Asi que la var de control "numero" no va a tener un valor de la lista
        # sino que va a ser del 1 hasta N
        for i in range(1, len(lista)): 
            if lista[i] == lista[i - 1]: # Se compara un valor con el anterior de la lista, debido a que
                                         # se ordeno anteriormente
                if lista[i] not in listaRepetidos: # Para evitar duplicados en la lista de repetidos
                    listaRepetidos.append(lista[i])
    
        print(lista)
        print(listaRepetidos)

Problema12()