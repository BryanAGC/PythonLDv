"""
Escribe una función que reciba una lista de números y devuelva True 
si todos los números son pares, y False en caso contrario.
"""

def todos_pares(lista_numeros):
    for numero in lista_numeros:
        if numero % 2 != 0:  
            return False
    return True


lista1 = [2, 4, 6, 8]
lista2 = [1, 2, 3, 4]
print(f"¿Todos los números en lista1 son pares? {todos_pares(lista1)}")
print(f"¿Todos los números en lista2 son pares? {todos_pares(lista2)}")
