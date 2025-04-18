"""
Convierte un número en formato romano a su equivalente en entero.
"""
def romano_a_entero(s):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s) - 1):
        if valores[s[i]] < valores[s[i + 1]]:
            total -= valores[s[i]]
        else:
            total += valores[s[i]]
    return total + valores[s[-1]]

# Ejemplo de uso
print(romano_a_entero("XIV"))  # 14
