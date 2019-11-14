import numpy as np
import struct
import numpy as np
import random
import math
import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

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

usingTriMem = False


fig = plt.figure(0)
ax = plt.axes()
fig.suptitle('Food and Service Membership Functions (POOR, AVERAGE, GOOD)')

# POOR MEMBERSHIP
PMC = 0.1
PMD = 4.1
x = [0,PMC,PMD] 
y = [1,1,0] 
plt.plot(x, y, color='green') 

# MED MEMBERSHIP
MDA = 3.9
MDB = 5
MDC = 6
MDD = 7.9
x = [MDA,MDB,MDC,MDD] 
y = [0,1,1,0] 
if not usingTriMem:
    plt.plot(x, y,color='orange') 

# GOOD MEMBERSHIP
GDA = 5.9
GDB = 9.9

x = [GDA,GDB,10] 
y = [0,1,1] 
plt.plot(x, y,color='blue') 


#TRIANGLE MEMBERSHIP (AVG)
TA = 3.9
TM = 5.5
TB = 7.9
x = [TA,TM,TB] 
y = [0,1,0] 
if usingTriMem:
    plt.plot(x, y,color='orange') 

def poorMem(x):
    c = PMC
    d = PMD
    if x < c:
        return 1
    if x >= c and x <= d:
        return round((d - x)/(d - c),2)
    else:
        return 0


def avgMem(x):
    a = MDA
    b = MDB
    c = MDC
    d = MDD

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
    a = GDA
    b = GDB
    if x > b:
        return 1
    if x >= a and x <= b:
        return (x-a)/(b-a)
    else:
        return 0


def avgMemTri(x):
    a = TA
    m = TM
    b = TB

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
                fig = plt.figure(1)
                ax = plt.axes()
                fig.suptitle('Tipping Problem food={} service={}'.format(qos['food'], qos['service']))
                ax.set_ylabel('Rule Activation')
                ax.set_xlabel('Tip Rating Low=1, Medium=2, high=3')

                if qotIn == 1:
                    x = [.5,1,1.5] 
                    y = [0,1,0] 
                    plt.plot(x, y,color='green' ) 
                    plt.fill_between(x, fuzres[defuzIndex], color='blue', alpha=.25)
                    defuzIndex = defuzIndex + 1
                if qotIn == 2:
                    x = [1.5,2,2.5] 
                    y = [0,1,0] 
                    plt.plot(x, y,color='orange' ) 
                    plt.fill_between(x, fuzres[defuzIndex], color='blue', alpha=.25)
                    defuzIndex = defuzIndex + 1
                if qotIn == 3:
                    x = [2.5,3,3.5] 
                    y = [0,1,0] 
                    plt.plot(x, y,color='blue' ) 
                    plt.fill_between(x, fuzres[defuzIndex], color='blue', alpha=.25)
                    defuzIndex = defuzIndex + 1   

                
                break


if sum(fuzres) == 0:
    print(0)
    fig.suptitle('Tipping Problem food={} service={} RESULT = {} TIP'.format(qos['food'], qos['service'], qos[0]))
else:
    print(defuzSum/sum(fuzres))
    fig.suptitle('Tipping Problem food={} service={} RESULT = {} TIP'.format(qos['food'], qos['service'], qots[int(round(defuzSum/sum(fuzres)) - 1)]))






# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import numpy as np
# fig = plt.figure(1)
# ax = plt.axes()
# x = [1,2,3] 
# y = [0,1,0] 
# plt.plot(x, y ) 
# plt.fill_between(x, .7, color='blue', alpha=.25)

# fig2 = plt.figure(2)
# plt.plot(x, y ) 
# plt.fill_between(x, .7, color='blue', alpha=.25)
plt.show()


# plot each antecedent activation 
# plot each rule activation 
