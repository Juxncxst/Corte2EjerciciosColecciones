n = int(input())
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(1 if i==j else 0)
    matriz.append(fila)
for f in matriz:
    print(f)
