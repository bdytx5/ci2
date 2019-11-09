import numpy as np
import struct
import numpy as np
import random
import math
import cv2
x = np.transpose(np.array([[.9,.7,.2,.9]]))
y = np.array([[.6,.3,.8,.9,0]])

def custom_multiply(x, y):
    return np.array([min(row, column) for row in x for column in y.T]).reshape(x.shape[0], y.shape[1])


z = custom_multiply(x,y)
print(z)