import numpy as np
import os
import toml


#the values yoe want to iterate over
P = [1, 5]
L = [3, 4]
Beta = [30.0, 35.0]
U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]                           #starting U, ending U, stepsize


if __name__ == "__main__":
    sourceDirectory = "/home/hhpnhytt/configFiles"
    wrapperDirectory = "/home/hhpnhytt/lDGAPythonWrapper"

    os.system("cd" + wrapperDirectory)                                                      #open the Wrapper directory with runscript in it 
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:  
                    os.system("python3 " + "runscript.py " + sourceDirectory + "/testConfigs/B{}_P{}_L{}/config_U{}_Mu{}.toml".format(beta, p, l, u, u/2))




