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
        
    if abs(cartCoord) < 0.0001:
        cartCoord = 0.0;

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
r = 4.65
numInc = 26
incSize = 0.124
alpha = 120.*math.pi/180
gamma = 0.*math.pi/180

phi_in = 0.
phi_fin = 0.
phiInc = 1
theta_in = 0*math.pi/180
theta_fin = 180*math.pi/180
thetaInc = 5
beta=0

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
        
#Transform the reference molecule so that the primary atom is at the origin of the coordinate system.
transformation = [];
for i in range(0, 3, 1):
    transformation.append(-refMolecule.atoms[0].coordinates[i]);
    
for i in range(0, len(refMolecule.atoms), 1):
    for j in range(0, 3, 1):
        refMolecule.atoms[i].coordinates[j] = refMolecule.atoms[i].coordinates[j] + transformation[j];

#We now have a reference molecule meaning we can now generate the 2nd molecule in the dimer.
#First set the scan molecule equal to the reference molecule.
scanMolecule = copy.deepcopy(refMolecule);

#Iterate through increments of theta and phi.
for m,theta in enumerate(list(np.linspace(theta_in, theta_fin, thetaInc))):
    
    for n,phi in enumerate(list(np.linspace(phi_in, phi_fin, phiInc))):
    
        #Shift the scan molecule to the correct starting position as specified by the user.
        #First deal with the 'primary' atom i.e. O, N, F etc.
        for j in range(0, 3, 1):
            scanMolecule.atoms[0].coordinates[j] = refMolecule.atoms[0].coordinates[j] + sphereToCart(j, r, theta, phi);
        
        #Now position the hydrogens
        for i in range(1, len(scanMolecule.atoms), 1):
            for j in range(0, 3, 1):
                scanMolecule.atoms[i].coordinates[j] = scanMolecule.atoms[0].coordinates[j] + refMolecule.atoms[i].coordinates[j];

        os.makedirs("scan" + fileSuffix(theta, phi));

        #Deal with rotational degrees of freedom.
        #Need to boost molecule to origin of coordinate system in order to do rotations.
        boost = [];
        for i in range(0, 3, 1):
            boost.append(-scanMolecule.atoms[0].coordinates[i]);
        #perform translation.
        for i in range(0, len(scanMolecule.atoms), 1):
            for j in range(0, 3, 1):
                scanMolecule.atoms[i].coordinates[j] = scanMolecule.atoms[i].coordinates[j] + boost[j];
        
        if alpha != 0:
            #Rotate the hydrogens about the z axis.
            for i in range(1, len(scanMolecule.atoms), 1):
                tempXCoord = scanMolecule.atoms[i].coordinates[0]; tempYCoord = scanMolecule.atoms[i].coordinates[1];
                newXCoord = math.cos(alpha)*tempXCoord - math.sin(alpha)*tempYCoord;
                newYCoord = math.sin(alpha)*tempXCoord + math.cos(alpha)*tempYCoord;
                if abs(newXCoord) < 0.001: newXCoord = 0;
                if abs(newYCoord) < 0.001: newYCoord = 0;
                scanMolecule.atoms[i].coordinates[0] = newXCoord; scanMolecule.atoms[i].coordinates[1] = newYCoord;
                
        if beta != 0:
            #perform rotation about 'new' x axis.
            for i in range(1, len(scanMolecule.atoms), 1):
                tempYCoord = scanMolecule.atoms[i].coordinates[1]; tempZCoord = scanMolecule.atoms[i].coordinates[2];
                newYCoord = math.cos(beta)*tempYCoord - math.sin(beta)*tempZCoord;
                newZCoord = math.sin(beta)*tempYCoord + math.cos(beta)*tempZCoord;
                if abs(newYCoord) < 0.001: newYCoord = 0;
                if abs(newZCoord) < 0.001: newZCoord = 0;
                scanMolecule.atoms[i].coordinates[1] = newYCoord; scanMolecule.atoms[i].coordinates[2] = newZCoord;

        if gamma != 0:
            #Rotate the hydrogens about the 'new' z axis
            for i in range(1, len(scanMolecule.atoms), 1):
                tempXCoord = scanMolecule.atoms[i].coordinates[0]; tempYCoord = scanMolecule.atoms[i].coordinates[1];
                newXCoord = math.cos(gamma)*tempXCoord - math.sin(gamma)*tempYCoord;
                newYCoord = math.sin(gamma)*tempXCoord + math.cos(gamma)*tempYCoord;
                if abs(newXCoord) < 0.001: newXCoord = 0;
                if abs(newYCoord) < 0.001: newYCoord = 0;
                scanMolecule.atoms[i].coordinates[0] = newXCoord; scanMolecule.atoms[i].coordinates[1] = newYCoord;
                
        #transform back to it's previous spatial position now that it has been rotated.
        for i in range(0, len(scanMolecule.atoms), 1):
            for j in range(0, 3, 1):
                scanMolecule.atoms[i].coordinates[j] = scanMolecule.atoms[i].coordinates[j] - boost[j];

        #Create the necessary number of .gjf files
        for i in range(0, numInc, 1):
            
            #Generate the number part of the gjf filename
            if i < 10:
              fileNum  = "00" + str(i);
            elif i >= 10 and i < 100:
              fileNum = "0" + str(i);
            elif i > 100:
              fileNum = str(i);
            
            #Create the .xyz file
            inputFile = open(cwd + "/scan" + fileSuffix(int(theta*180/math.pi),phi) + "_" + fileNum + '.xyz','w+');
            inputFile.write("8\n");
            
            #Write the coordinates of the first molecule to the file (these do not change).
            for j in range(0, len(refMolecule.atoms), 1):
                tempAtom = refMolecule.atoms[j];
                inputFile.write("\n" + tempAtom.name);
                for k in range(0, 3, 1):
                    inputFile.write("  " + str(tempAtom.coordinates[k]));

        
            #Write the coordinates of the second molecule to the file, each loop will brign the molecules closer by another increment.
            for j in range(0, len(scanMolecule.atoms), 1):
                inputFile.write("\n" + scanMolecule.atoms[j].name);
                for k in range(0, 3, 1):
                    inputFile.write("  "  + str(scanMolecule.atoms[j].coordinates[k]  - sphereToCart(k, incSize*i, theta, phi))[:9]);
            
            #Close the file
            inputFile.close();


print("\n ----- \n")
print("Created .xyz files - waiting for conversion to .gzmat... Type: obabel *.xyz -ogzmat -m" )
conv_done = input("Type '1' when finished: ")
while conv_done != '1':
    conv_done = input("Type '1' when finished: ")

#if betaInc == 19:
#    ANGLE = 190
#    dec = 10
#elif betaInc == 37:
#    ANGLE = 185
#    dec = 5
#elif betaInc == 1:
#    ANGLE = 0
#    dec = 0
    
for m,theta in enumerate(list(np.linspace(theta_in, theta_fin, thetaInc))):
#        ANGLE -= dec
        for i in range(0, numInc, 1):
            
            #Generate the number part of the gjf filename
            if i < 10:
              fileNum  = "00" + str(i);
            elif i >= 10 and i < 100:
              fileNum = "0" + str(i);
            elif i > 100:
              fileNum = str(i);
            
            #Create the .gjf file
            gjfFile = open(cwd + "/scan" + fileSuffix(int(theta*180/math.pi),phi) + "_" + fileNum + '.gjf','w+');
            gzmatFile = open(cwd + "/scan" + fileSuffix(int(theta*180/math.pi),phi) + "_" + fileNum + '.gzmat','r+')
            
            gjfFile.write('%nprocshared=4\n');
            gjfFile.write('# opt=Z-Matrix b3lyp/aug-cc-pvtz \n \n');
            gjfFile.write('Scan' + str(i) + '\n \n');
            gjfFile.write('0 1\n');
            
            for num, line in enumerate(gzmatFile):
                if num in [0,1,2,3,4]:
                    continue
                elif num in [5,6,7,8,9,10,11]:
                    gjfFile.write(line)
                    continue
                elif num == 12:
                    gjfFile.write(line+'\n')
                elif num in [14,15,17,23,26,29,16,18,21,24,27,30]:
                    gjfFile.write(line)
                    
            gjfFile.write('\n')
            gzmatFile.seek(0)
            
            for num, line in enumerate(gzmatFile):
                if num not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,23,26,29,16,18,21,24,27,30]:
                    gjfFile.write(line)

            
            gjfFile.close()
            gzmatFile.close()

os.system("rm *.xyz")
os.system("rm *.gzmat")
print("Done.")