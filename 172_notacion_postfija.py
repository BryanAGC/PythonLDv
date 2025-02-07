"""
Convierte una expresión matemática de notación infija a postfija.
"""
def prioridad(op):
    prioridades = {'+': 1, '-': 1, '*': 2, '/': 2}
    return prioridades.get(op, 0)

def infija_a_postfija(expresion):
    salida = []
    pila = []
    for token in expresion:
        if token.isalnum():
            salida.append(token)
        elif token in "+-*/":
            while pila and prioridad(pila[-1]) >= prioridad(token):
                salida.append(pila.pop())
            pila.append(token)
        elif token == "(":
            pila.append(token)
        elif token == ")":
            while pila and pila[-1] != "(":
                salida.append(pila.pop())
            pila.pop()
    while pila:
        salida.append(pila.pop())
    return " ".join(salida)

expresion = "3 + 5 * ( 2 - 8 )"
print(infija_a_postfija(expresion.split()))  # '3 5 2 8 - * +'
