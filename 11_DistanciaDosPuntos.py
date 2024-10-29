"""
CREA UNA FUNCION QUE DEVUELVA 
LA DISTANCIA ENTRE DOS PUNTOS
"""
import math

def distancia(p1,p2):
    distx = p1[0]-p2[0]
    disty = p1[1]-p2[1]
    distancia_total = math.sqrt(distx**2 + disty**2)
    return distancia_total

print(distancia([5,7],[3,2]))