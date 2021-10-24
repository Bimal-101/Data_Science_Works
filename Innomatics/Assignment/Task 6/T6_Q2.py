#Task 6 - Q2 : Shape and Reshape

import numpy

lis = list(map(int ,input().split()))

a = numpy.array(lis)

print(numpy.reshape(a,(3,3)))
