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
def plotOccupancy(directoryRefined, Beta, P, L, KSteps, Ns, Symm):
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
Plot Hybridizationfunction Delta(iv) to look for asymptotic behaviour 
'''
def plotHybridFunc(Beta, P, L, U, KSteps, Ns, Symm, resolutionPoints, sourceDirectory, targetDirectory):
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in KSteps:
                        for ns in Ns:
                            for symm in Symm:
                                input = np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/g0mand'.format(beta, u, u/2, p, l, steps, ns, symm))
                                inputFort = np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/fort.1002'.format(beta, u, u/2, p, l, steps, ns, symm))

                                Delta = np.zeros(len(input))                                #to store the hybridization function in
                                x = np.zeros(len(input))
                                for i in range(len(input)):
                                    Delta[i] = input[i, 0] * (input[i, 0] - input[i, 2])           #calculate Delta by i\nu - 1/G_0(i\nu)
                                    x[i] = input[i, 0]

                                #Calculate Delta with the fort.1002 file, which probably is another one
                                DeltaFort = np.zeros(len(inputFort))
                                xFort = np.zeros(len(inputFort))
                                for i in range(len(inputFort)):
                                    DeltaFort[i] = 1.0 + inputFort[i, 0] * (inputFort[i, 0] + inputFort[i, 2]/(inputFort[i, 1] * inputFort[i, 1] + inputFort[i, 2] * inputFort[i, 2]))           #calculate Delta by i\nu - 1/G_0(i\nu)
                                    xFort[i] = inputFort[i, 0]




                                plt.plot(x[-resolutionPoints:], Delta[-resolutionPoints:], label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = {}$'.format(beta, p, l, steps, ns, symm), marker = '+')
                                plt.xlabel(r'$i\nu$')
                                plt.ylabel(r'$\Delta(i\nu)$')
                                plt.legend()
                                plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotG0mand_B{}_P{}_L{}_steps{}_Ns{}_symm{}.png".format(beta, p, l, steps, ns, symm))
                                plt.clf()

                                plt.plot(xFort[-resolutionPoints:], DeltaFort[-resolutionPoints:], label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = {}$'.format(beta, p, l, steps, ns, symm), marker = '+')
                                plt.xlabel(r'$i\nu$')
                                plt.ylabel(r'$\Delta(i\nu)$')
                                plt.legend()
                                plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotFort1002_B{}_P{}_L{}_steps{}_Ns{}_symm{}.png".format(beta, p, l, steps, ns, symm))
                                plt.clf()

                                plt.plot(x, Delta, label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = {}$'.format(beta, p, l, steps, ns, symm), marker = '+')
                                plt.xlabel(r'$i\nu$')
                                plt.ylabel(r'$\Delta(i\nu)$')
                                plt.legend()
                                plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotFullG0mand_B{}_P{}_L{}_steps{}_Ns{}_symm{}.png".format(beta, p, l, steps, ns, symm))
                                plt.clf()

                                plt.plot(xFort, DeltaFort, label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = {}$'.format(beta, p, l, steps, ns, symm), marker = '+')
                                plt.xlabel(r'$i\nu$')
                                plt.ylabel(r'$\Delta(i\nu)$')
                                plt.legend()
                                plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotFullFort1002_B{}_P{}_L{}_steps{}_Ns{}_symm{}.png".format(beta, p, l, steps, ns, symm))
                                plt.clf()


                                if symm:                        #only have to do it once
                                    #Calculate Delta for True
                                    inputTrue = np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/g0mand'.format(beta, u, u/2, p, l, steps, ns, True))
                                    DeltaTrue = np.zeros(len(inputTrue))                               
                                    x = np.zeros(len(inputTrue))
                                    for i in range(len(inputTrue)):
                                        DeltaTrue[i] = inputTrue[i, 0] * (inputTrue[i, 0] - inputTrue[i, 2])        
                                        x[i] = inputTrue[i, 0]
                                    #now calculate the same for False
                                    inputFalse = np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/g0mand'.format(beta, u, u/2, p, l, steps, ns, False))
                                    DeltaFalse = np.zeros(len(inputFalse))                               
                                    for i in range(len(inputFalse)):
                                        DeltaFalse[i] = inputFalse[i, 0] * (inputFalse[i, 0] - inputFalse[i, 2])        
                                        x[i] = inputFalse[i, 0]
                                    #Therefore can plot the difference of the True and False plot
                                    plt.plot(x, DeltaTrue - DeltaFalse, label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = True - False$'.format(beta, p, l, steps, ns), marker = '+')
                                    plt.xlabel(r'$i\nu$')
                                    plt.ylabel(r'$\Delta(i\nu)$')
                                    plt.legend()
                                    plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotDiffG0mand_B{}_P{}_L{}_steps{}_Ns{}_symmTrue-False.png".format(beta, p, l, steps, ns))
                                    plt.clf()

#
                                '''
                                #now the same for Fort
                                if symm:                        
                                    #Calculate Delta for True
                                    inputFortTrue = np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/fort.1002'.format(beta, u, u/2, p, l, steps, ns, True))
                                    DeltaFortTrue = np.zeros(len(inputFortTrue))                               
                                    xFort = np.zeros(len(inputFortTrue))
                                    for i in range(len(inputFortTrue)):
                                        DeltaFortTrue[i] = 1.0 + inputFortTrue[i, 0] * (inputFortTrue[i, 0] + inputFortTrue[i, 2]/(inputFortTrue[i, 1] * inputFortTrue[i, 1] + inputFortTrue[i, 2] * inputFortTrue[i, 2]))           #calculate Delta by i\nu - 1/G_0(i\nu)
                                        xFort[i] = inputFortTrue[i, 0]
                                    #now calculate the same for False
                                    inputFortFalse= np.loadtxt(sourceDirectory + '/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/fort.1002'.format(beta, u, u/2, p, l, steps, ns, False))
                                    DeltaFortFalse = np.zeros(len(inputFortFalse))                               
                                    xFort = np.zeros(len(inputFortFalse))
                                    for i in range(len(inputFortFalse)):
                                        DeltaFortFalse[i] = 1.0 + inputFortFalse[i, 0] * (inputFortFalse[i, 0] + inputFortFalse[i, 2]/(inputFortFalse[i, 1] * inputFortFalse[i, 1] + inputFortFalse[i, 2] * inputFortFalse[i, 2]))           #calculate Delta by i\nu - 1/G_0(i\nu)
                                        xFort[i] = inputFortFalse[i, 0]
                                    #Therefore can plot the difference of the True and False plot
                                    plt.plot(x, DeltaFortTrue - DeltaFortFalse, label = r'$\beta = {}, p = {}, L = {}, Ksteps = {}, Ns = {}, symmetry = True - False$'.format(beta, p, l, steps, ns), marker = '+')
                                    plt.xlabel(r'$i\nu$')
                                    plt.ylabel(r'$\Delta(i\nu)$')
                                    plt.legend()
                                    plt.savefig(targetDirectory  + "/tests/hybridizationFunctions/hybridPlotDiffFort1002_B{}_P{}_L{}_steps{}_Ns{}_symmTrue-False.png".format(beta, p, l, steps, ns))
                                    plt.clf()
                                '''





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







    










