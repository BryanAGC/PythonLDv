"""
Crea una función que calcule el valor final de una inversión a partir del monto inicial, la tasa de interés anual y el número de años.
"""
def calcular_intereses_compuestos(principal, tasa, anos):
    return principal * (1 + tasa) ** anos

# Ejemplo de uso
principal = 1000  # Monto inicial
tasa = 0.05  # Tasa de interés anual
anos = 10  # Número de años
valor_final = calcular_intereses_compuestos(principal, tasa, anos)
print(f"El valor final es: {valor_final:.2f}")
