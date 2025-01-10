"""
Genera una matriz identidad de tamaño n.
"""
def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Ejemplo de uso
for fila in matriz_identidad(4):
    print(fila)
