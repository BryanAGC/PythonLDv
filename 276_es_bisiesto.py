"""
Escribe una función que determine si un año es bisiesto o no.
"""
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

print(es_bisiesto(2024))  # True
print(es_bisiesto(2023))  # False
