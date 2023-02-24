import numpy as np
import os
import math
import cmath
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D








'''
do the plotting of Double Occupancy with matplotlib reading from a DataFrame which was saved before with ReadAndSaveResults.py
'''
def PlotOccupancy(directoryRefined, Beta, P, L, KSteps, Ns, Symm):
    DataFrame = pd.read_csv(directoryRefined + '/tests/DoubleOccupancies/occupancies_toCompareKsteps.csv')                         #load saved Dataframe
    for beta in Beta:
        for p in P:
            for l in L:
                for steps in KSteps:
                    for ns in Ns:
                        for symm in Symm:
                            smallDataFrame = DataFrame.loc[(DataFrame['L'] == l) & (DataFrame['Beta'] == beta)  & (DataFrame['P'] == p) & 
                                                            (DataFrame['Ksteps'] == steps) & (DataFrame['Ns'] == ns) & (DataFrame['Symmetry'] == symm)]            #select only the rows where the conditions of this iteration hold true, & is and
                            plt.plot(smallDataFrame.loc[:, 'U'], smallDataFrame.loc[:, 'Double Occupancies'], label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = {}$'.format(beta, p, l, steps, ns, symm), marker = '+')
                            plt.xlabel("U")
                            plt.ylabel(r'$<n_{i \uparrow} n_{i \downarrow}>$')
                            plt.legend()
                            plt.savefig(directoryRefined  + "/tests/DoubleOccupancies/occupanciesPlot_B{}_P{}_L{}_steps{}_Ns{}_symm{}.png".format(beta, p, l, steps, ns, symm))
                            plt.clf()






'''
below not used yet
'''


 
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







    










