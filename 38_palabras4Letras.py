"""
Escribe una función que reciba una cadena de texto y devuelva
la cantidad de palabras que tienen más de cuatro letras.
"""

def contar_palabras_largas(cadena):
    palabras = cadena.split()  # Divide la cadena en palabras
    return sum(1 for palabra in palabras if len(palabra) > 4)

# Ejemplo de uso
cadena = "Este es un ejemplo de cadena con varias palabras largas"
resultado = contar_palabras_largas(cadena)
print(f"Número de palabras con más de cuatro letras: {resultado}")
