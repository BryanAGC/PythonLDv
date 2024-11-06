"""
Escribe una función que reciba una cadena de texto y devuelva True si la cadena es un pangrama 
(es decir, contiene todas las letras del alfabeto al menos una vez), y False en caso contrario.
"""
import string

def es_pangrama(cadena):
    alfabeto = set(string.ascii_lowercase)  
    cadena = cadena.lower()  
    letras_en_cadena = set(cadena)  
    return alfabeto.issubset(letras_en_cadena)  


cadena = "El veloz murciélago hindú comía feliz cardillo y kiwi."
resultado = es_pangrama(cadena)
print(f"¿La cadena es un pangrama? {resultado}")
