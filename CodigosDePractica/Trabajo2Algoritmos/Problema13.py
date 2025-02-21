# Dados dos números naturales A y B, mostrar sus divisores comunes.
def Problema10():
    A = int(input("Ingresa un numero natural: "))
    B = int(input("Ingresa otro numero natural: "))
    a = A
    b = B
    DivisoresComunes = []
    
    if A <= 0 or B <= 0:
        print("Ingresa un numero natural profavor en ambos casos")
    else:
        # Se busca el MCD de los numeros ingresados
        while B != 0:
            res = A % B
            A = B
            B = res
        c = A # var con el MCD de a y b

        # Bucle que obtiene los divisores comunes entre ambos numeros
        for i in range(1, c + 1):
            if (c % i == 0):
                DivisoresComunes.append(i)
            else:
                continue
            
        DivisoresComunes.sort()
        
        print(f"los divisores comunes entre {a} y {b} son: {DivisoresComunes}")

Problema10()            
            
            