"""
Verifica si dos palabras son anagramas (contienen las mismas letras en diferente orden).
"""
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
print(es_anagrama("amor", "roma"))  # True
print(es_anagrama("ratón", "torna"))  # False
