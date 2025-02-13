bloques = int(input("Ingresa la cantidad de bloques: "))

ac = 0
nivel = 1

while ac + nivel <= bloques:
    ac += nivel
    nivel += 1
    
altura = nivel - 1
print(altura)