"""
Crea un juego de ahorcado en Python con una lista de palabras aleatorias.
"""
import random

def ahorcado():
    palabras = ["python", "programacion", "computadora", "inteligencia"]
    palabra = random.choice(palabras)
    intentos = 6
    progreso = ["_"] * len(palabra)

    while intentos > 0 and "_" in progreso:
        print(" ".join(progreso))
        letra = input("Adivina una letra: ").lower()

        if letra in palabra:
            for i, c in enumerate(palabra):
                if c == letra:
                    progreso[i] = letra
        else:
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")

    print("Ganaste" if "_" not in progreso else f"Perdiste. La palabra era {palabra}")

ahorcado()
