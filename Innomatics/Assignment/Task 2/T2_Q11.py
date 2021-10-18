#Task 2 - Q11 : Discard, Remove and POP

n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range(m):
    a = input().split()
    if a[0] == "remove":
        s.remove(int(a[1]))
    elif a[0] == "discard":
        s.discard(int(a[1]))
    else:
        s.pop()

if s == {}:
    print("0")
else:
    print(sum(s))
