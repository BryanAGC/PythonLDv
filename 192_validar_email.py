"""
Verifica si un correo electrónico tiene el formato correcto.
"""
import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(patron, email))

print(validar_email("ejemplo@mail.com"))
print(validar_email("correo@incorrecto"))
