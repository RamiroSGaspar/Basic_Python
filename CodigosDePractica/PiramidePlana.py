'''
Escenario:

Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques 
de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. 
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque 
más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la 
cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo 
inmediatamente.

Explicación:

Se crea una variable "bloques" donde el usuario ingresa la cantidad de bloques en entero,
lo ingresado mediante input() es convertido en entero mediante int(). Otras dos variables
se inician pero con el valor inicial de 0, "ac_bloques" y "mivel".

Se usa un bucle while donde la condicion es si la suma de los bloques acumulados + el nivel
de la piramide que se tiene es menor o igual a la varibale "bloques", de forma que si durante
un momento del bucle la suma entre ambos supera la cantidad de bloques se termina de ejecutar.
Si, si es posible la condicion entonces se va a seguir sumando el nivel a los bloques acumulados
pero si ya no es posible por que se supera la cantidad se detiene por que ya no es posible
completar otro nivel de altura con la cantidad de bloques completos necesarios para ese nivel.

Y el cuerpo del bucle contiene la variable nivel que se suma una vez mas en cada iteracion, para
lograr una piramide, y despues ese nivel que se tiene se suma a los bloques acumulados de forma
que se va viendo la cantida de bloques que se usaron.
'''


bloques = int(input("Ingresa la cantidad de bloques "))

ac_bloques = 0
nivel = 0

while ac_bloques + nivel <= bloques:
    nivel += 1
    ac_bloques += nivel
    
print("el nivel de altura es: ", nivel)