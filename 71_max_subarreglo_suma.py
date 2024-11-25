"""
Escribe una función que reciba una lista de números y encuentre el subarreglo contiguo con la suma más grande 
(utilizando el algoritmo de Kadane).
"""
def max_subarreglo_suma(lista):
    max_actual = max_global = lista[0]
    for num in lista[1:]:
        max_actual = max(num, max_actual + num)
        if max_actual > max_global:
            max_global = max_actual
    return max_global


print(max_subarreglo_suma([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 (subarreglo: [4, -1, 2, 1])
