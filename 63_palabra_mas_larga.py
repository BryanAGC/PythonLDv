"""
Escribe una función que reciba una cadena y devuelva la palabra más larga en la cadena. 
En caso de empate, devuelve la primera que aparece.
"""
def palabra_mas_larga(cadena):
    palabras = cadena.split()
    return max(palabras, key=len)

# Ejemplo de uso
print(palabra_mas_larga("Este es un ejercicio interesante y complejo"))  # "interesante"
