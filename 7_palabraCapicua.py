"""
FUNCION QUE DEVUELVA SI UNA PARABRALA
ES CAPICUA (SE LEE IGUAL AL REVEZ)
"""

def capicua(palabra):
    revez = ""
    for i in range(len(palabra)-1,-1,-1):
        revez += palabra [i]
        
    return palabra == revez

print(capicua("holaaloh"))