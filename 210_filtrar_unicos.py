"""
Escribe una función que reciba una lista de números y devuelva una nueva lista con solo los elementos únicos (sin duplicados).
"""
def filtrar_unicos(lista):
    return list(set(lista))

# Ejemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5]
resultado = filtrar_unicos(lista)
print(f"Elementos únicos: {resultado}")
