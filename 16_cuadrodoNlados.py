"""
HAZ UNA FUNCION QUE DIBUJE
UN CUADRADO DE N LADOS
"""

def dibujar_cuadrado(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

dibujar_cuadrado(4)