#Task 6 - Q9 : Sum and Prod

import numpy as np

N, M = map(int,input().split())

l = []
for i in range(N):
    l1 = list(map(int,input().split()))
    l.append(l1)

a = np.array(l)

s = np.sum(a,axis = 0)

print(np.prod(s))
