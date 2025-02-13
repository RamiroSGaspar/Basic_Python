bloques = int(input("Ingresa la cantidad de bloques "))

ac_bloques = 0
nivel = 0

while ac_bloques + nivel <= bloques:
    nivel += 1
    ac_bloques += nivel
    
altura = nivel
print(altura)