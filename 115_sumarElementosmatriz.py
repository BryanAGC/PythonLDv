"""
Suma todos los elementos de una matriz dada.
"""
def suma_matriz(matriz):
    return sum(sum(fila) for fila in matriz)

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(suma_matriz(matriz))  # 45
