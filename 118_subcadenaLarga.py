"""
Encuentra la subcadena más larga de una cadena que no contenga caracteres repetidos.
"""
def subcadena_mas_larga(s):
    seen = {}
    inicio = max_long = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= inicio:
            inicio = seen[char] + 1
        seen[char] = i
        max_long = max(max_long, i - inicio + 1)
    return max_long

# Ejemplo de uso
print(subcadena_mas_larga("abcabcbb"))  # 3 ("abc")
print(subcadena_mas_larga("bbbbb"))  # 1 ("b")
