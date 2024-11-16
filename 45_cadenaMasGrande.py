"""
Escribe una función que reciba una lista de cadenas
de texto y devuelva la cadena más larga de la lista. Si hay varias cadenas con la misma longitud máxima, 
devuelve la primera que aparezca.
"""

def cadena_mas_larga(lista_cadenas):
    if not lista_cadenas:  # Verifica si la lista está vacía
        return None
    return max(lista_cadenas, key=len)  # Encuentra la cadena con la mayor longitud

# Ejemplo de uso
lista = ["gato", "elefante", "perro", "hipopótamo"]
resultado = cadena_mas_larga(lista)
print(f"La cadena más larga es: {resultado}")
