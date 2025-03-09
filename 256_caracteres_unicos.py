def caracteres_unicos(cadena):
    return len(set(cadena)) == len(cadena)

print(caracteres_unicos("hola"))
print(caracteres_unicos("mundo"))
