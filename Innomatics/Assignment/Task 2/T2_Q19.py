# Task 2 - Q19 : Check Strict Super set

a = set(map(int, input().split()))

n = int(input())
c = 0
for i in range(n):
    b = set(map(int, input().split()))

    if b.intersection(a) == b:
        c += 0
    else:
        c += 1
if c == 0:
    print("True")
else:
    print("False")
