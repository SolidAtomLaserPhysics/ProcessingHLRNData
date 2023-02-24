import numpy as np
import os
import math
import cmath
import string
import matplotlib.pyplot as plt
import pandas as pd
import re
from mpl_toolkits.mplot3d import Axes3D







'''
Main part 
'''
if __name__ == "__main__":
    sourceDirectory = "/home/hhpnhytt/tests/toCompareKSteps"
    targetDirectory = "/home/hhpnhytt/refined"


    P = [1]
    L = [3]
    Beta = [30.0]
    U = [2.0]
    Ns = [5]
    Ksteps = [100]
    symm = True

    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in Ksteps:
                        for ns in Ns:

                            input = np.genfromtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/fort.1002'.format(beta, u, mu, p, l, steps, ns, symm), delimiter=",")

                            print(len(input))
                            Delta = np.zeros(len(input))
                            for i in len(input):
                                Delta = input[i, 0] + input[i, 2]/(input[i, 1] * input[i, 1] + input[i, 2] * input[i, 2])
                            print(Delta)




    










