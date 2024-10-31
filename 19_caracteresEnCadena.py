"""
HAZ UNA FUNCION QUE DEVUELVA CUANTAS VECES 
APARECE UAN LETRA EN UNA CADENA 
(SIN COUNT)
"""

def contar_letra(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

cadena = "hola que tal"
letra = "a"
print(f"La letra '{letra}' aparece {contar_letra(cadena, letra)} veces en la cadena.")
