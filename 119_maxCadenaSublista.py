"""
Encuentra la suma máxima de una sublista contigua en una lista de números enteros.
"""
def max_suma_sublista(lista):
    max_actual = max_global = lista[0]
    for num in lista[1:]:
        max_actual = max(num, max_actual + num)
        max_global = max(max_global, max_actual)
    return max_global

# Ejemplo de uso
print(max_suma_sublista([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 ([4, -1, 2, 1])
