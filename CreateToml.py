import numpy as np
import os
import toml


#the values yoe want to iterate over
P = [1]
L = [3, 4]
Beta = [30.0, 35.0]
U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
blueprintConfigPath = "/home/hhpnhytt/configFiles/blueprintConfig.toml"
targetPath = "/home/hhpnhytt/configFiles/testConfigs"


if __name__ == "__main__":

    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    startFile = toml.load(blueprintConfigPath)                             #opens and loads the toml file
                    startFile['parameters']['beta'] = beta
                    startFile['parameters']['U'] = u
                    startFile['parameters']['mu'] = u/2
                    startFile['parameters']['p'] = p
                    startFile['parameters']['L'] = l

                    endFile = open(targetPath + "/b{}_p{}_l{}/config_U{}_mu{}.toml".format(beta, p, l, u, u/2),'w+')           #opens the toml file
                    toml.dump(startFile, endFile)                                                                              #writes into toml file
                    endFile.close()



