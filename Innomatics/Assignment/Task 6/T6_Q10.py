#Task 6 - Q10 : Min Max

import numpy as np

N, M = map(int,input().split())

l = []

for i in range(N):
    l1 = list(map(int,input().split()))
    l.append(l1)
    
a = np.array(l)

mi = np.min(a,axis = 1)

print(np.max(mi))

