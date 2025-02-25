"""
Escribe una función que determine si un año es bisiesto.
"""
def es_bisiesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Ejemplo de uso
ano = 2020
if es_bisiesto(ano):
    print(f"{ano} es un año bisiesto.")
else:
    print(f"{ano} no es un año bisiesto.")
