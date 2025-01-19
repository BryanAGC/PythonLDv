"""
Dado un laberinto representado como una matriz de 0s y 1s, 
encuentra la ruta más corta desde la esquina superior izquierda hasta la inferior derecha.
"""
from collections import deque

def camino_mas_corto(laberinto):
    filas, columnas = len(laberinto), len(laberinto[0])
    if laberinto[0][0] == 1 or laberinto[filas - 1][columnas - 1] == 1:
        return -1

    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cola = deque([(0, 0, 1)])
    visitado = set()

    while cola:
        x, y, pasos = cola.popleft()
        if (x, y) == (filas - 1, columnas - 1):
            return pasos
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0 and (nx, ny) not in visitado:
                cola.append((nx, ny, pasos + 1))
                visitado.add((nx, ny))
    return -1

# Ejemplo de uso
laberinto = [[0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 0],
             [0, 0, 0, 0, 0]]

print(camino_mas_corto(laberinto))  # 7
