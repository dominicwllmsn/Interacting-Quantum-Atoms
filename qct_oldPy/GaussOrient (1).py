"""
Created on Sun Jul  1 20:17:57 2018

@author: Ben
"""
#A new version of GaussOrient that allows for different orientations of the water dimer -- note this still uses cartesian coordinates in the .gjf files.
#The user specifies the location of the 2nd molecule in the dimer iusing spherical polar coordinates (which are then converted to cartesian).
#The origin of the spherical coordinate system is the oxygen atom in the reference H2O molecule.
#The distance 'r' species the distance from this origin to the oxygen in the 2nd H2O molecule.

#(Also add internal rotaion degrees of freedom).

import os;
import math;

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
    cartCoord = 0.0;
    if coord == 0:
        cartCoord = r*math.sin(theta)*math.cos(phi);
    elif coord == 1:
        cartCoord = r*math.sin(theta)*math.sin(phi);
    elif coord == 2:
        cartCoord = r*math.cos(theta);

    return cartCoord;
        

#Create reference Oxygen atom
P1 = atom("P");
P1.addCoords(0.0); P1.addCoords(0.0); P1.addCoords(-1.42066);

#create reference hydrogen atoms
H1 = atom("H");
H1.addCoords(0.0); H1.addCoords(0.0); H1.addCoords(0.0);
H2 = atom("H");
H2.addCoords(0.9734658); H2.addCoords(1.034717); H2.addCoords(-1.42066);
H3 = atom("H");
H3.addCoords(0.9734658); H3.addCoords(-1.034717); H3.addCoords(-1.42066);

#Ask the user for the spherical polar coordinates of the 2nd H2O in the dimer.
r = float(input("separation (r): "));
theta = float(input("Polar angle (theta): "));
phi = float(input("Azimuthal angle (phi): "));

#Create reference Oxygen atom
P2 = atom("P");
P2.addCoords(0.0); P2.addCoords(0.0); P2.addCoords(r+1.42066);

#create reference hydrogen atoms
H4 = atom("H");
H4.addCoords(0.0); H4.addCoords(0.0); H4.addCoords(r);
H5 = atom("H");
H5.addCoords(0.9734658); H5.addCoords(-1.034717); H5.addCoords(r+1.42066);
H6 = atom("H");
H6.addCoords(0.9734658); H6.addCoords(1.034717); H6.addCoords(r+1.42066);

#Ask the user for the number of scan increments and the increment size.
numInc = int(input("Number of scan increments: "));
incSize = float(input("Increment size: "));

#Create the necessary number of .gjf files
for i in range(0, numInc, 1):
    
    #Create the .gjf file
    inputFile = open(cwd + "/scan" + str(i) + '.gjf','w+');
    
    #Write the basic info to the .gjf file
    inputFile.write('%nprocshared=4\n');
    inputFile.write('# freq b3lyp/6-31g out=wfn\n \n');
    inputFile.write('Scan' + str(i) + '\n \n');
    inputFile.write('0 1\n');   #MIGHT NEED TO CHANGE THIS
    
    #Write the coordinates of the first molecule to the file (these do not change).
    inputFile.write(P1.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(P1.coordinates[j]));
    inputFile.write("\n" + H1.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(H1.coordinates[j]));
    inputFile.write("\n" + H2.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(H2.coordinates[j]));
    inputFile.write("\n" + H3.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(H3.coordinates[j]));

    #Write the coordinates of the second molecule to the file, each loop will brign the molecules closer by another increment.
    inputFile.write("\n" + P2.name);
    for j in range (0, 2, 1):
        inputFile.write("  " + '%.8f' % P2.coordinates[j]);
    inputFile.write("  " + '%.8f' % (P2.coordinates[2]-incSize*i));
    
    inputFile.write("\n" + H4.name);
    for j in range (0, 2, 1):
        inputFile.write("  " + '%.8f' % H4.coordinates[j]);
    inputFile.write("  " + '%.8f' % (H4.coordinates[2]-incSize*i));
    
    inputFile.write("\n" + H5.name);
    for j in range (0, 2, 1):
        inputFile.write("  " + '%.8f' % H5.coordinates[j]);
    inputFile.write("  " + '%.8f' % (H5.coordinates[2]-incSize*i));
    
    inputFile.write("\n" + H6.name);
    for j in range (0, 2, 1):
        inputFile.write("  " + '%.8f' % H6.coordinates[j]);
    inputFile.write("  " + '%.8f' % (H6.coordinates[2]-incSize*i));
    
    #Write the name of the wfn file to the input file
    inputFile.write("\n\n" + "scan" + str(i) + ".wfn");
    
    #Close the file
    inputFile.close();

#Generate a log file to be used with accompanying script that plots energy deformation against distance.
#This log file contains the separations that will be used in the plot.
#logFile = open(cwd + "/Orient" + ".log", 'w+');
#for i in range(0, numInc, 1):
#    logFile.write(str(r - i*incSize) + "\n");
#logFile.close();