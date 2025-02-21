# Dada una lista de N números naturales x, mostrar el mayor de ellos.

def Prooblema11():
    N = int(input("Ingresa la cantidad de que de numeros a ingresar: "))
    lista = []
    
    if (N < 0):
        print("Ingresa un numero correcto para la lista de los numeros")
    else:
        # Bucle donde se guradan los numeros ingresado en la lista con los espacios
        # indicados por el usuario
        for i in range(1, N + 1): 
            x = int(input("Ingresa un numero natural: "))
            if x <= 0:
                print("Ingresa un numero natural profavor")
            else:
                lista.append(x)
        
        print(lista)
    
    # Verificacion si la lista no esta vacia
    if lista: 
        numMayor = lista[0]  
        
        # se encuentra el numero mayor en la lista
        for numero in lista:
            if numero > numMayor:
                numMayor = numero
        
        print("el numero mas grande de la lista es: ", numMayor)

Prooblema11()
                    
    