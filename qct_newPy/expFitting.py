#Quick plotting tool

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
import numpy as np
from scipy.optimize import curve_fit

def expFunc(t, A, B):
    return A*np.exp(B*t)

F_intra, H_intra = -9.9813437152E+01, -2.1606685337E-01
theta_start = 90
theta_end = 90
theta_step = 5
num_angles = theta_end//15
color1=iter(cm.viridis(np.linspace(0.1,0.9,num_angles + 1)))

max_energies = []
avg_energies = []
paramList= []
i = 1

for theta in range(theta_start,theta_end+1,theta_step):
    separations = [];
    Edef = [];
    #open data file.
    dataFile = open("rawdataFULL" + str(theta) + "_F1F3.txt", 'r');
    for line in dataFile:
        if line.startswith('Separation'):
            continue
        temp = line.split();
        separations.append(float(temp[0])/2.94); #separation rel. to 2*VdV radii
        Edef.append((float(temp[1])+float(temp[5])-2*F_intra)/3.8088E-04)

    max_energies.append(max(Edef[:16]))
    avg_energies.append(sum(Edef[:16])/16)
    fitParams, fitCovariances = curve_fit(expFunc, separations[:16], Edef[:16])
    paramList.append(list(fitParams))
    i += 1
    
    c1 = next(color1)
    plt.plot(separations[:16], expFunc(np.array(separations[:16]), fitParams[0], fitParams[1]), color=c1, label=str(theta))
    plt.scatter(separations[:16], Edef[:16], marker = '^', color=c1)
    
plt.legend()
plt.title("Exponential fits of $E_{def}$ for varied theta")
plt.xlabel("Separation relative to VdW radii")
plt.ylabel("$E_{def}$ (kJ mol$^{-1}$)")
plt.show()
plt.close()

#plt.plot(list(range(theta_start,theta_end+1,theta_step)),[ele[0] for ele in paramList], color='r')
#plt.title("Parameter 'A' for varied theta")
#plt.xlabel("Theta (º)")
#plt.show()
#plt.close()
#
#plt.plot(list(range(theta_start,theta_end+1,theta_step)), [-1*ele[1] for ele in paramList], color='b')
#plt.title("Parameter 'B' for varied theta")
#plt.xlabel("Theta (º)")
#plt.show()
#plt.close()
#
#plt.plot(list(range(theta_start,theta_end+1,theta_step)), max_energies, color='c')
#plt.title("Maximum $E_{def}$ for varied theta")
#plt.xlabel("Theta (º)")
#plt.ylabel("$E_{def}$ (kJ mol$^{-1}$)")
#plt.show()
#plt.close()

