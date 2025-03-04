def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(fibonacci(10))  
