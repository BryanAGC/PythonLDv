"""
Escribe una función que reciba una lista de números y devuelva 
True si la lista está ordenada en orden ascendente, y False en caso contrario.
"""

def esta_ordenada(lista_numeros):
    for i in range(len(lista_numeros) - 1):
        if lista_numeros[i] > lista_numeros[i + 1]:  
            return False
    return True


lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 4, 5]
print(f"La lista {lista1} está ordenada: {esta_ordenada(lista1)}")
print(f"La lista {lista2} está ordenada: {esta_ordenada(lista2)}")
