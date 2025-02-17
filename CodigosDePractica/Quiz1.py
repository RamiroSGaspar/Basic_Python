seleccion = int(input("Ingresa el numero de la pregunta para resolverlo: "))

# Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. 

def pregunta1():
    print("Resolucion de la pregunta 1")
    for numero in range(11):
        if numero % 2 != 0:
            print("numero impar: ", numero)

# Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. 

def pregunta2():
    print("Resolucion de la pregunta 2")
    n = 1
    while n < 11:
        if n % 2 != 0:
            print("numero impar: ", n)
        n += 1
        
# Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre
# los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @
# e imprimir la parte antes de @ en una línea.

def pregunta3():
    correo = input("Ingresa el correo electronico: ")
    nombre = ""
    for caracter in correo:
        if caracter == "@":
            break
        nombre += caracter
    print(nombre)

if seleccion == 1:
    pregunta1()
elif seleccion == 2:
    pregunta2()
elif seleccion == 3:
    pregunta3()