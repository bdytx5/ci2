import numpy as np
import struct
import numpy as np
import random
import math
import cv2


def Min1and1MinusAplusB(a, b):
    firstOp = (1 - a) + b
    return min(1, firstOp)


# A = small 1 2 3 4 
A = np.array([1.0,0.8,0.0,0.0])
# B = Medium a b c d e 
B = np.array([0.0,0.5,1.0,0.5,0.0])
# if (U is small (A)) then (V is Medium (B))

# so if U is A' ----> then V is B'    |||| from B'(y) = R(x,y)*A'(x)
# calc R
R = np.zeros((np.size(A), np.size(B)))

x=-1
y=-1
for a in A:
    x = x+1
    y = -1
    for b in B:
        y=y+1
        v = Min1and1MinusAplusB(a,b)
        R[x,y] = v
print(R)

res = np.zeros(R.shape[1])
Ap = np.array([1.0,0.8,0.0,0.0])
for x in range(R.shape[1]):
    preMax = np.zeros(np.size(Ap))
    for y in range(np.size(Ap)):
        preMax[y] = min(Ap[y],R[y,x])
    res[x] = max(preMax)

print(res)
    
# say we have A is small and B is big then C is Medium 




