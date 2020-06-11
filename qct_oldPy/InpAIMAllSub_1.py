# Writes a Shell Script to submit all .gjf files to Gaussian09 
# Import Modules
import os

# Get path to CWD and store it as a string
cwd = str( os.getcwd() )

wfn_filelist = []

# Get wfn files
for k in os.walk(r"%s"%(cwd)):
   for i in range(0,len(k),1):
      for j in range(0, len(k[i]), 1):
         if ".wfn" in k[i][j]:
            wfn_filelist.append(k[i][j])


k = 0
i = 0
j = 0
# Finds the root, folders and all the files within the CWD and stores them as variables:
# 'root', 'dirs' and 'allfiles'
folderlist = []
i = 0
for root, dirs, allfiles in os.walk(r'%s'%(cwd)):
    for folder in dirs:
       folderlist.append(folder)
       i = i + 1

# Sort to ensure order
folderlist = sorted(folderlist)
wfn_filelist = sorted(wfn_filelist)

# Gets all the inp files in the first folder
files = []
i = 0
for j in range(0, len(allfiles), 1):
    if allfiles[j].endswith('.inp') and ( '_' not in allfiles[j] ):
        files.append(allfiles[j])
        i = i + 1
    else:
        continue


# Ask for user input to define the number of cores
coresnum = int( raw_input('Number of cores per job: ' ) )

# Makes the new submission script file
sh_file = open(cwd + '/InpAIMAllSub_1.sh', 'w')

# Write in the file the first lines (these lines indicate that we want to work within the CWD and use the current shell environment etc. etc. etc. etc.)
sh_file.write( '#!/bin/bash\n\n#$ -cwd\n#$ -j y\n#$ -o AIMALL.log\n#$ -e AIMALL.err\n#$ -S /bin/bash\n#$ -V\n#$ -t 1-%d\n#$ -pe smp.pe %d\n\n' % (len(files)*len(folderlist),coresnum) )

# Tells the script to load Gaussian09 module
sh_file.write( 'PATH=$PATH:~/AIMAll\n\n' )

# Writes out the names of the files and all that shizz into a task array #YOLO
task_id = 1
for i in range(0, len(folderlist), 1):
   for j in range(0, len(files), 1):
      sh_file.write( 'if [ "$SGE_TASK_ID" == "%d" ];\nthen\nsleep 12\n' % (task_id) )
      sh_file.write( '~/AIMAll/aimint.ish %s/%s/%s %s/%s\nfi\n\n' % (cwd, folderlist[i], files[j], cwd, wfn_filelist[i]) )
      task_id = task_id + 1

sh_file.write( 'pwd\ndate\nset' )

sh_file.close()



