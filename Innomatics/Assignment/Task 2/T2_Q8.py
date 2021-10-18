#Task 2 - Q8 : Finding Average - sets

from __future__ import division

def average(array):
    array = set(array)
    avg = sum(array)/len(array)
    return avg

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
