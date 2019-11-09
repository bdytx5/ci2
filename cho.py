import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm


# lets make our Choquet integral class
class ChoquetIntegral:

    def __init__(self):
        """
            init function
        """
        
        self.N = 0    
        self.fm = []  
        self.g = []   
        
    def evaluate(self, x):
        """
            evaluate the Choquet integral
        """

        print("Input:",x)
                
        # do our sort
        pi_i = np.argsort(x)[::-1] + 1
        
        print("Sort:",pi_i)
        
        # do the first calculation 
        h = x[pi_i[0] - 1]
        idk = pi_i[:1]
        g = self.fm[ str(pi_i[:1]) ]
        o = h * g
        print("[h,g-0,res] Step 1 :",h,g,0,h*g)
        print(str(pi_i[:1]))
        
        # do the other N-1 terms
        for i in range(1, self.N):
            h = x[pi_i[i] - 1]            
            g1 = self.fm[str(np.sort(pi_i[:i]))]
            g2 = self.fm[str(np.sort(pi_i[:i + 1]))]
            print("[h,g2-g1,res] Step",i+1,":",h,g2,g1,h*(g2-g1))
            print(str(np.sort(pi_i[:i])))
            print(str(np.sort(pi_i[:i + 1])))
            # our calculation, namely, max of the mins
            o = o + ( h * (g2 - g1) )
            
        return o

    def get_keys_index(self):
        """
            sets up a dictionary for referencing the FM
            :return: keys to the dictionary
        """

        vls = np.arange(1, self.N + 1)
        count = 0
        Lattice = {}
        for i in range(0, self.N):
            Lattice[str(np.array([vls[i]]))] = count
            count = count + 1
        for i in range(2, self.N + 1):
            A = np.array(list(itertools.combinations(vls, i)))
            for latt_pt in A:
                Lattice[str(latt_pt)] = count
                count = count + 1
        return Lattice    
    
    def produce_lattice(self):
        """
            makes a nice little ole data structure for us to index our fuzzy measure 
        """

        index_keys = self.get_keys_index()
        Lattice = {}
        for key in index_keys.keys():
            Lattice[key] = self.g[index_keys[key]]
        return Lattice
    


# create our integral
chi = ChoquetIntegral()

# lets go with 4 inputs in our example
chi.N = 4

# fuzzy measure
#fm = [ x1 x2 x3 x4 x12 x13 x14 x23 x24 x34 x123 x124 x134 x234 x1234 ]
#fm = np.asarray( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1 ] ) # min
#fm = np.asarray( [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1 ] ) # max
fm = np.asarray( [ 1/4, 1/4, 1/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 3/4, 3/4, 3/4, 3/4, 1 ] ) # mean
chi.g = fm

# convert it into a data structure that is a little nicer to work with
chi.fm = chi.produce_lattice()
print("############################################")
print("Here is the fuzzy measure")
print("############################################")
print(chi.fm)

# do for one sample
print("############################################")
print("Here is evaluation of the fuzzy integral")
print("############################################")
print( chi.evaluate(np.asarray([0.25,0.5,0.75,0.5])) )

