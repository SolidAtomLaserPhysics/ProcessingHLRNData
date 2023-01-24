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
    L = [4]
    Beta = [30.0]
    U = [1.1]
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
                    f = open("/home/hhpnhytt/configFiles/testConfigs/b{}_p{}_l{}/config_U{}_mu{}.toml".format(beta, p, l, u, u/2),'w')           #opens the toml file
                    toml.dump(data, f)                                                                              #writes into toml file
                    f.close()



