n = int(input())
m = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
C = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(A[i][j] + B[i][j])
    C.append(fila)
for f in C:
    print(f)
