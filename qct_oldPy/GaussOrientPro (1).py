"""
Created on Tue Jul  3 13:52:50 2018
@author: bensy
"""
#The final (hopefully) version of GaussOrient that allows the user to choose which molecule to orient.
import os;
import math;
import numpy as np;
import copy

#Get current working directory
cwd = str(os.getcwd());

#Create an atom class
class atom:
    def __init__(self, name):
        self.name = name;
        self.coordinates = []
        
    def addCoords(self, coord):
        self.coordinates.append(coord);

#Create a molecule class
class molecule:
    def __init__(self, name):
        self.name = name;
        self.atoms = []

    def addAtom(self, atom):
        self.atoms.append(atom);

#Create a function to convert from spherical polars to cartesians.
def sphereToCart(coord, r, theta, phi):
    theta = (theta*math.pi)/180;
    phi = (phi*math.pi)/180;
    cartCoord = 0.0;
    if coord == 0:
        cartCoord = r*math.sin(theta)*math.cos(phi);
    elif coord == 1:
        cartCoord = r*math.sin(theta)*math.sin(phi);
    elif coord == 2:
        cartCoord = r*math.cos(theta);

    return cartCoord;
 
#Create a function that generates a file suffix for a given theta/phi       
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
        
    return thetaStr+phiStr

#Ask the user which molecule they would like to use.
moleculeChoice = raw_input("Enter molecule: ");
moleculeChoice.lower();

#Ask the user for the spherical polar coordinates of the 2nd NH3 in the dimer and the scan details
r = float(input("separation (r): "));
numInc = int(input("Number of scan increments: "));
incSize = float(input("Increment size: "));
theta_in = float(input("Initial polar angle (theta): "));
theta_fin = float(input("Final polar angle (theta): "));
thetaInc = int(input("Number of theta increments: "));
phi_in = float(input("Initial azimuthal angle (phi): "));
phi_fin = float(input("Final azimuthal angle (phi): "));
phiInc = int(input("Number of phi increments: "));

#Create an instance of the molecule class.
refMolecule = molecule(moleculeChoice);
#Open GaussOrient.txt and use the user's molecule choice to extract the reference coordinates for the correct molecule.
refFile = open(cwd + "/GaussOrient.txt", 'r');
for line in refFile:
    line.strip('/n');
    #Find the correct block in the text file.
    if line.startswith(moleculeChoice):
        for line in refFile:
            tempData = line.split();
            #If the line is blank --> at the end of the block of info --> break out of loop.
            if len(tempData) == 0:
                break;
            #Create an atom based on the info on the current line.
            tempAtom = atom(tempData[0]);
            for i in range (1, 4, 1):
                tempAtom.addCoords(float(tempData[i]));
            #Add the atom to the molecule.
            refMolecule.addAtom(tempAtom);
        break;

#We now have a reference molecule meaning we can now generate the 2nd molecule in the dimer.
#First set the scan molecule equal to the reference molecule.
scanMolecule = copy.deepcopy(refMolecule);

#Iterate through increments of theta and phi.
for m,theta in enumerate(list(np.linspace(theta_in, theta_fin, thetaInc))):
    
    for n,phi in enumerate(list(np.linspace(phi_in, phi_fin, phiInc))):

        os.makedirs("scan" + fileSuffix(theta, phi));

        #Shift the scan molecule to the correct starting position as specified by the user.
        #First deal with the 'primary' atom i.e. O, N, F etc.
        for j in range(0, 3, 1):
            scanMolecule.atoms[0].coordinates[j] += sphereToCart(j, r, theta, phi);
        
        
        #Then deal with all the hydrogens.
        for i in range(1, len(scanMolecule.atoms), 1):
            scanAtom = scanMolecule.atoms[0];
            tempAtom = scanMolecule.atoms[i];
            tempRefAtom = refMolecule.atoms[i];
            for j in range(0, 2, 1):
                tempAtom.coordinates[j] = scanAtom.coordinates[j] + tempRefAtom.coordinates[j];
            tempAtom.coordinates[2] = scanAtom.coordinates[2] + abs(tempRefAtom.coordinates[2]);
            scanMolecule.atoms[i] = tempAtom;

        #Create the necessary number of .gjf files
        for i in range(0, numInc, 1):
            
            #Generate the number part of the gjf filename
            if i < 10:
              fileNum  = "00" + str(i);
            elif i >= 10 and i < 100:
              fileNum = "0" + str(i);
            elif i > 100:
              fileNum = str(i);
            
            #Create the .gjf file
            inputFile = open(cwd + "/scan" + fileSuffix(theta, phi) + "/scan" + fileNum + '.gjf','w+');
            
            #Write the basic info to the .gjf file
            inputFile.write('%nprocshared=4\n');
            inputFile.write('# b3lyp/aug-cc-pvtz out=wfn\n \n');
            inputFile.write('Scan' + fileNum + '\n \n');
            inputFile.write('0 1');
            
            #Write the coordinates of the first molecule to the file (these do not change).
            for j in range(0, len(refMolecule.atoms), 1):
                tempAtom = refMolecule.atoms[j];
                inputFile.write("\n" + tempAtom.name);
                for k in range(0, 3, 1):
                    inputFile.write("  " + str(tempAtom.coordinates[k]));

        
            #Write the coordinates of the second molecule to the file, each loop will brign the molecules closer by another increment.
            #Once again deal with the 'primary' atom first.
            tempRefAtom = refMolecule.atoms[0];
            inputFile.write("\n" + scanMolecule.atoms[0].name);
            for j in range(0, 3, 1):
                inputFile.write("  " + str(tempRefAtom.coordinates[j] + sphereToCart(j, r - incSize*i, theta, phi))[:6]);
            
            for j in range(1, len(scanMolecule.atoms), 1):
                inputFile.write("\n" + scanMolecule.atoms[j].name);
                for k in range(0, 2, 1):
                    inputFile.write("  " + str(tempRefAtom.coordinates[k] + sphereToCart(k, r - incSize*i, theta, phi) + refMolecule.atoms[j].coordinates[k])[:6]);
                inputFile.write("  " + str(tempRefAtom.coordinates[2] + sphereToCart(2, r - incSize*i, theta, phi) + abs(refMolecule.atoms[j].coordinates[2]))[:6]);
            
            #Write the name of the wfn file to the input file
            inputFile.write("\n\n" + "scan" + fileNum + ".wfn");
            
            #Close the file
            inputFile.close();

        #Generate a log file to be used with accompanying script that plots energy deformation against distance.
        #This log file contains the separations that will be used in the plot.
        logFile = open(cwd + "/scan" + fileSuffix(theta, phi) + "/Orient" + ".log", 'w+');
        for i in range(0, numInc, 1):
            logFile.write(str(r - i*incSize) + "\n");
        logFile.close();