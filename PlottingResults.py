import numpy as np
import os
import math
import cmath
import string
import matplotlib.pyplot as plt
import pandas as pd
import re
from mpl_toolkits.mplot3d import Axes3D


Beta = [30]
U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
P = [1]
L = [3]




'''
do the plotting of Double Occupancy with matplotlib
'''
def PlotOccupancy(targetDirectory, DataFrame, beta, p, l):
                plt.plot(DataFrame.loc[:, 'U'], DataFrame.loc[:, 'Double Occupancies'], label = r'$\beta = {}, p = {}, L = {}$'.format(beta, p, l), marker = '+')
                plt.xlabel("U")
                plt.ylabel(r'$<n_{i \uparrow} n_{i \downarrow}>$')
                plt.legend()
                plt.savefig(targetDirectory  + "/tests/occupanciesPlot_b{}_p{}_l{}.png".format(beta, p, l))
                plt.clf()







 
'''
Read out Sigma from our file
'''
def readSigma(name):
    dataToRead = np.loadtxt(name)
    MatsubaraFreq = dataToRead[:, 0]
    RealPart = dataToRead[:, 1]
    ImagPart = dataToRead[:, 2]
    return MatsubaraFreq, RealPart, ImagPart



'''
do the plotting of Sigma with matplotlib
'''
def PlotSigma(Matsubara, Imag, name):
    plt.plot(Matsubara[:20], Imag[:20])                             #only plot until Matsubara frequency is the 20s value to see more structure
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'Im($\Sigma$)')
    plt.savefig(name)
    plt.clf()



'''
do the plotting of Sigma(small) values with matplotlib
'''
def PlotFirstSigma(U, Beta):
    FirstImags = np.zeros((len(U)))

    for beta in Beta: 
        for u in range((len(U))):
            Matsubara, Real, Imag = readSigma("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/SigmaValuesU{}Beta{}.txt".format(U[u], beta))
            FirstImags[u] = Imag[0]
        plt.plot(U, FirstImags, label = r'$\beta = {}$'.format(beta), linestyle = 'dashed', marker = '+')   
        for u in range((len(U))):
            Matsubara, Real, Imag = readSigma("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/SigmaValuesU{}Beta{}_Hysterese.txt".format(U[u], beta))
            FirstImags[u] = Imag[0]
        plt.plot(U, FirstImags, label = ' '.join(["Hysterese", r'$\beta = {}$'.format(beta)]), linestyle = 'dashed', marker = '+')                       
    plt.xlabel("U")
    plt.ylabel(r'Im($\Sigma(\omega_0)$)')
    plt.legend()
    plt.savefig("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/SmallImagValues.png")
    plt.clf()

    
'''
Now try to approximate Sigma(0) by Gradient of w_0 and w_1
'''    
def PlotZerosSigma(U, Beta):
    ZeroImags = np.zeros((len(U)))

    for beta in Beta: 
        for u in range((len(U))):
            Matsubara, Real, Imag = readSigma("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/SigmaValuesU{}Beta{}.txt".format(U[u], beta)) 
            Gradient = (Imag[1] - Imag[0])/(Matsubara[1] - Matsubara[0])
            ZeroImags[u] = Imag[0] - Gradient * Matsubara[0]
        plt.plot(U, ZeroImags, label = r'$\beta = {}$'.format(beta), linestyle = 'dashed', marker = '+')
                   
        for u in range((len(U))):
            Matsubara, Real, Imag = readSigma("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/SigmaValuesU{}Beta{}_Hysterese.txt".format(U[u], beta))
            Gradient = (Imag[1] - Imag[0])/(Matsubara[1] - Matsubara[0])
            ZeroImags[u] = Imag[0] - Gradient * Matsubara[0]
        plt.plot(U, ZeroImags, label = ' '.join(["Hysterese", r'$\beta = {}$'.format(beta)]), linestyle = 'dashed', marker = '+')                    
    plt.xlabel("U")
    plt.ylabel(r'Im($\Sigma(0)$)')
    plt.legend()
    plt.savefig("/afs/physnet.uni-hamburg.de/users/th1_km/nhyttrek/Desktop/MA/MACode/dmft_code_not_parallel/BetterFewCalculations/ZeroImagValues.png")
    plt.clf()





'''
Main part 
'''
if __name__ == "__main__":
    sourceDirectory = "/home/hhpnhytt/tests"
    targetDirectory = "/home/hhpnhytt/refined"

    DataFrame = pd.read_csv(sourceDirectory + '/tests/occupancies.csv')                         #load saved Dataframe
    for u in U:
        for beta in Beta:
            for p in P:
                for l in L:
                    smallDataFrame = DataFrame.loc[(DataFrame['L'] == l) & (DataFrame['Beta'] == beta)  & (DataFrame['P'] == p)]            #select only the rows where these conditions hold true, & is and
                    PlotOccupancy(targetDirectory, smallDataFrame, beta, p, l)



                    Matsubara, Real, Imag = readSigma(sourceDirectory + "/b{}_U{}_mu{}_p{}_L{}/self-en_wim".format(beta, u, u/2, p, l))
                    PlotSigma(Matsubara, Imag, targetDirectory + "/tests/b{}_p{}_L{}/ImagSigmaPlot_b{}_U{}_mu{}_p{}_L{}.png".format(beta, p, L, beta, u, u/2, p, l))


    










