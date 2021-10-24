#Task 6 - Q8 : Floor, Ceil, Rint

import numpy as np
np.set_printoptions(legacy='1.13')

l = list(map(float,input().split()))
a = np.array(l)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
