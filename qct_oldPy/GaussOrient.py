"""
Created on Thu Jun 28 21:30:43 2018
@author: bensy
"""
#A program that generates .gjf files for a h2o dimer so that it is in a proper orientation for a study of repulsion energies.

import os;

#Get current working directory
cwd = str(os.getcwd());

#Create an atom class
class atom:
    def __init__(self, name):
        self.name = name;
        self.coordinates = []
        
    def addCoords(self, coord):
        self.coordinates.append(coord);

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

#Create reference Oxygen atom
theta = 0
phi = 0
O = atom("O");
O.addCoords(0.0); O.addCoords(0.0); O.addCoords(0.11432);

#create reference hydrogen atoms
H1 = atom("H");
H1.addCoords(0.0); H1.addCoords(0.79094); H1.addCoords(-0.45729);
H2 = atom("H");
H2.addCoords(0.0); H2.addCoords(-0.79094); H2.addCoords(-0.45729);

#Ask user for the desired separation.
separation = float(input("Please enter the desired separation: "));

#Generate the coordinates of the second molecule based on the reference and the separation.
F = atom("F");
F.addCoords(0.0); F.addCoords(0.0);
F.addCoords(O.coordinates[2] + separation);  #Note that the translation is only applied along one at the moment axis (here it is the z axis).

H3 = atom("H");
H3.addCoords(0.0); H3.addCoords(0.0); 
H3.addCoords(F.coordinates[2] + 0.92412);

#Ask the user for the number of scan increments and the increment size.
numInc = int(input("Number of scan increments: "));
incSize = float(input("Increment size: "));

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
    
    #Write the coordinates of the first molecule to the file.
    inputFile.write(O.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(O.coordinates[j]));
    inputFile.write("\n" + H1.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(H1.coordinates[j]));
    inputFile.write("\n" + H2.name);
    for j in range (0, 3, 1):
        inputFile.write("  " + str(H2.coordinates[j]));

    #Write the coordinates of the second molecule to the file, each loop will apply another increment.
    inputFile.write("\n" + F.name);
    inputFile.write("0   ");
    inputFile.write("0   ");
    inputFile.write("  " + '%.8f' % (F.coordinates[2]-incSize*i));
    
    inputFile.write("\n" + H3.name);
    inputFile.write("0   ");
    inputFile.write("0   ");
    inputFile.write("  " + '%.8f' % (H3.coordinates[2]-incSize*i));
    
    
    #Write the name of the wfn file to the input file
    inputFile.write("\n\n" + "scan" + str(i) + ".wfn");
    
    #Close the file
    inputFile.close();

#Generate a log file to be used with accompanying script that plots energy deformation against distance.
#This log file contains the separations that will be used in the plot.
logFile = open(cwd + "/Orient" + ".log", 'w+');
for i in range(0, numInc, 1):
    logFile.write(str(separation - i*incSize) + "\n");
logFile.close();