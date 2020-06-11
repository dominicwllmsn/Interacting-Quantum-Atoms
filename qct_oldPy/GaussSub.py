# Writes a Shell Script to submit all .gjf files to Gaussian09 
# Import Modules
import os

# Get path to CWD and store it as a string
cwd = str( os.getcwd() )

# Finds the root, folders and all the files within the CWD and stores them as variables:
# 'root', 'dirs' and 'allfiles'
for root, dirs, allfiles in os.walk(r'%s'%(cwd)):
    continue

# Loop through all files in CWD and make new array that only contains ones that end with GJF
files = []
for i in range(0,len(allfiles),1):
    if allfiles[i].endswith('.gjf'):
        files.append(allfiles[i])
    else:
        continue

# Ask for user input to define the number of cores
coresnum = 4

# Makes the new submission script file
sh_file = open(cwd + '/GaussSub.sh', 'w')

# Write in the file the first lines (these lines indicate that we want to work within the CWD and use the current shell environment etc. etc. etc. etc.)
sh_file.write( '#!/bin/bash -l\n#$ -cwd\n#$ -V\n#$ -t 1-%d\n#$ -pe smp.pe %d\n\n' % (len(files),coresnum) )

# Tells the script to load Gaussian09 module
sh_file.write( 'module load apps/binapps/gaussian/g09b01_em64t\nmodule list\n\n' )

# Writes out the names of the files and all that shizz into a task array #YOLO
task_id = 1
for i in range(0, len(files), 1):
    sh_file.write( 'if [ "$SGE_TASK_ID" == "%d" ];\nthen\nsleep 12\nexport PREFERRED_SCRDIR=/scratch\n' % (task_id) )
    sh_file.write( '$g09root/g09/g09 %s.gjf %s.log\ncp fort.7 %s.dev\nfi\n\n' % (files[i][:-4], files[i][:-4], files[i][:-4]) )
    task_id = task_id + 1

sh_file.close()



