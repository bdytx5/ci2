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

# membership functions (1-10 scale)

def poorMem(x):
    c = 0.1
    d = 4.1
    if x < c:
        return 1
    if x >= c and x <= d:
        return round((d - x)/(d - c),2)
    else:
        return 0


def avgMem(x):
    a = 3.9
    b = 5
    c = 6
    d = 7.9

    if x < a:
        return 0
    if x >= a and x <= b:
        return (x - a)/(b - a)
    if x >= b and x <= c:
        return 1
    if x >= c and x <= d:
        return (d - x)/(d - c)
    else:
        return 0



def goodMem(x):
    a = 5.9
    b = 9.9
    if x > b:
        return 1
    if x >= a and x <= b:
        return (x-a)/(b-a)
    else:
        return 0


def avgMemTri(x):
    a = 3.9
    m = 5.5
    b = 7.9

    if x <= a:
        return 0
    if x > a and x <= m:
        return (x - a)/(m - a)
    if x > m and x < b:
        return (b-x)/(b-m)
    else:
        return 0


R1 = [{'food':goodMem},'or',{'service':goodMem}, {'tip':'high'} ]
R2 = [{'service':avgMemTri}, {'tip':'medium'} ]
R3 = [{'food':poorMem},'and',{'service':poorMem}, {'tip':'low'} ]
Rules = [R1,R2,R3]

qos = {'food':8,'service':7}        

        

fuzres = np.zeros(len(Rules))
resIndex = 0
# defuzzy -- add up each degree of food and service times value, divide by degrees --- low = 1, med = 2, high = 3
for Rs in Rules:
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
            if setMem:
                fuzres[resIndex] = mem
                resIndex = resIndex + 1
            else:
                mem = list(Rs[0].values())[0](qos[list(Rs[0].keys())[0]]) # mouthfull 
                fuzres[resIndex] = mem
                resIndex = resIndex + 1

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
                curmetric = list(curAnt.keys())[0]
                firstmetric = list(firstAnt.keys())[0]

                setMem = True
                if op == 'and':
                    mem = min(curAnt[curmetric](qos[curmetric]),firstAnt[firstmetric](qos[firstmetric]))
                else:
                    mem = max(curAnt[curmetric](qos[curmetric]),firstAnt[firstmetric](qos[firstmetric]))
            else:
                curmetric = list(curAnt.keys())[0]
                if op == 'and':
                    mem = min(mem,curAnt[curmetric](qos[curmetric]))
                else:
                    mem = max(mem,curAnt[curmetric](qos[curmetric]))




# triangular membership functions




        # 1      2        3
qots = ['low','medium','high']
defuzSum = 0
defuzIndex = 0
for r in Rules:
    for val in r:
        if val != 'and' and val != 'or':
            if list(val.keys())[0] == 'tip':
                qotIn = qots.index(val['tip']) + 1
                defuzSum = defuzSum + qotIn*fuzres[defuzIndex]
                defuzIndex = defuzIndex + 1
                break


if sum(fuzres) == 0:
    print(0)
else:
    print(defuzSum/sum(fuzres))





