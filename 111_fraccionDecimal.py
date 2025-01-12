"""
Convierte una fracción dada en su representación decimal.
"""
from fractions import Fraction

def fraccion_a_decimal(numerador, denominador):
    return float(Fraction(numerador, denominador))

# Ejemplo de uso
print(fraccion_a_decimal(3, 4))  # 0.75
