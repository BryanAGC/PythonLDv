"""
Escribe una función que reciba una cadena y cuente cuántas vocales contiene.
"""
def contar_vocales(cadena):
    return sum(1 for c in cadena if c.lower() in 'aeiou')

# Ejemplo de uso
cadena = "Hola Mundo"
resultado = contar_vocales(cadena)
print(f"La cadena contiene {resultado} vocales.")
