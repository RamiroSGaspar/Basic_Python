palabra = input("Ingresa una palabra para quitarle las vocales: ")
palabra = palabra.upper()

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