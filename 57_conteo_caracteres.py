"""
Escribe una función que reciba una cadena y devuelva 
un diccionario con el conteo de cada carácter (ignorar espacios).
"""
def conteo_caracteres(cadena):
    return {caracter: cadena.count(caracter) for caracter in cadena.replace(" ", "")}


print(conteo_caracteres("hola mundo"))  # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
