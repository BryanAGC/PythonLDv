"""
Escribe una función que simule el juego de adivinar un número. 
El número debe ser generado aleatoriamente y el usuario tiene 5 intentos para adivinarlo.
"""
import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 5
    print("Adivina el número (entre 1 y 100):")
    while intentos > 0:
        intento = int(input(f"Te quedan {intentos} intentos. Ingresa tu número: "))
        if intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            return
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        intentos -= 1
    print(f"Lo siento, el número era {numero_secreto}.")

# Ejemplo de uso
adivinar_numero()
