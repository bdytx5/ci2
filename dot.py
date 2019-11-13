import numpy as np
import struct
import numpy as np
import random
import math
import cv2
# x = np.transpose(np.array([[.9,.7,.2,.9],[.9,.7,.2,.9]]))
# y = np.array([[.6,.3,.8,.9,0],[.6,.3,.8,.9,0]])

x = np.transpose(np.array([[.9,.7,.2,.9]]))
y = np.array([[.6,.3,.8,.9,0]])

# # A = small 1 2 3 4 
# x = np.transpose(np.array([1.0,0.8,0.0,0.0]))
# # B = Medium a b c d e 
# y = np.array([0.0,0.5,1.0,0.5,0.0])
# if (U is small (A)) then (V is Medium (B))

try:
    res = np.zeros(x.shape[0]* y.shape[1])
except:
    res = np.zeros(x.shape[0]* y.shape[0])
iz = 0
for row in x:
    for column in y.T:
            mins = np.zeros(np.size(column))
            # check size of 
            for index in range(np.size(column)):
                try:
                    mins[index] = min(row[index],column[index])
                except:
                    mins[index] = min(row,column)
            res[iz] = max(mins)
            iz = iz + 1

try:
    r = np.array([res.reshape(x.shape[0], y.shape[1])])
except:
    r = np.array([res.reshape(x.shape[0], y.shape[0])])

print(r)

# def custom_multiply(x, y):
#     return np.array([min(row, column) for row in x for column in y.T ]).reshape(x.shape[0], y.shape[1])

# def custom_multiply(x, y):
#     print([(row, column) for row in x for column in y.T])

# def _multiply(x, y):
#     return np.array([(min(r,c)) for row in x for column in y.T for r in row for c in column])


# z = _multiply(x,y)



# print(z)



# def Min1and1MinusAplusB(a, b):
#     firstOp = (1 - a) + b
#     return min(1, firstOp)


