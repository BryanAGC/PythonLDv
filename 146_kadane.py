"""
Encuentra la suma máxima de un subarray en un array de números enteros utilizando el algoritmo de Kadane.
"""
def max_subarray(arr):
    max_actual = max_global = arr[0]
    
    for num in arr[1:]:
        max_actual = max(num, max_actual + num)
        max_global = max(max_global, max_actual)

    return max_global

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr))  # Salida: 6 (subarray [4, -1, 2, 1])
