# Task 2 - Q12 : Union


n = int(input())
x = set(map(int, input().split()))
b = int(input())
y = set(map(int, input().split()))

u = x.union(y)

print(len(u))
