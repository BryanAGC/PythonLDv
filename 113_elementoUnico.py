"""
Dada una lista donde todos los elementos se repiten excepto uno, encuentra el elemento único.
"""
def encontrar_unico(lista):
    unico = 0
    for num in lista:
        unico ^= num  # Operación XOR
    return unico

# Ejemplo de uso
print(encontrar_unico([1, 2, 3, 2, 1]))  # 3
