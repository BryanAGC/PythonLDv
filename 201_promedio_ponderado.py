"""
Escribe una función que calcule el promedio ponderado de un conjunto de calificaciones y pesos.
"""
def promedio_ponderado(calificaciones, pesos):
    suma_ponderada = sum(c * p for c, p in zip(calificaciones, pesos))
    suma_pesos = sum(pesos)
    return suma_ponderada / suma_pesos if suma_pesos != 0 else 0

# Ejemplo de uso
calificaciones = [8, 9, 7]
pesos = [0.5, 0.3, 0.2]
resultado = promedio_ponderado(calificaciones, pesos)
print(f"El promedio ponderado es: {resultado:.2f}")
