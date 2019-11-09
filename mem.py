import numpy as np
import struct
import numpy as np
import random
import math
import cv2

# need to create a membership function for the iris dataset 


# special case of membership function (R-function)
def smallAMem(x):
    c = 1.8
    d = 3
    if x < c:
        return 1
    if x > c and x < d:
        return (d - x)/(d - c)
    else:
        return 0

# membership function
def medAMem(x):
    a = 1
    b = 2.5
    c = 3
    d = 4

    if x < a:
        return 0
    if x >= a and x <= b:
        return (x - a)/(b - a)
    if x > b and x < c:
        return 1
    if x > c and x <= d:
        return (d - x)/(d - c)
    else:
        return 0

# special case of membership function (L-function)
def largeAMem(x):

    a = 2.9
    b = 4

    if x >= b:
        return 1
    if x >= a and x < b:
        return (x-a)/(b-a)
    else:
        return 0




