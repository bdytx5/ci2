import numpy as np
import struct
import numpy as np
import random
import math
import cv2


def LukaOp(a, b):
    firstOp = (1 - a) + b
    return min(1, firstOp)

def CorrProduct(a, b):
    return a*b

def CorrMin(a, b):
    return min(a, b)

# A = small 1 2 3 4 
A = np.array([1.0,0.8,0.0,0.0])
# B = Medium   a   b   c   d   e 
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
        v = LukaOp(a,b)
        R[x,y] = v

res = np.zeros(R.shape[1])
Ap = np.array([1.0,0.8,0.0,0.0])
for x in range(R.shape[1]):
    preMax = np.zeros(np.size(Ap))
    for y in range(np.size(Ap)):
        preMax[y] = min(Ap[y],R[y,x])
    res[x] = max(preMax)

print(res)




# need to do the tipping problem !
# IF the service was good or the food quality was good, THEN the tip will be high.
# IF the service was average, THEN the tip will be medium.
# IF the service was poor and the food quality was poor THEN the tip will be low.



def medAMem(x):
    a = 1
    b = 2.5
    c = 3
    d = 4

    if x < a:
        return 0
    if x >= a and x <= b:
        return (x - a)/(b - a)
    if x > b and x <= c:
        return 1
    if x > c and x <= d:
        return (d - x)/(d - c)
    else:
        return 0

def chopTipMem(m):
    a = 1
    b = 2.5
    c = 3
    d = 4

    if x < a:
        return 0
    if x >= a and x <= b:
        return d + m*(b-a)
    if x > b and x <= c:
        return 1
    if x > c and x <= d:
        return d + m*(d-c)
    else:
        return 0

Rs = [{'food':medAMem},'and',{'service':medAMem}, {'tip':medAMem} ]

# defuzzy -- add up each degree of food and service times value, divide by degrees --- low = 1, med = 2, high = 3
firstAnt = {}
mem = 0.0
op = '' 
setMem = False
for i in range(len(Rs)):
    try:
        if Rs[i] == 'and' or Rs[i] == 'or':
            op = Rs[i]
            continue
    except:
        print('err')
        continue

    if list(Rs[i].keys())[0] == 'tip':
        # compute result 
        res = chopTipMem(mem)
        print(res)
        break


    if not firstAnt: 
        firstAnt = Rs[i]
        try:
            if Rs[i+1] == 'and' or Rs[i+1] == 'or':
                firstAnt['op'] = Rs[i+1]
        except:
            print('err')
            continue
    else:
        curAnt = Rs[i]
        if not setMem: # 
            setMem = True
            if op == 'and':
                mem = min(curAnt[list(curAnt.keys())[0]](2.7),firstAnt[list(firstAnt.keys())[0]](2.7))
            else:
                mem = max(curAnt[list(curAnt.keys())[0]](2.7),firstAnt[list(firstAnt.keys())[0]](2.7))
        else:
            if op == 'and':
                mem = min(mem,curAnt[list(curAnt.keys())[0]](3.5))
            else:
                mem = max(mem,curAnt[list(curAnt.keys())[0]](3.5))


