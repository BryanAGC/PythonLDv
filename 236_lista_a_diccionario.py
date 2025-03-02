"""
Escribe una función que reciba una lista de tuplas y la convierta en un diccionario.
"""
def lista_a_diccionario(lista):
    return dict(lista)

# Ejemplo de uso
lista = [("a", 1), ("b", 2), ("c", 3)]
resultado = lista_a_diccionario(lista)
print(f"Diccionario resultante: {resultado}")
#