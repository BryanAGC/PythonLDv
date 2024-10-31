"""
CREA UNA  FUNCION QUE DEVUELVA EL NUMERO
CONTENIDO EN UNA FRACE
"""

def devolver_numero(frase):
    numeros=[]
    for letra in frase:
        if letra.isdigit():
            numeros.append(int(letra))
    return numeros

print(devolver_numero("hola 21 que tal 12 estas"))