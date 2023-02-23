import numpy as np
import os
import toml


#the values yoe want to iterate over
P = [1]
L = [3]
Beta = [30.0]
U = [2.0]                           #starting U, ending U, stepsize
KSteps = [30, 50, 70, 100, 150, 200, 300]
Ns = [5, 6, 7]
symm = False


if __name__ == "__main__":
    sourceDirectory = "/home/hhpnhytt/configFiles"
    wrapperDirectory = "/home/hhpnhytt/lDGAPythonWrapper"

    #os.system("cd" + wrapperDirectory)                                                      #open the Wrapper directory with runscript in it 
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in KSteps:
                        for ns in Ns:
                            os.system("python3 " + wrapperDirectory + "/runscript.py " + sourceDirectory + "/testConfigs/B{}_P{}_L{}_steps{}_Ns{}_symm{}/config_U{}_Mu{}.toml".format(beta, p, l, steps, ns, symm, u, u/2))



