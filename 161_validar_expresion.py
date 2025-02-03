"""
Verifica si una expresión matemática tiene los paréntesis correctamente balanceados usando una pila.
"""
def es_valida(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expresion:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila or pila.pop() != pares[char]:
                return False

    return not pila

expresion = "{[()]}"
print(es_valida(expresion))  # True

expresion = "{[(])}"
print(es_valida(expresion))  # False
