def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola mundo"))
