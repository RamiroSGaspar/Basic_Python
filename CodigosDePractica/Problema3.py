# Soluciṕn al problema 3, dividir A con B, division entera.
def problema3():
    p1 = int(input("Ingresa un número: "))  # A
    p2 = int(input("Ingresa el siguiente número: "))    # B
    p3 = p1 
    p4 = 0  # Contador del resultado
    
    
    while p3 >= p2:
        p3 = p3 - p2
        p4 += 1
        
    print(f"La division de {p1} // {p2} = {p4}")

problema3()