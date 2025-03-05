import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print(generar_contraseña(12))
