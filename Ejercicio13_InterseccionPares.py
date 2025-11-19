A = list(map(int, input().split()))
B = list(map(int, input().split()))
paresA = {x for x in A if x%2==0}
paresB = {x for x in B if x%2==0}
print(paresA & paresB)
