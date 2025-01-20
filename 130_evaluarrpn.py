"""
Evalúa una expresión en notación postfija (RPN).
"""
def evaluar_rpn(expresion):
    pila = []
    for token in expresion:
        if token.isdigit():
            pila.append(int(token))
        else:
            b, a = pila.pop(), pila.pop()
            pila.append(eval(f"{a}{token}{b}"))
    return pila[0]

# Ejemplo de uso
print(evaluar_rpn(["2", "1", "+", "3", "*"]))  # 9
