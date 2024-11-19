"""
Escribe una función que reciba una lista de números y devuelva 
una nueva lista con los números elevados al cuadrado.
"""
def cuadrados(lista_numeros):
    return [num ** 2 for num in lista_numeros]


lista = [1, 2, 3, 4, 5]
print(cuadrados(lista))  # [1, 4, 9, 16, 25]
