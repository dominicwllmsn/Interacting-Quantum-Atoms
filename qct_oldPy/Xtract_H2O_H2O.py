import os
cwd = str(os.getcwd());

separations = [];
selfEnergies_o1 = [];
VneEnergies_o1 = [];
TaEnergies_o1 = [];
VeeEnergies_o1 = [];
selfEnergies_o4 = [];
VneEnergies_o4 = [];
TaEnergies_o4 = [];
VeeEnergies_o4 = [];
selfEnergies_h2 = [];
VneEnergies_h2 = [];
TaEnergies_h2 = [];
VeeEnergies_h2 = [];
selfEnergies_h3 = [];
VneEnergies_h3 = [];
TaEnergies_h3 = [];
VeeEnergies_h3 = [];
selfEnergies_h5 = [];
VneEnergies_h5 = [];
TaEnergies_h5 = [];
VeeEnergies_h5 = [];
selfEnergies_h6 = [];
VneEnergies_h6 = [];
TaEnergies_h6 = [];
VeeEnergies_h6 = [];
titles = ["Separation" "Self-Energy_o1" "VneEnergy_o1" "TaEnergy_o1" "VeeEnergy_o1" "Self-Energy_o4" "VneEnergy_o4" "TaEnergy_o4" "VeeEnergy_o4"];

startSeparation = float(input("Starting separation: "));
numIncs = int(input("Number of increments: "));
incSize = float(input("Increment size: "));
for i in range(0, numIncs, 1):
        separations.append(startSeparation - i*incSize);


for i in range(0, len(separations), 1):
	
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/o1.int";
	intfile = open(path, "r")

	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for j in line:
          			counter +=1;
          			if j == "=":
            				selfEnergy_o1 = float(line[counter+1:]);
					selfEnergies_o1.append(selfEnergy_o1);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for k in line:
          			counter +=1;
          			if k == "-":
            				posVneEnergy_o1 = float(line[counter:]);
					negVneEnergy_o1 = posVneEnergy_o1 * (-1);
					VneEnergies_o1.append(negVneEnergy_o1);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for l in line:
          			counter +=1;
          			if l == "=":
            				TaEnergy_o1 = float(line[counter+1:]);
					TaEnergies_o1.append(TaEnergy_o1);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)      "):
        		counter = 0;
        		for m in line:
          			counter +=1;
          			if m == "=":
            				VeeEnergy_o1 = float(line[counter+1:]);
					VeeEnergies_o1.append(VeeEnergy_o1);
            				break;
        		break;


for i in range(0, len(separations), 1):
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/o4.int";
	intfile = open(path, "r")
	
	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for n in line:
          			counter +=1;
          			if n == "=":
            				selfEnergy_o4 = float(line[counter+1:]);
					selfEnergies_o4.append(selfEnergy_o4);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for o in line:
          			counter +=1;
          			if o == "-":
            				posVneEnergy_o4 = float(line[counter:]);
					negVneEnergy_o4 = posVneEnergy_o4 * (-1);
					VneEnergies_o4.append(negVneEnergy_o4);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for p in line:
          			counter +=1;
          			if p == "=":
            				TaEnergy_o4 = float(line[counter+1:]);
					TaEnergies_o4.append(TaEnergy_o4);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)      "):
        		counter = 0;
        		for q in line:
          			counter +=1;
          			if q == "=":
            				VeeEnergy_o4 = float(line[counter+1:]);
					VeeEnergies_o4.append(VeeEnergy_o4);
            				break;
        		break;
				
for i in range(0, len(separations), 1):
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/h2.int";
	intfile = open(path, "r")

	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for n in line:
          			counter +=1;
          			if n == "=":
            				selfEnergy_h2 = float(line[counter+1:]);
					selfEnergies_h2.append(selfEnergy_h2);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for o in line:
          			counter +=1;
          			if o == "-":
            				posVneEnergy_h2 = float(line[counter:]);
					negVneEnergy_h2 = posVneEnergy_h2 * (-1);
					VneEnergies_h2.append(negVneEnergy_h2);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for p in line:
          			counter +=1;
          			if p == "=":
            				TaEnergy_h2 = float(line[counter+1:]);
					TaEnergies_h2.append(TaEnergy_h2);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)       "):
        		counter = 0;
        		for q in line:
          			counter +=1;
          			if q == "=":
            				VeeEnergy_h2 = float(line[counter+1:]);
					VeeEnergies_h2.append(VeeEnergy_h2);
            				break;
        		break;


for i in range(0, len(separations), 1):
	
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/h3.int";
	intfile = open(path, "r")

	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for n in line:
          			counter +=1;
          			if n == "=":
            				selfEnergy_h3 = float(line[counter+1:]);
					selfEnergies_h3.append(selfEnergy_h3);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for o in line:
          			counter +=1;
          			if o == "-":
            				posVneEnergy_h3 = float(line[counter:]);
					negVneEnergy_h3 = posVneEnergy_h3 * (-1);
					VneEnergies_h3.append(negVneEnergy_h3);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for p in line:
          			counter +=1;
          			if p == "=":
            				TaEnergy_h3 = float(line[counter+1:]);
					TaEnergies_h3.append(TaEnergy_h3);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)        "):
        		counter = 0;
        		for q in line:
          			counter +=1;
          			if q == "=":
            				VeeEnergy_h3 = float(line[counter+1:]);
					VeeEnergies_h3.append(VeeEnergy_h3);
            				break;
        		break;

for i in range(0, len(separations), 1):
	
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/h5.int";
	intfile = open(path, "r")

	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for n in line:
          			counter +=1;
          			if n == "=":
            				selfEnergy_h5 = float(line[counter+1:]);
					selfEnergies_h5.append(selfEnergy_h5);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for o in line:
          			counter +=1;
          			if o == "-":
            				posVneEnergy_h5 = float(line[counter:]);
					negVneEnergy_h5 = posVneEnergy_h5 * (-1);
					VneEnergies_h5.append(negVneEnergy_h5);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for p in line:
          			counter +=1;
          			if p == "=":
            				TaEnergy_h5 = float(line[counter+1:]);
					TaEnergies_h5.append(TaEnergy_h5);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)         "):
        		counter = 0;
        		for q in line:
          			counter +=1;
          			if q == "=":
            				VeeEnergy_h5 = float(line[counter+1:]);
					VeeEnergies_h5.append(VeeEnergy_h5);
            				break;
        		break;
				
for i in range(0, len(separations), 1):
	
	fileNum = 0;
	if i <10:
		fileNum = "00" + str(i);
	elif 10<= i <100:
		fileNum = "0" + str(i);
	elif i >=100:
		fileNum = str(i);
	
	path = cwd + "/scan" + fileNum + "_atomicfiles/h6.int";
	intfile = open(path, "r")

	for line in intfile:
    		if line.startswith("E_IQA_Intra(A)"):
        		counter = 0;
        		for n in line:
          			counter +=1;
          			if n == "=":
            				selfEnergy_h6 = float(line[counter+1:]);
					selfEnergies_h6.append(selfEnergy_h6);
            				break;
        		break;
	
	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vneen(A,A)/2"):
        		counter = 0;
        		for o in line:
          			counter +=1;
          			if o == "-":
            				posVneEnergy_h6 = float(line[counter:]);
					negVneEnergy_h6 = posVneEnergy_h6 * (-1);
					VneEnergies_h6.append(negVneEnergy_h6);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("T(A)"):
        		counter = 0;
        		for p in line:
          			counter +=1;
          			if p == "=":
            				TaEnergy_h6 = float(line[counter+1:]);
					TaEnergies_h6.append(TaEnergy_h6);
            				break;
        		break;

	intfile.seek(0);
	for line in intfile:
    		if line.startswith("Vee(A,A)         "):
        		counter = 0;
        		for q in line:
          			counter +=1;
          			if q == "=":
            				VeeEnergy_h6 = float(line[counter+1:]);
					VeeEnergies_h6.append(VeeEnergy_h6);
            				break;
        		break;
				
datafile = open(cwd + "/rawdataH2O.txt", 'w+');
datafile.write("Separation" + "    " + "Self-Energy_o1" + "    " \
                + "VneEnergy_o1" + "    " + "TaEnergy_o1" + "    " \
                + "VeeEnergy_o1" + "    " + "Self-Energy_o4" + "    " \
                + "VneEnergy_o4" + "    " + "TaEnergy_o4" + "    " \
                + "VeeEnergy_o4" + "    " + "Self-Energy_h2" + "    " \
                + "VneEnergy_h2" + "    " + "TaEnergy_h2" + "    " \
                + "VeeEnergy_h2" + "    " + "Self-Energy_h3" + "    " \
                + "VneEnergy_h3" + "    " + "TaEnergy_h3" + "    " \
                + "VeeEnergy_h3" + "    " + "Self-Energy_h5" + "    " \
                + "VneEnergy_h5" + "    " + "TaEnergy_h5" + "    " \
                + "VeeEnergy_h5" + "    " + "Self-Energy_h6" + "    " \
                + "VneEnergy_h6" + "    " + "TaEnergy_h6" + "    " \
                + "VeeEnergy_h6" + "\n");
for i in range (0, len(separations), 1):
    datafile.write(str(separations[i]) + "         " \
                + str(selfEnergies_o1[i]) + "      " \
                + str(VneEnergies_o1[i]) + "    " \
				+ str(TaEnergies_o1[i]) + "   " \
				+ str(VeeEnergies_o1[i]) + "    " \
                + str(selfEnergies_o4[i]) + "     " \
                + str(VneEnergies_o4[i]) + "    " \
                + str(TaEnergies_o4[i]) + "    " \
				+ str(VeeEnergies_o4[i])+ "         " \
				+ str(selfEnergies_h2[i]) + "      " \
                + str(VneEnergies_h2[i]) + "    " 
				+ str(TaEnergies_h2[i]) + "  " \
                + str(VeeEnergies_h2[i]) + "    " \
                + str(selfEnergies_h3[i]) + "     " \
                + str(VneEnergies_h3[i]) + "    " \
                + str(TaEnergies_h3[i]) + "    " \
                + str(VeeEnergies_h3[i]) + "     " \
				+ str(selfEnergies_h5[i]) + "     " \
                + str(VneEnergies_h5[i]) + "    " \
                + str(TaEnergies_h5[i]) + "    " \
                + str(VeeEnergies_h5[i]) + "     "\
				+ str(selfEnergies_h6[i]) + "     " \
                + str(VneEnergies_h6[i]) + "    " \
                + str(TaEnergies_h6[i]) + "    " \
				+ str(VeeEnergies_h6[i]) + "\n");
    
datafile.close()