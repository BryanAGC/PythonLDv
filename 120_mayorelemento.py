"""
Encuentra el elemento mayoritario en una lista (el que aparece más de n/2 veces).
"""
def elemento_mayoritario(lista):
    candidato, conteo = None, 0
    for num in lista:
        if conteo == 0:
            candidato, conteo = num, 1
        elif num == candidato:
            conteo += 1
        else:
            conteo -= 1
    return candidato if lista.count(candidato) > len(lista) // 2 else None

# Ejemplo de uso
print(elemento_mayoritario([3, 3, 4, 2, 3, 3, 3]))  # 3
print(elemento_mayoritario([1, 2, 3, 4]))  # None
