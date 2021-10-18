# Task 2 - Q9 : Symmetric Diffference

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

c = a.difference(b)
d = b.difference(a)

sd = c.union(d)
sd = list(sd)
sd.sort()
for i in sd:
    print(i)
