#Task 6 - Q3 : Transpose and Flatten

import numpy

N, M = map(int, input().split())

l = []

for i in range(N):
    l1 = list(map(int,input().strip().split()))
    l.append(l1)

a = numpy.array(l)

t = numpy.transpose(a)
f = a.flatten()
print(t)
print(f)
