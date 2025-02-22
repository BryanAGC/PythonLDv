"""
Escribe una función que reciba una cadena y reemplace una subcadena específica con otra subcadena.
"""
def reemplazar_subcadena(cadena, subcadena_a_reemplazar, subcadena_nueva):
    return cadena.replace(subcadena_a_reemplazar, subcadena_nueva)

# Ejemplo de uso
cadena = "Hola mundo, bienvenidos al mundo"
subcadena_a_reemplazar = "mundo"
subcadena_nueva = "universo"
resultado = reemplazar_subcadena(cadena, subcadena_a_reemplazar, subcadena_nueva)
print(resultado)
