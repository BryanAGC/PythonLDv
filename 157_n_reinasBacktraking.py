"""
Resuelve el problema de las N-Reinas con backtracking.
"""
def es_seguro(tablero, fila, col, N):
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, N, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    return True

def resolver_n_reinas(tablero, col, N):
    if col >= N:
        return True
    for i in range(N):
        if es_seguro(tablero, i, col, N):
            tablero[i][col] = 1
            if resolver_n_reinas(tablero, col + 1, N):
                return True
            tablero[i][col] = 0
    return False

def imprimir_solucion(N):
    tablero = [[0] * N for _ in range(N)]
    if not resolver_n_reinas(tablero, 0, N):
        print("No hay solución")
        return
    for fila in tablero:
        print(fila)

imprimir_solucion(8)
