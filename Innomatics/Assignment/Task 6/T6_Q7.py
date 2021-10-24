#Task 6 - Q7 : Array Mathematics


import numpy as np

N, M = map(int, input().split())

l1 = []
l2 = []

for i in range(N):
    a = list(map(int,input().split()))
    l1.append(a)
    
for i in range(N):
    b = list(map(int,input().split()))
    l2.append(b)
    
c = np.array(l1)
d = np.array(l2)


print(c+d)
print(c-d)
print(c*d)
print(c//d)
print(c%d)
print(c**d)
