#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:22:50 2018

@author: dominicwilliamson
"""

import os
import fileinput

cwd = str(os.getcwd());

noSteps = int(input("Number of scan steps: "))
thetaIn = int(input("Initial angle: "))
thetaFin = int(input("Final angle: "))
thetaSteps = int(input("Angle separation: "))

for i in range(noSteps):
    for theta in range(thetaIn,thetaFin+1,thetaSteps):
        if theta < 10:
            angleStr = "00"+str(theta)
        elif 10 < theta < 100:
            angleStr = "0"+str(theta)
        else:
            angleStr = str(theta)
            
        try:
            wfnPath = cwd + "/scan" + angleStr + \
                           "_10" + ".wfn"
            finput = fileinput.input(wfnPath, inplace=True)
            for line in finput:
                if line.startswith("GAUSSIAN"):
                    line = line.replace("NUCLEI","NUCLEI  B3LYP\n")
                    print(line)
                else:
                    print(line)
            finput.close()
            
        except IOError:
            print("Can't find .wfn file")