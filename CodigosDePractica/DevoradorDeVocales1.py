'''
Programa para devorar las vocales que ingresa el usuario

Explicación: 

Se inicia la variable "palabra" que contiene una cadena ingresada por el usuario
mediante la función input() que dentro tiene un mensaje indicatorio, todos los 
caracteres ingresados se convierten en mayusculas, mediante la función de upper()

Despues se inicia un bucle for, donde la variable de control es "caracter" y la
cantidad de iteraciones son la cantidad de cadenas que hay en la variable de
"palabra", de forma que cada vez que se itere, "caracter" almacene un nuevo valor
osea un caracter de "palabra". Donde dentro del cuerpo del bucle hay varias condiciones
buscando los caracteres pertenecientes a las vocales. Donde si se detecta una, no la 
imprime y pasa a la siguiente iteracion para volver a verificar si no hay vocales, 
hasta que se complete el recorrido 

'''
palabra = input("Ingresa una palabra para quitarle las vocales: ").upper()

for caracter in palabra:
    if caracter == "A":
        continue
    elif caracter == "E":
        continue
    elif caracter == "I":
        continue
    elif caracter == "O":
        continue
    elif caracter == "U":
        continue
    else:
        print(caracter)