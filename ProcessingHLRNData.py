import numpy as np
import os
import toml

import ScheduleConfigs as Schedule
import CreateToml as Create
import PlottingResults as Plot
import ReadAndSaveResults as Save


#the values yoe want to iterate over
P = [1]
L = [3]
Beta = [30.0]
U = [2.0]                           
KSteps = [30]
Ns = [5]
Symm = [False]

calculate = False
plotDoubleOccupancy = True 


#all paths needed
blueprintConfigPath = "/home/hhpnhytt/configFiles/blueprintConfig.toml"                     #blueprint config, from which you only change that stuff below
configTargetDirectory = "/home/hhpnhytt/configFiles/testConfigs"                                       #where to put the config files
configSourceDirectory = "/home/hhpnhytt/configFiles/testConfigs"                                        #where we had our config files
wrapperDirectory = "/home/hhpnhytt/lDGAPythonWrapper"
directoryRawDataSource = "/home/hhpnhytt/tests/toCompareKSteps"                            #change for different types of calculations
directoryRefined = "/home/hhpnhytt/refined"



if __name__ == "__main__":

    #if True, the config.toml will be created and scheduled on the HLRN to calculate DMFT
    if calculate:
        Create.CreateConfigs(Beta, P, L, U, KSteps, Ns, Symm, blueprintConfigPath, configTargetDirectory)
        Schedule.ScheduleCalculations(P, L, Beta, U, KSteps, Ns, Symm, configSourceDirectory, wrapperDirectory)

    #if True, the double occupancy will be read from the DMFT reults, saved in a DataFrame and plotted
    if plotDoubleOccupancy:
        Save.saveDoubleOccupancyToUse(Beta, U, P, L, KSteps, Ns, Symm, directoryRawDataSource, directoryRefined)
        Plot.PlotOccupancy(directoryRefined, Beta, P, L, KSteps, Ns, Symm)







