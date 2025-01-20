"""
Dada una cadena con una expresión matemática, valida si los paréntesis están bien balanceados.
"""
def es_valida(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for char in expresion:
        if char in pares.values():
            pila.append(char)
        elif char in pares.keys():
            if not pila or pila.pop() != pares[char]:
                return False
    return not pila

# Ejemplo de uso
print(es_valida("{[()]}"))  # True
print(es_valida("{[(])}"))  # False
