"""
Verifica si una matriz cuadrada es simétrica (igual a su transpuesta).
"""
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(es_simetrica(matriz))  # True
