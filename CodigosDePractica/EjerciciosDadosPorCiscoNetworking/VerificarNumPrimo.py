# Programa para saber si el numero ingresado es primo o no

n = int(input("Ingresa un numero: ")) # Var que almacena el num ingresado por el usuario

# Condicion, con la cual se descartan los num que son menores a 2, debido a que no son primos
if n < 2:
    print(f"{n} no es un numero primo. ")
    
# Si no se cumple esa condicion entonces se procede a buscar un divisor para ese numero
else:
    for i in range(2, int(n ** 0.5)+1): # Truco matematico, donde si un numero tiene un divisor es menor o igual a su raiz cuadrada
        if n % i == 0:
            print(f"{n} no es un numero primo. ")
            break # Se sale del bucle
    else: # Si el bucle esta vacio o termino todas sus iteraciones, entonces se pasa a este bucle
        print(f"{n} es un numero primo. ")
        