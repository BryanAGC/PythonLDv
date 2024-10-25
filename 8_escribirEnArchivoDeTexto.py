"""
ESCRIBE LOS NUMEROS DEL 1-100
EN UN ARCHIVO DE TEXTO
"""
file = open("numeros.txt","w")
for  i in range(100):
    file.write(f"{i}\n")
file.close()