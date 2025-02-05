"""
Genera un laberinto aleatorio y resuélvelo usando backtracking.
"""
import random

def generar_laberinto(n, m):
    laberinto = [['#'] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if random.random() > 0.3:
                laberinto[i][j] = '.'
    laberinto[0][0] = 'S'
    laberinto[n-1][m-1] = 'E'
    return laberinto

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(' '.join(fila))

lab = generar_laberinto(10, 10)
imprimir_laberinto(lab)
