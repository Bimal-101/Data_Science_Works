# Task 2 - Q16 : Set Mutations


n = int(input())
a = set(map(int, input().split()))

m = int(input())

for i in range(m):
    b = input().split()
    if b[0] == "intersection_update":
        c = set(map(int, input().split()))
        a.intersection_update(c)
    elif b[0] == "update":
        d = set(map(int, input().split()))
        a.update(d)
    elif b[0] == "symmetric_difference_update":
        e = set(map(int, input().split()))
        a.symmetric_difference_update(e)
    else:
        f = set(map(int, input().split()))
        a.difference_update(f)
        
print(sum(a))
