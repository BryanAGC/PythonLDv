"""
CREA UNA FUNCION QUE DEVUELVA LOS NUMERO 
PARES ENTRE A Y B
"""

def pares(A,B):
    for n in range(A,B):
        if n % 2 ==0:
            print(n)

pares(2,18)