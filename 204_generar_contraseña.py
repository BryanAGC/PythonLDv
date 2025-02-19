"""
Escribe una función que genere una contraseña aleatoria con una longitud específica y contenga letras, números y caracteres especiales.
"""
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Ejemplo de uso
contraseña = generar_contraseña(12)
print(f"La contraseña generada es: {contraseña}")
