#Task 2 - Q 10  : Set Add

n = int(input())
c = []
for i in range(n):
    a = input()
    if a != c:
        c += [a]
d = set(c)
print(len(d))
