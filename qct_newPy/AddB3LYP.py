"""
Created on Wed Jul  4 15:11:47 2018

@author: bensy
"""
#A basic script that edits .wfn files to include "B3LYP".
import os;

#Get current working directory.
cwd = str(os.getcwd());


noSteps = int(input("Number of scan steps: "))
thetaIn = int(input("Initial angle: "))
thetaFin = int(input("Final angle: "))
thetaSteps = int(input("Size between each angle: "))

for theta in range(thetaIn,thetaFin+1,thetaSteps):
    print(theta)
    for i in range(noSteps):
        if theta < 10:
            angleStr = "00"+str(theta)
        elif 10 <= theta < 100:
            angleStr = "0"+str(theta)
        else:
            angleStr = str(theta)
                    
        if i < 10:
            fileNum = "00" + str(i);
        elif i >= 10 and i < 100:
            fileNum = "0" + str(i);
        elif i > 100:
            fileNum = str(i);
        #Open the original wfn file and create a new, temporary one.
        try:
            originalFile = open(cwd + "/scan" + angleStr + "_" + fileNum + ".wfn", 'r');
        except IOError:
            print("Cannot open" + cwd + "/scan" + angleStr + "_" + fileNum + ".wfn")
            print("Continuing...")
            continue
        newFile = open(cwd + "/temp.wfn", 'w+');
        
        counter = 0;
        for line in originalFile:
            #If the current line is the second line in the file then make the required addition.
            if counter == 1:
                tempString = line.rstrip() + "  B3LYP\n";
                newFile.write(tempString);
                counter = counter +1;
                continue;
            #Otherwise simply copy the file;.
            newFile.write(line);
            counter = counter +1;
            
        #Close and delete the original file.
        originalFile.close();
        os.remove(cwd + "/scan" + angleStr + "_" + fileNum + ".wfn");
    
        #Close and then rename the new file so that it replaces the old one.
        newFile.close();
        os.rename(cwd + "/temp.wfn", cwd + "/scan" + angleStr + "_" + fileNum + ".wfn");
