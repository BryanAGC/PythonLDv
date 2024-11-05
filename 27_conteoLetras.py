"""
ESCRIBE UNA FUNCION QUE CUENTE CUANTAS LETRAS
DE CADA UNA HAY EN UNA FRASE
"""

def contar_letras(cadena):
    conteo = {}
    cadena = cadena.replace(" ", "").lower()  

    for letra in cadena:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    
    return conteo


cadena = "Hola Mundo"
resultado = contar_letras(cadena)
print(f"Conteo de letras: {resultado}")
