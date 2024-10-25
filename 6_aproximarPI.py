"""
Aproximar el numero pi
"""

n = 2*int(input("n:"))
contador = 1
pi = 0
for t in range(1,n+1,2):
    if contador%2:
        pi +=4/t 
    else:
        pi -= 4/t
    contador += 1
    print(pi)
# se usa la serie de Leibniz