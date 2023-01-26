import numpy as np
import os
import toml


#the values yoe want to iterate over
P = [1]
L = [3, 4]
Beta = [30.0, 35.0]
U = range(1.0, 4.0, 0.2)                                                                    #starting U, ending U, stepsize
blueprintConfigPath = "/home/hhpnhytt/configFiles/blueprintConfig.toml"                     #blueprint config, from which you only change that stuff below
targetPath = "/home/hhpnhytt/configFiles/testConfigs"                                       #where to put the config files


if __name__ == "__main__":

    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    startFile = toml.load(blueprintConfigPath)                             #opens and loads the toml file
                    
                    #lines you want to change in the config.toml
                    startFile['parameters']['beta'] = beta
                    startFile['parameters']['U'] = u
                    startFile['parameters']['mu'] = u/2
                    startFile['parameters']['p'] = p
                    startFile['parameters']['L'] = l

                    endFile = open(targetPath + "/b{}_p{}_l{}/config_U{}_mu{}.toml".format(beta, p, l, u, u/2),'w+')           #opens the toml file
                    toml.dump(startFile, endFile)                                                                              #writes into toml file
                    endFile.close()



