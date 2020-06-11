"""
Created on Fri Jun 29 10:57:49 2018
@author: bensy
"""
#A python script that calculates the energy deformation at each separation in a scan and plots it, for a H2O dimer.

import os
#import matplotlib as plt

#Get the current working directory.
cwd = str(os.getcwd());

#First check for a log file in order to find the separations
separations = [];
try:
    logFile = open(cwd + "/Orient.log", "r");
    #Extract the information from the log file.
    for line in logFile:
        separations.append(float(line));
    
except IOError:
    #If there is no log file then ask the user for the details of the scan.
    startSeparation = float(input("Starting separation: "));
    numIncs = int(input("Number of increments: "));
    incSize = float(input("Increment size: "));
    for i in range(0, numIncs, 1):
        separations.append(startSeparation - i*incSize);

thetaIn = int(input("Initial theta: "));
thetaFin = int(input("Final theta: "));
thetaStep = int(input("Size of theta increments: "));
#Enter the reference energy for the oxygen in a free H2O molecule.
F_energy = -9.9813437152E+01;


#Create an array for the deformation energies.
defEnergies = [];

#Find all the directories that end with "_atomicfiles".
#for dirs in os.walk(r'%s'%(cwd)):
#    continue
    
#print(len(dirs));
#for i in range(0, len(dirs), 1):
#    print(str(dirs[i]) + "\n");
    
#atomicDirs = [];
#for i in range(0,len(dirs),1):
#    temp = str(dirs[i]);
#    if temp.endswith('atomicfiles'):
#        atomicDirs.append(dirs[i]);
#    else:
#        continue
#        
#for i in range(0, len(atomicDirs), 1):
#    print(atomicDirs[i]);

for run in range (thetaIn,thetaFin+1, thetaStep):
    print(run)
    defEnergies = []
    #Enter each of the atomicfiles folders and then each of the .int files to extract the IQA energies.
    for i in range(0, len(separations), 1):
        if i < 10:
            fileNum = "00" + str(i);
        elif 10 <= i < 100:
            fileNum = "0" + str(i);
        elif i > 100:
            fileNum = str(i);
        #open the int file for the first oxygen
        try:
            if run < 10:
                path = cwd + "/scan00"+ str(run) + "_" + fileNum + "_atomicfiles/f1.int";
            elif 10 <= run < 100:
                path = cwd + "/scan0" + str(run) + "_" + fileNum + "_atomicfiles/f1.int";
            else:
                path = cwd + "/scan" + str(run) + "_" + fileNum + "_atomicfiles/f1.int";
            intFile = open(path, 'r+');
        except IOError:
            print("Path:", path, ", Scan", i, " --  f2.int does not exist")
            defEnergies.append("ERROR")
            continue
            
        
        #Run through the file until the line with the IQA energy is reached and store it as a float.
        energy = 0.0;
        for line in intFile:
          if line.startswith("E_IQA_Intra(A)"):
            counter = 0;
            for j in line:
              counter +=1;
              if j == "=":
                energy = float(line[counter+1:]);
                break;
            break;
        #Calculate the deformation energy
        deformationEnergy = energy - F_energy;
        
        #open the int file for the second oxygen
        try:
            if run < 10:
                path = cwd + "/scan00"+ str(run) + "_" + fileNum + "_atomicfiles/f3.int";
            elif 10 <= run < 100:
                path = cwd + "/scan0" + str(run) + "_" + fileNum + "_atomicfiles/f3.int";
            else:
                path = cwd + "/scan" + str(run) + "_" + fileNum + "_atomicfiles/f3.int";
            intFile = open(path, 'r+');
        except IOError:
            print("Path:", path, ", Scan", i, " --  f4.int does not exist")
            try:
                del separations[i]
            except IndexError:
                continue
        
        #Run through the file until the line with the IQA energy is reached and store it as a float.
        for line in intFile:
          if line.startswith("E_IQA_Intra(A)"):
            counter = 0;
            for j in line:
              counter +=1;
              if j == "=":
                energy = float(line[counter+1:]);
                break;
            break;
        #Calculate the total deformation energy and add to out array.
        deformationEnergy = deformationEnergy + energy - F_energy;
        defEnergies.append(deformationEnergy);
    #print("---\n"+len(defEnergies)+"\n---")
    
    #Create a text file with the raw data.
    dataFile = open(cwd + "/rawdataF2F4" + str(run) + ".txt", 'w+');
    for i in range(0, len(separations), 1):
      try:
          dataFile.write(str(separations[i]) + "  " + str(defEnergies[i]) + "\n");
      except IndexError:
          print("Cannot write -- indexing issue")
    dataFile.close();
