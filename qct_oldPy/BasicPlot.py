#Quick plotting tool

import matplotlib.pyplot as plt

separations = [];
selfenergies = [];
Vne = [];
Ta = [];
Vee = [];
sumVdW = 1.55+1.55;
#open data file.
plt.figure(figsize=(7,6));

dataFile = open("20intra.txt", 'r');
counter= 0;
    
for line in dataFile:
    if counter == 0:
        counter +=1;
        continue;
    temp = line.split();
    separations.append(float(temp[0]));
    selfenergies.append(float(temp[1]));
    Vne.append(float(temp[2]));
    Ta.append(float(temp[3]));
    Vee.append(float(temp[4]));

for i in range(0, len(separations), 1):
    separations[i] = (separations[i])/sumVdW;
        
plt.plot(separations, selfenergies, linestyle="-", marker="^", label="E$_{\mathbf{intra}}$", color="black");
plt.plot(separations, Vne, linestyle="-", marker="o", label="V$_{\mathbf{ne}}$", color="#FF0000");
plt.plot(separations, Ta, linestyle="-", marker="s", label="T", color="#2CFF00");
plt.plot(separations, Vee, linestyle="-", marker="v", label="V$_{\mathbf{ee}}$", color="#0095FF");
separations = [];
selfenergies = [];
Vne = [];
dataFile.close();

#THIS BIT CONTAINS SAME CODE AS ABOVE BUT LOOPED IN CASE YOU WANT TO DO MULTIPLE PLOTS ON SAME GRAPH
#for j in range(1, 19, 1):
    
#    dataFile = open(str(j*10) + ".txt", 'r');
#    counter= 0;
    
#    for line in dataFile:
        #if counter == 0:
        #    counter +=1;
        #    continue;
#        temp = line.split();
#        separations.append(float(temp[0]));
#        selfenergies.append(float(temp[1]));
#        Vne.append(float(temp[2]));
        #Ta.append(float(temp[3]));
        #Vee.append(float(temp[4]));
                              
#    for i in range(0, len(separations), 1):
#        separations[i] = (separations[i])/sumVdW;
        
#    plt.plot(separations, selfenergies, linestyle="-", marker="^", color="black");
#    plt.plot(separations, Vne, linestyle="-", marker="o", color="r");
    #plt.plot(separations, Ta, linestyle="-", marker="s", label="T$_{a}$", color="r");
    #plt.plot(separations, Vee, linestyle="-", marker="v", label="V$_{ee}$", color="black");
#    separations = [];
#    selfenergies = [];
#    Vne = [];
#    dataFile.close();
    
plt.grid(axis='y', linestyle="-");
plt.xlabel("Separation (Relative to Sum of vdW Radii)", size=12);
plt.ylabel("Deformation Energy (kJ/mol)", size=12);
#plt.ylim(1.002, 1.008);
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False);
plt.xlim(0.6, 1.4);
plt.legend(prop={'size': 18});
#plt.ylim(ymin=0);
#plt.ylim(ymax=200);
#plt.xlim(xmin=2.5)
plt.show();