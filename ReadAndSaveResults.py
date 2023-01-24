import numpy as np
import os
import math
import cmath
import matplotlib.pyplot as plt
import pandas as pd
import re
from mpl_toolkits.mplot3d import Axes3D




'''
Now read out the out.dat to get double occupancy
'''
def readOccupancy(name):
    occupancy = 0
    with open(name, 'r') as file:
        for line in file:
            x = line.find("Average Double Occupancy")                       #to find the line, in which douple occupancy is written
            if (x != -1):                                                   #in case we found it in that line
                splittedLine = line.split()
                length = len(splittedLine)
                occupancy = float(splittedLine[length - 1])                       #number is the last string in this line
    return occupancy



'''
Now save double occupancy and its U and Beta in a file
'''
def writeOccupancy(name, beta, U, mu, p, l, occupancy):
    with open(name, 'a') as file:                                           #'a' is useful to append a line to a file instead of substituting it
        file.write("{},{},{},{},{},{}".format(beta, U, mu, p, l, occupancy))
        file.write("\n")                                                    #going to the next line



'''
Read out the Data, which consists of the Sigma in dependence of Matsubara frequency
'''
def readSigma(name):
    dataToRead = np.loadtxt(name)
    MatsubaraFreq = dataToRead[:, 0]
    RealPart = dataToRead[:, 1]
    ImagPart = dataToRead[:, 2]
    return MatsubaraFreq, RealPart, ImagPart


'''
Write Data again in nicer format
'''
def writeSigma(name, MatsubaraFreq, RealPart, ImagPart):
    dataToWrite = np.zeros((len(MatsubaraFreq), 3))
    for i in range(len(MatsubaraFreq)):
        dataToWrite[i] = [MatsubaraFreq[i], RealPart[i], ImagPart[i]]
    np.savetxt(name, dataToWrite)





if __name__ == "__main__":
    directorySource = "/home/hhpnhytt/tests"
    directoryRefined = "/home/hhpnhytt/refined"
    

    P = [1]
    L = [3]
    Beta = [30.0]
    U = [1.1]
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    occupancy = readOccupancy(directorySource + "/b{}_U{}_mu{}_p{}_L{}/ed_dmft/run.out".format(beta, u, u/2, p, l))
                    writeOccupancy(directoryRefined + "/tests/occupancies_b{}_p{}_L{}.txt".format(beta, p, l), beta, u, u/2, p, l, occupancy)
                    Matsubara, Real, Imag = readSigma(directorySource + "/b{}_U{}_mu{}_p{}_L{}/ed_dmft/self-en_vim".format(beta, u, u/2, p, l))
                    writeSigma(directoryRefined + "/tests/SigmaValues_b{}_U{}_mu{}_p{}_L{}.txt".format(beta, u, u/2, p, l))

