#Task 6 - Q15 : Linear Algebra


import numpy as np

N = int(input())

l = []
for i in range(N):
    A = list(map(float,input().split()))
    l.append(A)
    
a = np.array(l)

print(round(np.linalg.det(a),2))
