"""
Escribe una función que reciba una lista de números y devuelva la diferencia entre el número mayor y el menor.
"""
def rango(lista_numeros):
    return max(lista_numeros) - min(lista_numeros) if lista_numeros else 0


print(rango([10, 20, 30, 5]))  # 25
