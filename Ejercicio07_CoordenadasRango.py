x, y = map(int, input().split())
min_r = int(input())
max_r = int(input())
if min_r <= x <= max_r and min_r <= y <= max_r:
    print("Dentro del rango")
else:
    print("Fuera del rango")
