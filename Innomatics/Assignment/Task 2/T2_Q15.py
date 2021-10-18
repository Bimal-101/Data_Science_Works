# Task 2 - Q15 : Symmetric Difference

n = int(input())
x = set(map(int, input().split()))
b = int(input())
y = set(map(int, input().split()))

d1 = x.difference(y)
d2 = y.difference(x)

u = d1.union(d2)

print(len(u))
