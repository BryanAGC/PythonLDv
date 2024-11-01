import math

def calcular_area(radio):
    return math.pi * radio ** 2

def calcular_perimetro(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area(radio)
perimetro = calcular_perimetro(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
