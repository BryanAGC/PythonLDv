"""
Implementa la compresión de cadenas usando la codificación Run-Length Encoding (RLE).
"""
def comprimir_rle(cadena):
    resultado = []
    i = 0
    while i < len(cadena):
        contador = 1
        while i + 1 < len(cadena) and cadena[i] == cadena[i + 1]:
            contador += 1
            i += 1
        resultado.append(cadena[i] + str(contador))
        i += 1
    return ''.join(resultado)

# Ejemplo de usoo
print(comprimir_rle("aaabbcddd"))  # "a3b2c1d3"
