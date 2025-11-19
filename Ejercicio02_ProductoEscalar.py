lista_a = list(map(int, input().split()))
lista_b = list(map(int, input().split()))
if len(lista_a) != len(lista_b):
    print("Error")
else:
    producto = 0
    for i in range(len(lista_a)):
        producto += lista_a[i] * lista_b[i]
    print(producto)
