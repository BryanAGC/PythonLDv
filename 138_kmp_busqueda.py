"""
Implementa el algoritmo de Knuth-Morris-Pratt (KMP) para buscar un patrón en un texto.
"""
def calcular_lps(patron):
    lps = [0] * len(patron)
    j = 0
    for i in range(1, len(patron)):
        while j > 0 and patron[i] != patron[j]:
            j = lps[j - 1]
        if patron[i] == patron[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_busqueda(texto, patron):
    lps = calcular_lps(patron)
    j = 0
    for i in range(len(texto)):
        while j > 0 and texto[i] != patron[j]:
            j = lps[j - 1]
        if texto[i] == patron[j]:
            j += 1
        if j == len(patron):
            print(f"Patrón encontrado en índice {i - j + 1}")
            j = lps[j - 1]

# Ejemplo de uso
kmp_busqueda("ababcabcabababd", "ababd")
