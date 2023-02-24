import numpy as np
import os
import toml






def ScheduleCalculations(P, L, Beta, U, KSteps, Ns, Symm, configSourceDirectory, wrapperDirectory):


    #os.system("cd" + wrapperDirectory)                                                      #open the Wrapper directory with runscript in it 
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in KSteps:
                        for ns in Ns:
                            for symm in Symm:
                                os.system("python3 " + wrapperDirectory + "/runscript.py " + configSourceDirectory + "/B{}_P{}_L{}_steps{}_Ns{}_symm{}/config_U{}_Mu{}.toml".format(beta, p, l, steps, ns, symm, u, u/2))




