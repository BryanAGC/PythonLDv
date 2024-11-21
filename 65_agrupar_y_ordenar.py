"""
Escribe una función que reciba una lista de números y devuelva una lista con los números ordenados en grupos de pares e impares.
Primero todos los pares en orden ascendente, luego todos los impares en orden ascendente.
"""
def agrupar_y_ordenar(lista_numeros):
    pares = sorted([num for num in lista_numeros if num % 2 == 0])
    impares = sorted([num for num in lista_numeros if num % 2 != 0])
    return pares + impares

# Ejemplo de uso
print(agrupar_y_ordenar([7, 2, 4, 5, 1, 6]))  # [2, 4, 6, 1, 5, 7]
