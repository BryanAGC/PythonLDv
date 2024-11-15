"""
Escribe una función que reciba una lista de números y
devuelva True si la lista está ordenada en orden ascendente, y False en caso contrario.
"""

def esta_ordenada(lista_numeros):
    return lista_numeros == sorted(lista_numeros)  # Compara la lista con su versión ordenada

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 4, 5]
print(f"¿La lista1 está en orden ascendente? {esta_ordenada(lista1)}")
print(f"¿La lista2 está en orden ascendente? {esta_ordenada(lista2)}")
