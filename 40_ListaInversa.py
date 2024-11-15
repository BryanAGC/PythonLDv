"""
    Escribe una función que reciba una lista de palabras y 
    devuelva una nueva lista con las palabras en orden inverso.
"""

def invertir_lista_palabras(lista_palabras):
    return lista_palabras[::-1]  # Invierte el orden de la lista

# Ejemplo de uso
lista = ["perro", "gato", "pájaro"]
resultado = invertir_lista_palabras(lista)
print(f"Lista en orden inverso: {resultado}")
