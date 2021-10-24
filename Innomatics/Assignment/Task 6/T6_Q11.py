#Task 6 - Q 11 : Mean, Var, Std

import numpy as np

N, M = map(int,input().split())

l = []
for i in range(N):
    l1 = list(map(int,input().split()))
    l.append(l1)

a = np.array(l)

print(np.mean(a, axis = 1))
print(np.var(a, axis = 0))
b = np.std(a, axis = None)
print(round(b,11))
