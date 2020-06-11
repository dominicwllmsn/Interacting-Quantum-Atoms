import os
cwd = str(os.getcwd());

separations = [];
selfEnergies_f1 = [];
VneEnergies_f1 = [];
TaEnergies_f1 = [];
VeeEnergies_f1 = [];
selfEnergies_f2 = [];
VneEnergies_f2 = [];
TaEnergies_f2 = [];
VeeEnergies_f2 = [];

startSeparation = 3.822 #float(input("Starting separation: "));
numIncs = 15 #int(input("Number of increments: "));
incSize = 0.1176 #float(input("Increment size: "));
for i in range(0, numIncs, 1):
    separations.append(startSeparation - i*incSize);

for run in range (numIncs):
    for i in range(0, len(separations), 1):
        try:
            path = cwd + "/HF_scan"+ str(run) +"/scan" + str(i) + "_atomicfiles/f1.int";
            intfile = open(path, "r")
        except IOError:
            print("Run", run, " -- f1.int does not exist")
            continue
            
        for line in intfile:
                if line.startswith("E_IQA_Intra0(A)"):
                    counter = 0;
                    for j in line:
                        counter +=1;
                        if j == "=":
                              selfEnergy_f1 = float(line[counter+1:]);
                              selfEnergies_f1.append(selfEnergy_f1);
                              break;
        
        intfile.seek(0);
        for line in intfile:
                if line.startswith("Vneen(A,A)/2"):
                    counter = 0;
                    for k in line:
                          counter +=1;
                          if k == "-":
                                VneEnergy_f1 = float(line[counter:]);
                                VneEnergies_f1.append(VneEnergy_f1);
                                break;
                    break;
    
        intfile.seek(0);
        for line in intfile:
                if line.startswith("T(A)"):
                    counter = 0;
                    for l in line:
                          counter +=1;
                          if l == "=":
                                TaEnergy_f1 = float(line[counter+1:]);
                                TaEnergies_f1.append(TaEnergy_f1);
                                break;
                    break;
    
        intfile.seek(0);
        for line in intfile:
                if line.startswith("Vee(A,A)"):
                    counter = 0;
                    for m in line:
                          counter +=1;
                          if m == "=":
                                VeeEnergy_f1 = float(line[counter+1:]);
                                VeeEnergies_f1.append(VeeEnergy_f1);
                                break;
                    break;
    
    
    for i in range(0, len(separations), 1):
        try:
            path = cwd + "/HF_scan"+ str(run) +"/scan" + str(i) + "_atomicfiles/f3.int";
            intfile = open(path, "r")
        except IOError:
            print("Run", run, " -- f3.int does not exist")
            continue
        for line in intfile:
                if line.startswith("E_IQA_Intra0(A)"):
                    counter = 0;
                    for n in line:
                          counter +=1;
                          if n == "=":
                                selfEnergy_f2 = float(line[counter+1:]);
                                selfEnergies_f2.append(selfEnergy_f2);
                                break;
                    break;
        
        intfile.seek(0);
        for line in intfile:
                if line.startswith("Vneen(A,A)/2"):
                    counter = 0;
                    for o in line:
                          counter +=1;
                          if o == "-":
                                VneEnergy_f2 = float(line[counter:]);
                                VneEnergies_f2.append(VneEnergy_f2);
                                break;
                    break;
    
        intfile.seek(0);
        for line in intfile:
                if line.startswith("T(A)"):
                    counter = 0;
                    for p in line:
                          counter +=1;
                          if p == "=":
                                TaEnergy_f2 = float(line[counter+1:]);
                                TaEnergies_f2.append(TaEnergy_f2);
                                break;
                    break;
    
        intfile.seek(0);
        for line in intfile:
                if line.startswith("Vee(A,A)"):
                    counter = 0;
                    for q in line:
                          counter +=1;
                          if q == "=":
                                VeeEnergy_f2 = float(line[counter+1:]);
                                VeeEnergies_f2.append(VeeEnergy_f2);
                                break;
                    break;
    
    
    datafile = open(cwd + "/HF_scan"+ str(run) + "/rawdata" + str(run) + ".txt", 'w+');
    datafile.write("Separation" + "    " + "Self-Energy_f1" + "    " \
                    + "VneEnergy_f1" + "    " + "TaEnergy_f1" + "    " \
                    + "VeeEnergy_f1" + "    " + "Self-Energy_f2" + "    " \
                    + "VneEnergy_f2" + "    " + "TaEnergy_f2" + "    " \
                    + "VeeEnergy_f2" + "\n");
    for i in range (0, len(separations), 1):
        datafile.write(str(separations[i]) \
                    + "         " + str(selfEnergies_f1[i]) + "      " \
                    + str(VneEnergies_f1[i]) + "    " + str(TaEnergies_f1[i]) \
                    + "   " + str(VeeEnergies_f1[i]) + "    " \
                    + str(selfEnergies_f2[i]) + "     " \
                    + str(VneEnergies_f2[i]) + "    " \
                    + str(TaEnergies_f2[i]) + "    " \
                    + str(VeeEnergies_f2[i])+ "\n");
        
    datafile.close()