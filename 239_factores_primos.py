def factores_primos(n):
    i = 2
    factores = []
    while i * i <= n:
        while n % i == 0:
            factores.append(i)
            n //= i
        i += 1
    if n > 1:
        factores.append(n)
    return factores

print(factores_primos(84))  
