"""
CREA UNA FUNCION QUE MULTIPLIQUE 
DOS NUMERO SIN UTILIZAR *
"""

def multiplicar (a,b):
    total = 0 
    for i in range(a):
        total +=b
    return total

print(multiplicar(4,6))