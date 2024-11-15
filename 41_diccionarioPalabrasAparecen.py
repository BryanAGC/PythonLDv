"""
Escribe una función que reciba una cadena de texto y devuelva un diccionario donde
las claves sean las letras y los valores sean el número de
veces que aparece cada letra en la cadena. Ignora los espacios y convierte todo a minúsculas
"""

def contar_letras(cadena):
    cadena = cadena.replace(" ", "").lower()  # Elimina espacios y convierte a minúsculas
    conteo = {}
    for letra in cadena:
        if letra in conteo:
            conteo[letra] += 1  # Incrementa el contador si ya existe la letra en el diccionario
        else:
            conteo[letra] = 1  # Agrega la letra al diccionario con un conteo inicial de 1
    return conteo

# Ejemplo de uso
cadena = "Hola Mundo"
resultado = contar_letras(cadena)
print(f"Conteo de letras: {resultado}")
