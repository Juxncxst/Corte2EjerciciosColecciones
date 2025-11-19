numeros = list(map(int, input().split()))
promedio = sum(numeros) / len(numeros)
mayores = [n for n in numeros if n > promedio]
print(promedio)
print(sorted(mayores))
