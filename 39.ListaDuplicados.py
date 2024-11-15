"""
Escribe una función que reciba una lista de números y devuelva 
la lista sin duplicados, manteniendo el orden original.
"""

def eliminar_duplicados(lista_numeros):
    lista_sin_duplicados = []
    for numero in lista_numeros:
        if numero not in lista_sin_duplicados:  # Solo agrega si no está ya en la lista
            lista_sin_duplicados.append(numero)
    return lista_sin_duplicados

# Ejemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(lista)
print(f"Lista sin duplicados: {resultado}")
