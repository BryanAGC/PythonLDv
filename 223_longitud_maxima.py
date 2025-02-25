"""
Escribe una función que reciba una lista de cadenas y devuelva la longitud de la cadena más larga.
"""
def longitud_maxima(lista):
    return len(max(lista, key=len))

# Ejemplo de uso
lista = ["manzana", "banana", "kiwi", "cereza"]
resultado = longitud_maxima(lista)
print(f"La longitud del elemento más largo es: {resultado}")
