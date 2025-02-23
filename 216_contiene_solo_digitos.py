"""
Escribe una función que determine si una cadena contiene solo dígitos.
"""
def contiene_solo_digitos(cadena):
    return cadena.isdigit()

# Ejemplo de uso
cadena = "123456"
if contiene_solo_digitos(cadena):
    print(f"La cadena {cadena} contiene solo dígitos.")
else:
    print(f"La cadena {cadena} no contiene solo dígitos.")
