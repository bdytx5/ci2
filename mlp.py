import numpy as np
import struct
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import cv2
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


iris = datasets.load_iris()
x = np.ones((150,5))
x[:,:4] = np.array(iris.data[:, :4])
yp = np.array(iris.target)
y = np.zeros((150,3))
for i in range(len(yp)):
    if i < 50:
        y[i][0] = 1
        y[i][1] = 0
        y[i][2] = 0
        continue
    if i < 100:
        y[i][0] = 0
        y[i][1] = 1
        y[i][2] = 0
        continue
    if i < 150:
        y[i][0] = 0
        y[i][1] = 0
        y[i][2] = 1



def tanh2(x, derive=False): # x is the input, derive is do derivative or not
    if derive:
        return (1.0 - x**2)
                           # depends on how you call the function
    return ((eee(x)-eee(-x))/(eee(x)+eee(-x)))



def eee(val):
    return np.exp(val)

def tanh(x, derive=False): 
    if derive: 
        return x * (1.0 - x) 
    return ( 1.0 / (1.0 + np.exp(-x)))

epochs = 1000000
eta = 0.1 # learning rate
B = 0.7
bs = 5

w1 = np.random.normal(0,1,(20, 5))
w2 = np.random.normal(0,1,(3, 21))
bw1 = np.array(np.zeros((151,20,5)))
bw2 = np.array(np.zeros((151,3,21)))

mbw1 = np.array(np.zeros((20,5)))
mbw2 = np.array(np.zeros((3,21)))
bc = 0
actualEpochs = 0
ee = np.zeros(epochs)
for e in range(epochs):
    actualEpochs = e
    for i in range(150):
        
        if bc == bs:
            bc = 0
            w1 = w1 - mbw1
            w2 = w2 - mbw2
            mbw1 = np.array(np.zeros((20,5)))
            mbw2 = np.array(np.zeros((3,21)))
        bc = bc + 1
            
        # layer 1
        v1 = np.dot(x[i, :], np.transpose(w1))
        y1 = tanh(v1)
        # layer 2
        v2 = np.dot(np.append(y1,1), np.transpose(w2))
        y2 = tanh(v2)
        #backprop 
        err = -np.array(y[i, :]-y2)
        errphiprimev2 = err*tanh(y2,derive=True)
        dEdW2 = np.dot(np.transpose(np.array([errphiprimev2])), np.array([np.append(y1,1)])) # e/dw2
        errphiprimev2w2 = np.array(np.dot(np.array(errphiprimev2), w2))[0:(w2.shape[1] - 1)] # exclude bias since its not part of de/dy2
        errphiprimev2w2phiprimev1 = errphiprimev2w2 * tanh(y1, derive=True)
        dEdW1 = np.dot(np.transpose(np.array([errphiprimev2w2phiprimev1])), np.array([x[i, :]]))
        ee[e] = ee[e] + ((1.0/2.0) * ((y[i, :] - y2)**2).mean(axis=0))
        # adjustments
        mbw2 = mbw2 + (bw2[i] + eta*dEdW2)
        mbw1 = mbw1 + (bw1[i]+ eta*dEdW1)
        bw1[i+1] = B*(bw1[i]+ eta*dEdW1)
        bw2[i+1] = B*(bw2[i] + eta*dEdW2)
    print(ee[e])
    if(ee[e] < .2):
        print('total epochs ', e)
        break
 
print('w1----',w1)
print('w2----',w2)



s = 0
conf = np.array(np.zeros((3,3)))
for i in range(150):
        # layer 1
    v1 = np.dot(x[i, :], np.transpose(w1))
    y1 = tanh(v1)
        # layer 2
    v2 = np.dot(np.append(y1,1), np.transpose(w2))
    y2 = tanh(v2)
    act = y[i].argmax()
    pred = y2.argmax()
    if act == pred:
        s = s + 1
    conf[act][pred] = conf[act][pred] + 1

print(s/2000)
print(conf)
for i in range(3):
    print(i,conf[i])
print(actualEpochs)

plt.plot(ee[0:actualEpochs])
plt.ylabel('error')
plt.xlabel('epochs')
plt.show()
        