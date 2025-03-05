def son_anagramas(cadena1, cadena2):
    return sorted(cadena1) == sorted(cadena2)

print(son_anagramas("roma", "amor"))  
print(son_anagramas("hola", "mundo"))  
