# need to make some rules 
# if petal length is low (<2) then setosa 
# if petal length is med (3-5) and petal width is med (3-5) versicolor 
# if petal length is large (>5) and petal width is large (>5) virginica 


# membership functions 

# membership function

# fig = plt.figure(0)
# ax = plt.axes()
# ax.set_xlabel('Pedal Length')
# ax.set_ylabel('Rule activation')


lowPla = 0
lowPlb = 1
lowPlc = 1.9
lowPld = 2.2

# x = [lowPla,lowPlb,lowPlc,lowPld] 
# y = [0,1,1,0] 
# if not usingTriMem:
#     plt.plot(x, y,color='orange') 

def lowPl(x):
    a = 0
    b = 1
    c = 1.9
    d = 2.2

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

medPla = 2
medPlb = 3.9
medPlc = 4.1
medPld = 6


def medPl(x):
    a = 2
    b = 3.9
    c = 4.1
    d = 6

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



lrgPla = 4
lrgPlb = 5.5
lrgPlc = 5.9
lrgPld = 7


def lrgPl(x):
    a = 4
    b = 5.5
    c = 5.9
    d = 7

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




medPwa = 0.8 
medPwb = 1.3 
medPwc = 1.5 
medPwd = 2 


def medPw(x):
    a = 0.8
    b = 1.3
    c = 1.5
    d = 2

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


lrgPwa = 1
lrgPwb = 1.8
lrgPwc = 2
lrgPwd = 3



def lrgPw(x):
    a = 1
    b = 1.8
    c = 2.0
    d = 3

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



# evaluate 


# classifying... 


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :4] 
y = iris.target 

sl = X[:, :1]
sw = X[:, 1:2]


pl = X[:, 2:3]
pw = X[:, 3:4]

print('setosa pl min-', min(pl[0:50]), 'max-',max(pl[0:50]) )
print('versi pl min-', min(pl[50:100]), 'max-',max(pl[50:100]) )
print('vir pl min-',min(pl[100:150]),  'max-', max(pl[100:150]))
print('versi pw min-', min(pw[50:100]), 'max-',max(pw[50:100]) )
print('vir pw min-',min(pw[100:150]),  'max-', max(pw[100:150]))


# need to be able to feed the entire dataset in
# rule structure = [sl,sw,pl,pw]
 

# flowers = [[5.1,1.3,3.5,1.3]]
flowers = X
# if petal length is low (<2) then setosa 
# if petal length is med (3-5) and petal width is med (3-5) versicolor 
# if petal length is large (>5) and petal width is large (>5) virginica 


R1 = [{'pl':lowPl}, {'flower':'setosa'}]
R2 = [{'pl':medPl},'and',{'pw':medPw}, {'flower':'versicolor'}]
R3 = [{'pl':lrgPl},'and',{'pw':lrgPw}, {'flower':'virginica'}]

rules = [R1,R2,R3]
findex = 0
finalResults = np.zeros(len(flowers))
# rules = [R]
for f in flowers:
    findex = findex + 1
    qos = {'pl':f[2], 'pw':f[3],'sl':f[0],'sw':f[1]}
    fuzres = np.zeros(len(rules))
    resIndex = 0
    
    for Rs in rules:
        firstAnt = {}
        mem = 0.0
        op = '' 
        setMem = False


        for i in range(len(Rs)):
            if Rs[i] == 'and' or Rs[i] == 'or':
                op = Rs[i]
                continue
        
            if list(Rs[i].keys())[0] == 'flower':
                # compute result 
                if setMem:
                    fuzres[resIndex] = mem
                    resIndex = resIndex + 1
                else:
                    metric = list(Rs[0].keys())[0]
                    mem = list(Rs[0].values())[0](qos[metric]) # mouthfull 
                    fuzres[resIndex] = mem
                    resIndex = resIndex + 1
                break


            if not firstAnt: 
                firstAnt = Rs[i]
            else:
                curAnt = Rs[i]
            
                if not setMem: 
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
                    # 1      2        3
    qots = ['setosa','versicolor','virginica']
    defuzSum = 0
    defuzIndex = 0
    for r in rules:
        for val in r:
            if val != 'and' and val != 'or':
                if list(val.keys())[0] == 'flower':
                    qotIn = qots.index(val['flower']) + 1
                    defuzSum = defuzSum + qotIn*fuzres[defuzIndex]
                    defuzIndex = defuzIndex + 1
                    break


    if sum(fuzres) == 0:
        print(0)
        finalResults[findex-1] = 0
    else:
        print(defuzSum/sum(fuzres),  '--',findex)
        finalResults[findex-1] = defuzSum/sum(fuzres)



errors = 0
for i in range(len(finalResults)):
    preRound = finalResults[i]
    res = round(finalResults[i],0)
    if i < 50:
        errors = errors + 1 if res != 1 else errors
        continue
    if i < 100:
        errors = errors + 1 if res != 2.0 else errors
        continue
    if i < 150:
        errors = errors + 1 if res != 3.0 else errors


print((len(finalResults)-errors)/len(finalResults))


