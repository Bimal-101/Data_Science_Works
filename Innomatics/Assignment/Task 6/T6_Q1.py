#Task 6 - Q1 : Arrays - Numpy


import numpy

def arrays(arr):
    arr = arr[::-1]
    a = numpy.array(arr,float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
