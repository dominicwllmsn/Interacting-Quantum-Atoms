#A script that determines the 'goodness' of an exponential fit based on rms differences.
import numpy as np

#Fit parameters
A = 54445.9;
B = 2.23446;

separations = [];
defEnergies = [];
fitDefEnergies = [];

#Read in the data from the text file. 
dataFile = open("rawdataforplot.txt");

for line in dataFile:
    temp = line.split();
    separations.append(float(temp[0]));
    defEnergies.append(float(temp[1]));
    
#Calculate the exact values for the fit.
for i in range(0, len(separations), 1):
    tempVal = A*np.exp(-B*separations[i]);
    fitDefEnergies.append(tempVal);

rmsError = 0.0;
residual = 0.0;
sumResidual = 0.0;
for i in range(0, len(separations), 1):
    residual = fitDefEnergies[i] - defEnergies[i];
    residual = residual*residual;
    sumResidual = sumResidual + residual;
    
rmsError = np.sqrt(sumResidual/len(separations));

print("rms error is: " + str(rmsError));