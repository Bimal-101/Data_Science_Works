# Task 3 - Q2 : Finding angle

import math

ab = int(input())
bc = int(input())
x = float(ab/bc)

the = math.atan(x)
th = math.degrees(the)

print(str(round(th))+chr(176))
