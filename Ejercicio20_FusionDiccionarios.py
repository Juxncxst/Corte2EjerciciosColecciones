A = eval(input())
B = eval(input())
f1 = A.copy()
f1.update(B)
f2 = A | B
print(f1)
print(f2)
