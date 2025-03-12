#Crea una función que reciba un número entero y cuente cuántos bits están en 1 en su representación binaria.

def ParImparBits():
    n = int(input("Ingresa un numero entero: "))
    
    if n & 1:
        print("Es impar")
    else:
        print("Es par")
        
ParImparBits()