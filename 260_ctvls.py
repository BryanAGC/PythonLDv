def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")

print(contar_vocales("Python es genial"))
