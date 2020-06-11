"""
Created on Sun Jul  1 20:17:57 2018

@author: Ben (HF and iterative modifications by Dom)
"""
#A new version of GaussOrient that allows for different orientations of the water dimer -- note this still uses cartesian coordinates in the .gjf files.
#The user specifies the location of the 2nd molecule in the dimer iusing spherical polar coordinates (which are then converted to cartesian).
#The origin of the spherical coordinate system is the oxygen atom in the reference H2O molecule.
#The distance 'r' species the distance from this origin to the oxygen in the 2nd H2O molecule.

#(Also add internal rotaion degrees of freedom).

import os;
import math;
import numpy as np;

#Get current working directory
cwd = str(os.getcwd());

#Create an atom class
class atom:
    def __init__(self, name):
        self.name = name;
        self.coordinates = []
        
    def addCoords(self, coord):
        self.coordinates.append(coord);

#Create a function to convert from spherical polars to cartesians.
def sphereToCart(coord, r, theta, phi):
    theta = theta*math.pi/180
    phi = phi*math.pi/180
    if coord == 0:
        cartCoord = r*math.sin(theta)*math.cos(phi);
    elif coord == 1:
        cartCoord = r*math.sin(theta)*math.sin(phi);
    elif coord == 2:
        cartCoord = r*math.cos(theta);

    return cartCoord;

def fileSuffix(theta, phi):
    if theta < 10:
        thetaStr = '00'+str(int(theta))
    elif theta < 100:
        thetaStr = '0' + str(int(theta))
    else:
        thetaStr = str(int(theta))
        
    if phi < 10: 
        phiStr = '00'+str(int(phi))
    elif phi < 100:
        phiStr = '0'+str(int(phi))
    else:
        phiStr = str(int(phi))
        
    return thetaStr

eqBond = 0.92412

r = float(input("Separation (r): ")) + eqBond/2;
theta_in = float(input("Polar angle initial (theta): "));
theta_fin = float(input("Polar angle final (theta): "));
thetaInc = int(input("Number of theta increments: "));
phi = 0. #float(input("Azimuthal angle (phi): "));


#Ask the user for the number of scan increments and the increment size.
numInc = int(input("Number of scan increments: "));
incSize = float(input("Increment size: "));

for m,theta in enumerate(list(np.linspace(theta_in, theta_fin, thetaInc))):
    
    F1 = atom("F");
    F1.addCoords(0.0); F1.addCoords(0.0); F1.addCoords(+eqBond/2);
    
    #create reference Hydrogen atom
    H1 = atom("H");
    H1.addCoords(0.0); H1.addCoords(0.0); H1.addCoords(-eqBond/2);
    
    #Generate the coordinates of the second molecule based on the reference and input
    F2 = atom("F");
    for i in range(3):
        F2.addCoords(0.0 + sphereToCart(i, r, theta, phi));
    
    H2 = atom("H");
    for i in range(3):
        H2.addCoords(F2.coordinates[i] + sphereToCart(i, eqBond, theta, phi));
          
    #Create the necessary number of .gjf files
    for i in range(0, numInc, 1):
        if i < 10:
            fileNum = "00" + str(i);
        elif i >= 10 and i < 100:
            fileNum = "0" + str(i);
        elif i > 100:
            fileNum = str(i);
        
        #Create the .gjf file
        inputFile = open(cwd + "/scan" + fileSuffix(theta, phi) + "_" + fileNum + '.gjf','w+');
        
        #Write the basic info to the .gjf file
        inputFile.write('%nprocshared=4\n');
        inputFile.write('# freq b3lyp/aug-cc-pvtz out=wfn\n \n');
        inputFile.write('Scan' + str(i) + '\n \n');
        inputFile.write('0 1\n');   #MIGHT NEED TO CHANGE THIS
        
        #Write the coordinates of the first molecule to the file (these do not change).
        inputFile.write(F1.name);
        for j in range (3):
            inputFile.write("  " + '%.8f' % F1.coordinates[j]);
        inputFile.write("\n" + H1.name);
        for j in range (3):
            inputFile.write("  " + '%.8f' % H1.coordinates[j]);
    
        #Write the coordinates of the second molecule to the file, each loop will brign the molecules closer by another increment.
        inputFile.write("\n" + F2.name);
        for j in range(3):
            inputFile.write("  " + '%.8f' % (0.0 + sphereToCart(j, r - incSize*i, theta, phi)));
        inputFile.write("\n" + H2.name);
        for j in range(3):
            inputFile.write("  " + '%.8f' % (0.0 + sphereToCart(j, r - incSize*i, theta, phi) + sphereToCart(j, eqBond, theta, phi)));
    
        #Write the name of the wfn file to the input file
        inputFile.write("\n\n" + "scan" + fileSuffix(theta, phi) + "_" + fileNum + ".wfn");
        
        #Close the file
        inputFile.close();
    
    #Generate a log file to be used with accompanying script that plots energy deformation against distance.
    #This log file contains the separations that will be used in the plot.
#    logFile = open(cwd + "/Orient" + fileSuffix(theta, phi) + ".log", 'w+');
#    for i in range(0, numInc, 1):
#        logFile.write('{:8f}'.format(r - i*incSize) + "_" + "\n");
#    logFile.close();
