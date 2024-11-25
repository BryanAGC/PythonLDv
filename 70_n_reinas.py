"""
Escribe una función que resuelva el problema de las n-reinas: coloca n reinas en un tablero de ajedrez n x n 
de tal forma que ninguna se ataque entre sí. Devuelve todas las posibles soluciones.
"""
def resolver_n_reinas(n):
    def es_seguro(tablero, fila, col):
        for i in range(col):
            if tablero[fila][i] == 1:
                return False
        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
        for i, j in zip(range(fila, n), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
        return True

    def resolver(col):
        if col >= n:
            soluciones.append([fila.index(1) for fila in tablero])
            return
        for i in range(n):
            if es_seguro(tablero, i, col):
                tablero[i][col] = 1
                resolver(col + 1)
                tablero[i][col] = 0

    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    resolver(0)
    return soluciones


print(resolver_n_reinas(4))
