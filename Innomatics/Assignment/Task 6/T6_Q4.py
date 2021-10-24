#Task 6 - Q4 : Concentrate

import numpy



N, M, P = map(int,input().split())

l1 = []
l2 = []

for i in range(N):
    lis1 = list(map(int,input().split()))
    l1.append(lis1)

for j in range(M):
    lis2 = list(map(int,input().split()))
    l2.append(lis2)
    
a = numpy.array(l1)
b = numpy.array(l2)

print(numpy.concatenate((a,b)))
