#Quick plotting tool

import matplotlib.pyplot as plt
import numpy as np


max_energies = []
fig, ax = plt.subplots()

alexEnergy = [150.54,
125.02,
101.46,
84.70,
70.92,
48.93,
34.39,
25.24,
18.48,
13.85,
10.72,
8.35,
6.64,
5.39,
4.50]

alexSep = [0.70,
0.73,
0.75,
0.78,
0.80,
0.85,
0.90,
0.95,
1.00,
1.05,
1.10,
1.15,
1.20,
1.25,
1.30]

for theta in range(0,5,10):
    separations = [];
    energies = [];
    #open data file.
    dataFile = open("rawdata" + str(theta) + ".txt", 'r');
    for line in dataFile:
        temp = line.split();
        separations.append(float(temp[0])/2.94);
        energies.append(float(temp[1])/3.8088E-04);
    max_energies.append(max(energies))     
#    if theta == 0:
#        ax.plot(separations, energies, alpha=0.1, label=str(theta)+"º");
#    else:
#        ax.plot(separations, energies, alpha=theta*2/180, label=str(theta)+"º");

ax.grid()
#ax.plot(list(range(0,180,10)), max_energies, color='b')
ax.plot(separations, energies, color='g')
ax.plot(alexSep, alexEnergy, color='r')
#ax.legend(loc = 0)
plt.xlabel("Separation (Relative to sum of VDW radii)")
#plt.xlabel("Theta (º)");
#plt.xticks(list(range(0,180,10)))
plt.xticks(list(np.linspace(0.7,1.3,7)))
plt.ylabel("Deformation energy (kJ/mol)");
#plt.ylim(ymin=41.2);
#plt.ylim(ymax=41.265);
#plt.xlim(xmin=2.5)
plt.title("HF dimer - linear approach");
plt.show();