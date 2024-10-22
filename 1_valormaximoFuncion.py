"""" 
EJERCICIO:
HAZ UNA FUNCION QUE ACEPTE
COMO PARAMETROS UNA LISTA Y DEVUELVA EL MAVOR MAXIMO
milista = [13, 5, 78, 38, 1, 35]
"""
def devuelveMayor(mi_lista):
    mayor = mi_lista[0]
    for n in mi_lista:
        if n > mayor:
            mayor = n
    return mayor

print(devuelveMayor(milista))
