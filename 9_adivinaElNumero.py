import random
ai = random.randint(1,100)
intentos= 0
numero = -1
while numero != ai:
    numero = int(input("introdce un numero: "))
    intentos +=1
    if numero > ai:
        print("Te has pasado")
    elif numero < ai:
        print("Te has quedado corto")
print(f"Has terminado, el nmero era: {ai} ")
print(f"Te ha tomado {intentos} intentos conseguirlo")