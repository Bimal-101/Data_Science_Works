#Task 2 - Q17 : Captains Room


n = int(input())
a = map(int, input().split())

l = list(a)
x = []
y = []


for i in l:
    if i not in x:
        x += [i]
    else:
        y += [i]
        
x = set(x)
y = set(y)
z = x.difference(y)

for j in z:
    print(j)
