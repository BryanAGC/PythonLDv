def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(son_anagramas("amor", "Roma"))
print(son_anagramas("hola", "adios"))
