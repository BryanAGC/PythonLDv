"""
Coloca N reinas en un tablero de ajedrez de NxN sin que se ataquen entre sí.
"""
def es_seguro(tablero, fila, col, n):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def resolver_n_reinas(n, fila=0, tablero=[]):
    if fila == n:
        print(tablero)
        return
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            resolver_n_reinas(n, fila + 1, tablero + [col])

# Ejemplo de uso con 4 reinas
resolver_n_reinas(4)
