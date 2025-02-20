"""
Escribe una función que calcule la edad de una persona a partir de su fecha de nacimiento.
"""
from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Ejemplo de uso
fecha_nacimiento = datetime(1995, 5, 10)
edad = calcular_edad(fecha_nacimiento)
print(f"La edad es: {edad} años")
