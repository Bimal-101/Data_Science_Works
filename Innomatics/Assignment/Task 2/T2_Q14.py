# Task 2 - Q14 : Difference


n = int(input())
x = set(map(int, input().split()))
b = int(input())
y = set(map(int, input().split()))

d = x.difference(y)

print(len(d))
