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
blueprintConfigPath = "/home/hhpnhytt/configFiles/blueprintConfig.toml"                     #blueprint config, from which you only change that stuff below
targetDirectory = "/home/hhpnhytt/configFiles/testConfigs"                                       #where to put the config files
symm = True

if __name__ == "__main__":

    for beta in Beta:
        for p in P:
            for l in L:
                for u in U:
                    for steps in KSteps:
                        for ns in Ns:
                            if not os.path.exists(targetDirectory + "/B{}_P{}_L{}_steps{}_Ns{}_symm{}/".format(beta, p, l, steps, ns, symm)):                                  #make directory if not exists already
                                os.makedirs(targetDirectory + "/B{}_P{}_L{}_steps{}_Ns{}_symm{}/".format(beta, p, l, steps, ns, symm))
                            startFile = toml.load(blueprintConfigPath)                             #opens and loads the toml file
                    

                            #lines you want to change in the config.toml
                            startFile['parameters']['beta'] = beta
                            startFile['parameters']['U'] = u
                            startFile['parameters']['mu'] = u/2
                            startFile['parameters']['p'] = p
                            startFile['parameters']['L'] = l
                            startFile['parameters']['Ksteps'] = steps
                            startFile['parameters']['Ns'] = ns
                            startFile['parameters']['Symm'] = symm
                        
                            #lines we have to add as well to fit what the Wrapper wants
                            startFile['ED']['ksteps'] = steps
                            startFile['ED']['ns'] = ns
                            startFile['ED']['symm'] = symm

                            endFile = open(targetDirectory + "/B{}_P{}_L{}_steps{}_Ns{}_symm{}/config_U{}_Mu{}.toml".format(beta, p, l, steps, ns, symm, u, u/2),'w+')           #opens the toml file
                            toml.dump(startFile, endFile)        #writes into toml file
                            endFile.close()



