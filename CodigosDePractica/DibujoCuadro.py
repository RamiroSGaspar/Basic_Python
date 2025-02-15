import turtle

# Configurar la pantalla
t = turtle.Turtle()
t.speed(1)  # Velocidad media

# Función para dibujar un "cuadro" según el algoritmo dado
def dibujar_cuadro():
    for _ in range(4):  # Cuatro lados
        t.forward(100)  # Dibujar línea hacia "arriba"
        for _ in range(3):  # Girar 30 grados tres veces (total 90 grados)
            t.right(30)

# Llamar la función para dibujar
dibujar_cuadro()

# Evitar que la ventana se cierre inmediatamente
turtle.done()
