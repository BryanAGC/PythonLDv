"""
Escribe una función que convierta una lista de cadenas en una sola cadena, separada por espacios.
"""
def lista_a_cadena(lista):
    return ' '.join(lista)

# Ejemplo de uso
lista = ["Hola", "mundo", "Python"]
resultado = lista_a_cadena(lista)
print(f"La cadena resultante es: '{resultado}'")
