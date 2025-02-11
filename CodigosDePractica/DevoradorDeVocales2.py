palabra = input("Ingresa una variable para quitarle las vocales: ").upper()
LetrasAcumuladas = ""

for caracter in palabra:
    if caracter not in "AEIOU":
        LetrasAcumuladas += caracter

print(LetrasAcumuladas)