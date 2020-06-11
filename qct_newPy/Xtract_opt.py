import os
cwd = str(os.getcwd());


for ele in ['f1','f2']:
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
  
  path = cwd + "/"+ele+".int";
  intfile = open(path, 'r+');
      
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


  datafile = open(cwd + "/rawdataFULL"+ele+".txt", 'w+');
  datafile.write("Self-Energy_f1" + "    " \
                  + "VneEnergy_f1" + "    " + "TaEnergy_f1" + "    " \
                  + "VeeEnergy_f1" + "    " + "VeeC_f1" + "    "+ "VeeX_f1" \
                  + "    "+"Vol1"+ "    "+"charge1\n")

  datafile.write(str(selfEnergies_f1[0]) + "      " \
              + str(VneEnergies_f1[0]) + "    " + str(TaEnergies_f1[0]) \
              + "   " + str(VeeEnergies_f1[0]) + "    " \
              + str(VeeC_f1[0])+ "    " + str(VeeX_f1[0])+ "    " + str(Vol_f1[0])\
              + "    " + str(q_f1[0]))
      
  datafile.close()
  print(ele.capitalize(), "done.")
