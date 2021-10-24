#Task 6 - Q14 : Polynomials 

import numpy as np

P = map(float, input().split())
x = int(input())

a = np.array(list(P))

print(np.polyval(a,x))
