import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm

# what is our input?
N = 4 # N inputs
h = np.asarray( [0.5, 0.4, 0.9, 0.1] ) # four inputs, where h(x1) = 0.5, h(x2) = 0.2, ...

# what are our weights in the OWA?
w = np.asarray( [1/4, 1/4, 1/4, 1/4] ) # four weights that add up to one!

# step one in the OWA, sort!
hsort = np.sort( h )[::-1] # put in descending order
print( "Sorted input: ", hsort )

# calculate the OWA!!! (yes, that simple)
y = np.sum(np.multiply(hsort,w))
print( "Result is: ", y )

##################################
## modify this ################### 
##################################

# w = np.asarray( ... 

# ##################################
# ##################################

# hsort = np.sort( h )[::-1] 
# y = np.sum(np.multiply(hsort,w))
# print( "Result is: ", y )


# ##################################
# ## modify this ################### 
# ##################################

# w = np.asarray( ... 

# ##################################
# ##################################

# hsort = np.sort( h )[::-1] 
# y = np.sum(np.multiply(hsort,w))
# print( "Result is: ", y )