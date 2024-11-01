def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

opcion = input("¿Quieres convertir a Fahrenheit o Celsius? (F/C): ").lower()

if opcion == "f":
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(celsius):.2f}")
elif opcion == "c":
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    print(f"La temperatura en Celsius es: {fahrenheit_a_celsius(fahrenheit):.2f}")
else:
    print("Opción no válida.")
