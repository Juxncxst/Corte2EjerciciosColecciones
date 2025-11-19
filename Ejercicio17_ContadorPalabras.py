frase = input().split()
cont = {}
for p in frase:
    cont[p] = cont.get(p,0)+1
print(cont)
