"""
Created on Wed Jul  4 15:11:47 2018

@author: bensy
"""
#A basic script that edits .wfn files to include "B3LYP".
import os;

#Get current working directory.
cwd = str(os.getcwd());

numWfns = 0;
#Find out how many .wfn files are in the cwd
for filename in os.listdir(cwd):
    if filename.endswith(".wfn"):
        numWfns = numWfns + 1;
        continue;

fileNum = 0;
for i in range(0, numWfns, 1):
    
    if i < 10:
        fileNum = "00" + str(i);
    elif i >= 10 and i < 100:
        fileNum = "0" + str(i);
    elif i > 100:
        fileNum = str(i);
    #Open the original wfn file and create a new, temporary one.
    originalFile = open(cwd + "/scan" + fileNum + ".wfn", 'r');
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
    os.remove(cwd + "/scan" + fileNum + ".wfn");

    #Close and then rename the new file so that it replaces the old one.
    newFile.close();
    os.rename(cwd + "/temp.wfn", cwd + "/scan" + fileNum + ".wfn");