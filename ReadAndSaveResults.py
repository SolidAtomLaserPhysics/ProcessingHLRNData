import numpy as np
import os
import math
import pandas as pd


'''
This programm, at the moment, extracts and saves the Double Occupancy for many cases(see arrays below) in a pandas DataFrame
'''



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
Now save double occupancy and its U, Beta and so on in a dataframe
'''
def addOccupancy(oldFrame, beta, u, mu, p, l, steps, ns, symm, occupancy):
    newData = {'U': [u], 'Mu': [mu], 'Beta': [beta], 'P': [p], 'L': [l], 'Ksteps': [steps], 'Ns': [ns], 'Symmetry': [symm], 'Double Occupancies': [occupancy]}
    outputFrame = pd.DataFrame(data = newData)
    return pd.concat([oldFrame, outputFrame], ignore_index=True)


'''
Brings together reading and saving the Double Occupancy
'''
def saveDoubleOccupancyToUse(Beta, U, P, L, KSteps, Ns, Symm, directoryRawDataSource, directoryRefined):
    categories = {'U': [], 'Mu': [], 'Beta': [], 'P': [], 'L': [], 'Double Occupancies': []}
    Frame = pd.DataFrame(data = categories)
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in KSteps:
                        for ns in Ns:
                            for symm in Symm:
                                #actual reading and writing    
                                occupancy = readOccupancy(directoryRawDataSource + "/B{}_U{}_Mu{}_P{}_L{}_steps{}_Ns{}_symm{}/ed_dmft/run.out".format(beta, u, u/2, p, l, steps, ns, symm))
                                Frame = addOccupancy(Frame, beta, u, u/2, p, l, occupancy)
    Frame.to_csv(directoryRefined + "/tests/occupancies_toCompareKsteps.csv", mode = 'w+')    



