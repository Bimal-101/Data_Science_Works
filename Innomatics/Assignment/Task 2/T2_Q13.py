# Task 2 - Q13 : Intersection



n = int(input())
x = set(map(int, input().split()))
b = int(input())
y = set(map(int, input().split()))

i = x.intersection(y)

print(len(i))
