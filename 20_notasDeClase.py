"""
PROGRAMA QUE RECIBA NOTAS DE CLASE HASTA 
QUE RECIBA -1 DEBE IMPRIMIR LA MEDIA
"""
def calcular_media():
    notas = []
    while True:
        nota = float(input("Introduce una nota (o -1 para terminar): "))
        if nota == -1:
            break
        notas.append(nota)
    
    if notas: 
        media = sum(notas) / len(notas)
        print(f"La media de las notas es: {media:.2f}")
    else:
        print("No se introdujeron notas.")

calcular_media()
