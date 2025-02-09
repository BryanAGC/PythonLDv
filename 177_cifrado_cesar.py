"""
Implementa un cifrado César que permite desplazamientos dinámicos por palabra.
"""
def cifrar(texto, desplazamientos):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = []
    palabras = texto.split()

    for i, palabra in enumerate(palabras):
        desplazamiento = desplazamientos[i % len(desplazamientos)]
        nueva_palabra = ''.join(alfabeto[(alfabeto.index(c) + desplazamiento) % 26] if c in alfabeto else c for c in palabra)
        resultado.append(nueva_palabra)
    
    return ' '.join(resultado)

texto = "hola mundo secreto"
desplazamientos = [3, 1, 4]  
print(cifrar(texto, desplazamientos))
