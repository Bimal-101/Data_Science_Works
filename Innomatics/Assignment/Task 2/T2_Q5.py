# Task 2 - Q5 : Happiness Index

n,m = (int(j) for j in input().split())

l1 = list(map(int, input().split()))
l2 = set(map(int, input().split()))
l3 = set(map(int, input().split()))

h = 0

for i in l1:
    if i in l2:
        h += 1
    elif i in l3:
        h += -1
print(h)
