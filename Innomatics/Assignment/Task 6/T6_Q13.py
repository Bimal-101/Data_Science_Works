#Task 6 - Q 13 : Inner Outer

import numpy as np

A = map(int,input().split())
B = map(int,input().split())

a = np.array(list(A))
b = np.array(list(B))

print(np.inner(a,b))
print(np.outer(a,b))
