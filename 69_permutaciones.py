"""
Escribe una función que calcule todas las permutaciones posibles de una lista de elementos.
"""
def permutaciones(lista):
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([lista[i]] + p)
    return resultado

# Ejemplo de uso
print(permutaciones([1, 2, 3]))  
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
