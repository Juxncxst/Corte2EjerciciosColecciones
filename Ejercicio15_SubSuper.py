A = eval(input())
B = eval(input())
if A.issubset(B):
    print("A es subconjunto de B")
if B.issuperset(A):
    print("B es superconjunto de A")
