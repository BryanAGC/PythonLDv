def es_palindromo(numero):
    return str(numero) == str(numero)[::-1]

print(es_palindromo(121))  
print(es_palindromo(123))  
