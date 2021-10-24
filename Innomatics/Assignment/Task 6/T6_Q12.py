#Task 6 - Q12 : Dot and Cross

import numpy as np

N = int(input())

l1 = []
l2 = []

for i in range(N):
    l3 = list(map(int,input().split()))
    l1.append(l3)
for i in range(N):
    l4 = list(map(int,input().split()))
    l2.append(l4)
    
a = np.array(l1)
b = np.array(l2)

print(np.dot(a,b))
