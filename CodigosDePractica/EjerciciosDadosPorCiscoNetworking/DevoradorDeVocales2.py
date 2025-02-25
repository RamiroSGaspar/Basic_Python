'''
Devorador de vocales ver2

Explicación:

La varibale "palabra" tiene la misma funcion que en la anterior ver, pero
se agrega una nueva variable con una cadena vacia, "LetrasAcumuladas".

Se inicia un bucle for, que la funcionalidad es la misma que en la anterior version
pero en el cuerpo se utiliza una sola condicion, si la variable de control no contiene
las vocales entonces se acumulan en la variable que se creo para ir mostrando despues
en pantalla, por que ahora la palabra sin las vocales se van a mostrar en una sola linea
en la salida
'''
palabra = input("Ingresa una variable para quitarle las vocales: ").upper()
LetrasAcumuladas = ""

for caracter in palabra:
    if caracter not in "AEIOU":
        LetrasAcumuladas += caracter

print(LetrasAcumuladas)