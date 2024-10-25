"""
IMPRIME LOS PRIMEROS 20  NUMEROS 
DE LA SUCESION DE FIGONACCI
"""

def figonacci(n):
    if n < 2:
        return n
    else:
        return figonacci(n-1) + figonacci(n-2)
    
for i in range(20):
    print(figonacci(i))