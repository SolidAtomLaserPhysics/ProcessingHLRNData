import numpy as np
import os
import math
import pandas as pd



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
Now save double occupancy and its U and Beta and so on in a dataframe
'''
def addOccupancy(oldFrame, beta, u, mu, p, l, occupancy):
    newData = {'u': [u], 'mu': [mu], 'Beta': [beta], 'p': [p], 'L': [l], 'double occupancies': [occupancy]}
    outputFrame = pd.DataFrame(data = newData)
    return pd.concat([oldFrame, outputFrame], ignore_index=True)








if __name__ == "__main__":
    directorySource = "/home/hhpnhytt/tests"
    directoryRefined = "/home/hhpnhytt/refined"
    

    P = [1]
    L = [3]
    Beta = [30.0]
    #U = np.arange(1.0, 4.1, 0.2)  
    U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
    categories = {'u': [], 'mu': [], 'Beta': [], 'p': [], 'L': [], 'double occupancies': []}
    Frame = pd.DataFrame(data = categories)
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    #actual reading and writing    
                    occupancy = readOccupancy(directorySource + "/b{}_U{}_mu{}_p{}_L{}/ed_dmft/run.out".format(beta, u, u/2, p, l))
                    Frame = addOccupancy(Frame, beta, u, u/2, p, l, occupancy)
    Frame.to_csv(directoryRefined + "/tests/occupancies.csv", mode = 'w+')

