"""
Verifica si una palabra es un isograma (no tiene letras repetidas).
"""
def es_isograma(palabra):
    palabra = palabra.lower()
    return len(set(palabra)) == len(palabra)

# Ejemplo de uso
print(es_isograma("murcielago"))  # True
print(es_isograma("programacion"))  # False
