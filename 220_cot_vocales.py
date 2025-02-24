"""
Escribe una función que cuente cuántas vocales hay en una cadena.
"""
def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in 'aeiou')

# Ejemplo de uso
cadena = "Hola Mundo"
resultado = contar_vocales(cadena)
print(f"La cantidad de vocales en '{cadena}' es: {resultado}")
