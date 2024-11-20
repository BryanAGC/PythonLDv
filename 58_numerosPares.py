"""
Escribe una función que reciba una lista de números y devuelva una nueva lista con los números que son pares.
"""
def numeros_pares(lista_numeros):
    return [num for num in lista_numeros if num % 2 == 0]


print(numeros_pares([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
