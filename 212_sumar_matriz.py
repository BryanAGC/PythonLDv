"""
Escribe una función que reciba una matriz (lista de listas) y devuelva la suma de todos sus elementos.
"""
def sumar_matriz(matriz):
    return sum(sum(fila) for fila in matriz)

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = sumar_matriz(matriz)
print(f"La suma de todos los elementos de la matriz es: {resultado}")
