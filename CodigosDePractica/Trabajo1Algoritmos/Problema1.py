
# Solucion para el problema de la suma de n numeros
def Problema1():
    p1 = 0  # Pizarra para ver el total de la suma de n numeros
    p2 = 0  # Pizarra para el numero actual
    p3 = 0  # Se utiliza para ver el resultado
    p4 = 0  # Se usa para saber la cantidad de veces que se hizo una suma
    
    condicion = ""
    
    while condicion != "N":
        p2 = int(input("Ingresa un numero: "))
        p1 += p2
        p3 = p1
        p4 +=1
        condicion = input("Quieres seguir (Y/N):").upper()
        
        if p4 > 1:
            print("Resultado de la suma: ", p3)
            print("Cantidad de veces que se realizo una suma: ",p4)
    print("Total:", p1)
    
Problema1()