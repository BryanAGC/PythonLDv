"""
Escribe una función que cuente cuántas veces aparece un elemento en una lista.
"""
def contar_apariciones(lista, elemento):
    return lista.count(elemento)

# Ejemplo de uso
lista = [1, 2, 2, 3, 2, 4, 5]
elemento = 2
resultado = contar_apariciones(lista, elemento)
print(f"El elemento {elemento} aparece {resultado} veces en la lista.")
