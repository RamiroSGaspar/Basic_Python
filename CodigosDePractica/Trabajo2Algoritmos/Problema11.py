# Dado un número entero x, calcular xy y mostrar el resultado.

# yo entendi que xy se refiere a que "x" es la base e "y" es el exponente
def Problema8():
    x = int(input("Ingresa un numero entero: "))
    y = int(input("Ingresa el exponente: "))
    
    resultado = x**y
    print(resultado)
    
Problema8()