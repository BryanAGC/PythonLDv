"""
EJERCICIO 2:
IMPRIME OS NUMEROS DEL 1 A n
SIN USAR BUCLES(FOR,WHILE)
"""
def pec(i,n):
    if i <= n :
        print(i)
        i +=  1
        pec(i,n)
pec(1,100)