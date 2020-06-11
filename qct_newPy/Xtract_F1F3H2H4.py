import os
cwd = str(os.getcwd());


startSeparation = float(input("Starting separation: "));
numIncs = int(input("Number of scan increments: "));
incSize = float(input("Increment size: "));

thetaIn = int(input("Initial theta: "));
thetaFin = int(input("Final theta: "));
thetaStep = int(input("Size of theta increments: "));


for ele in [('f1','f3'),('h2','h4')]:
    for run in range (thetaIn,thetaFin+1, thetaStep):
        selfEnergies_f1 = [];
        VneEnergies_f1 = [];
        TaEnergies_f1 = [];
        VeeEnergies_f1 = [];
        selfEnergies_f2 = [];
        VneEnergies_f2 = [];
        TaEnergies_f2 = [];
        VeeEnergies_f2 = [];
        VeeC_f1, VeeX_f1, VeeC_f2, VeeX_f2 = [], [], [], []
        Vol_f1, Vol_f2, q_f1, q_f2 = [], [], [], []
        separations = []
        for i in range(0, numIncs, 1):
            separations.append(startSeparation - i*incSize);
        print(run)    #Enter each of the atomicfiles folders and then each of the .int files to extract the IQA energies.
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
                    path = cwd + "/scan00"+ str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[0])+".int";
                elif 10 <= run < 100:
                    path = cwd + "/scan0" + str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[0])+".int";
                else:
                    path = cwd + "/scan" + str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[0])+".int";
                intfile = open(path, 'r+');
            except IOError:
                print("Angle", run, ", Scan", i, " --  "+str(ele[0])+".int does not exist")
                del separations[i]
                print("Deleted separation")
                continue
            
            for line in intfile:
                    if line.startswith("E_IQA_Intra(A)"):
                        counter = 0;
                        for j in line:
                            counter +=1;
                            if j == "=":
                                  selfEnergy_f1 = float(line[counter+1:]);
                                  selfEnergies_f1.append(selfEnergy_f1);
                                  break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("Vneen(A,A)/2"):
                        counter = 0;
                        for k in line:
                              counter +=1;
                              if k == "-":
                                    VneEnergy_f1 = float(line[counter:]);
                                    VneEnergies_f1.append(-1.*VneEnergy_f1);
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
                    if line.startswith("Vee(A,A)      "):
                        counter = 0;
                        for m in line:
                              counter +=1;
                              if m == '+':
                                  continue
                              elif m == "=":
                                    VeeEnergy_f1 = float(line[counter+1:]);
                                    VeeEnergies_f1.append(VeeEnergy_f1);
                                    break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("VeeC(A,A)      "):
                        counter = 0;
                        for a in line:
                              counter +=1;
                              if a == '+':
                                  continue
                              elif a == "=":
                                    VeeC = float(line[counter+1:]);
                                    VeeC_f1.append(VeeC);
                                    break;
                        break;
                        
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("VeeX(A,A)      "):
                        counter = 0;
                        for b in line:
                              counter +=1;
                              if b == '+':
                                  continue
                              elif b == "=":
                                    VeeX = float(line[counter+1:]);
                                    VeeX_f1.append(VeeX);
                                    break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("  Vol1"):
                        counter = 0;
                        for b in line:
                              counter +=1;
                              if b == "=":
                                    Vol = float(line[counter+1:]);
                                    Vol_f1.append(Vol);
                                    break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("          N ="):
                        q = float(line[37:55]);
                        q_f1.append(q);
                        break;
        
        
        for z in range(0, len(separations), 1):
            if z < 10:
                fileNum = "00" + str(z);
            elif 10 <= z < 100:
                fileNum = "0" + str(z);
            elif z > 100:
                fileNum = str(z);
            try:
                if run < 10:
                    path = cwd + "/scan00"+ str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[1])+".int";
                elif 10 <= run < 100:
                    path = cwd + "/scan0" + str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[1])+".int";
                else:
                    path = cwd + "/scan" + str(run) + "_" + fileNum + "_atomicfiles/"+str(ele[1])+".int";
                intfile = open(path, 'r+');
            except IOError:
                print("Angle", run, ", Scan", z, " --  "+str(ele[1])+".int does not exist")
                del separations[z]
                print("Deleted separation")
                continue
            
            for line in intfile:
                    if line.startswith("E_IQA_Intra(A)"):
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
                                VneEnergies_f2.append(-1.*VneEnergy_f2);
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
                    if line.startswith("Vee(A,A)      "):
                        counter = 0;
                        for q in line:
                            counter +=1;
                            if q =='+':
                                continue
                            elif q == "=":
                                VeeEnergy_f2 = float(line[counter+1:]);
                                VeeEnergies_f2.append(VeeEnergy_f2);
                                break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("VeeC(A,A)      "):
                        counter = 0;
                        for c in line:
                              counter +=1;
                              if c == '+':
                                  continue
                              elif c == "=":
                                    VeeC = float(line[counter+1:]);
                                    VeeC_f2.append(VeeC);
                                    break;
                        break;
                        
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("VeeX(A,A)      "):
                        counter = 0;
                        for d in line:
                              counter +=1;
                              if d == '+':
                                  continue
                              elif d == "=":
                                    VeeX = float(line[counter+1:]);
                                    VeeX_f2.append(VeeX);
                                    break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("  Vol1"):
                        counter = 0;
                        for b in line:
                              counter +=1;
                              if b == "=":
                                    Vol = float(line[counter+1:]);
                                    Vol_f2.append(Vol);
                                    break;
                        break;
            
            intfile.seek(0);
            for line in intfile:
                    if line.startswith("          N ="):
                        q = float(line[37:55]);
                        q_f2.append(q);
                        break;
            
        
        datafile = open(cwd + "/rawdataFULL" + str(run) + "_"+str(ele[0]).capitalize() \
                        +str(ele[1]).capitalize()+".txt", 'w+');
        datafile.write("Separation" + "    " + "Self-Energy_f1" + "    " \
                        + "VneEnergy_f1" + "    " + "TaEnergy_f1" + "    " \
                        + "VeeEnergy_f1" + "    " + "Self-Energy_f2" + "    " \
                        + "VneEnergy_f2" + "    " + "TaEnergy_f2" + "    " \
                        + "VeeEnergy_f2" + "    "+ "VeeC_f1" + "    "+ "VeeX_f1" \
                        + "    "+ "VeeC_f2" + "    "+ "VeeX_f2"+"    "+ "Vol1" +\
                        "    "+ "Vol2"+"    "+ "charge1"+"    "+ "charge2"+"\n");
        for i in range (0, len(separations), 1):
            datafile.write(str(separations[i]) \
                        + "         " + str(selfEnergies_f1[i]) + "      " \
                        + str(VneEnergies_f1[i]) + "    " + str(TaEnergies_f1[i]) \
                        + "   " + str(VeeEnergies_f1[i]) + "    " \
                        + str(selfEnergies_f2[i]) + "     " \
                        + str(VneEnergies_f2[i]) + "    " \
                        + str(TaEnergies_f2[i]) + "    " \
                        + str(VeeEnergies_f2[i]) + "    " + str(VeeC_f1[i])+ "    " \
                        + str(VeeX_f1[i]) + "    " + str(VeeC_f2[i]) + "    " + str(VeeX_f2[i]) \
                        + "    " + str(Vol_f1[i]) + "    " + str(Vol_f2[i])+ "    " + str(q_f1[i])\
                        + "    " + str(q_f2[i])+"\n");
            
        datafile.close()
    
    print("--- Run 1 done ---")
