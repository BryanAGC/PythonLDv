"""
Dada una expresión matemática como cadena, evalúa su resultado. 
Soporta +, -, *, / y paréntesis.
"""
def evaluar_expresion(expresion):
    return eval(expresion)

expresion = "(2 + 3) * (5 - 2) / 3"
print(evaluar_expresion(expresion))  # 5.0
