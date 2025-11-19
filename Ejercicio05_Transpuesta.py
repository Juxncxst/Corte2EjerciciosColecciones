n = int(input())
m = int(input())
matriz = [list(map(int, input().split())) for _ in range(n)]
trans = []
for j in range(m):
    fila = []
    for i in range(n):
        fila.append(matriz[i][j])
    trans.append(fila)
for f in trans:
    print(f)
