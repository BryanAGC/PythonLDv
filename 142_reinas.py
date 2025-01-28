"""
Resuelve el problema de N-Reinas colocando N reinas en un tablero NxN sin que se ataquen entre sí.
"""
def es_seguro(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def resolver_n_reinas(n, fila=0, tablero=[]):
    if fila == n:
        print(tablero)
        return
    for col in range(n):
        if es_seguro(tablero, fila, col):
            resolver_n_reinas(n, fila + 1, tablero + [col])

# Ejecutar con N = 4
resolver_n_reinas(4)
