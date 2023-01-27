import numpy as np
import os
import toml


#the values yoe want to iterate over
P = [1, 5]
L = [3, 4]
Beta = [30.0, 35.0]
U = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]                           #starting U, ending U, stepsize
blueprintConfigPath = "/home/hhpnhytt/configFiles/blueprintConfig.toml"                     #blueprint config, from which you only change that stuff below
targetDirectory = "/home/hhpnhytt/configFiles/testConfigs"                                       #where to put the config files


if __name__ == "__main__":

    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    if not os.path.exists(targetDirectory + "/B{}_P{}_L{}/".format(beta, p, l)):                                  #make directory if not exists already
                        os.makedirs(targetDirectory + "/B{}_P{}_L{}/".format(beta, p, l))
                    startFile = toml.load(blueprintConfigPath)                             #opens and loads the toml file
                    
                    #lines you want to change in the config.toml
                    startFile['parameters']['beta'] = beta
                    startFile['parameters']['U'] = u
                    startFile['parameters']['mu'] = u/2
                    startFile['parameters']['p'] = p
                    startFile['parameters']['L'] = l


                    endFile = open(targetDirectory + "/B{}_P{}_L{}/config_U{}_Mu{}.toml".format(beta, p, l, u, u/2),'w+')           #opens the toml file
                    toml.dump(startFile, endFile)                                                                              #writes into toml file
                    endFile.close()



