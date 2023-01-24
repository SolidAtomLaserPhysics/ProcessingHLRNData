import numpy as np
import os
import math
import cmath
import matplotlib.pyplot as plt
import pandas as pd
import re
from mpl_toolkits.mplot3d import Axes3D
import toml




if __name__ == "__main__":






    P = [1]
    L = [3, 4]
    Beta = [30.0, 35.0]
    U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    file = toml.load("/home/hhpnhytt/configFiles/blueprintConfig.toml")                             #opens and loads the toml file
                    file['parameters']['beta'] = beta
                    file['parameters']['U'] = u
                    file['parameters']['mu'] = u/2
                    file['parameters']['p'] = p
                    file['parameters']['L'] = l
                    f = open("/home/hhpnhytt/configFiles/testConfigs/b{}_p{}_l{}/config_U{}_mu{}.toml".format(beta, p, l, u, u/2),'w+')           #opens the toml file
                    toml.dump(file, f)                                                                              #writes into toml file
                    f.close()



