# Author: Andrew Lines
#         anlines@deloitte.com.au
#
# Revision History
# 0.2 - made the filename comparison case insensitive
# 0.1 - Initial structure and functionality

import os
import csv
import shutil

pblFolder = 'PBL Docs'
transTable = 'transTable.csv'
flag1 = 0
flag2 = 0
flag3 = 0

# Create list of files in current folder
fileList = os.listdir(".")

# Create new folder
os.mkdir(pblFolder)

# Read in document translation table
with open(transTable, 'rb') as csvFile:
    csvReader = csv.reader(csvFile,'excel')
    
    # Test documents in folder for presence in table
    for thisRow in csvReader:
        flag1 += 1
        print 'f1_%d' % flag1

        # If file is in table
        for thisFile in fileList:
            if thisFile.lower() == thisRow[0].lower():
                flag2 += 1
                print 'f2_%d' % flag2
                
                
                # Copy file to new folder
                currFilePath = '%s\\%s'%(os.getcwd(),thisFile)
                ##print currFilePath
                newPath = '%s\\%s'%(os.getcwd(),pblFolder)
                ##print newPath
                shutil.copy2(currFilePath,newPath)
                
                # Rename file if necessary
                if thisFile != thisRow[1]:
                
                    flag3 += 1
                    print 'f3_%d' % flag3
                
                    newFilePath = '%s\\%s'%(newPath,thisFile)
                    ##print newFilePath
                    ##print thisRow[1]
                    os.rename(newFilePath,os.path.join(newPath,thisRow[1]))
                
                # currFilePath = '%s\\%s'%(os.getcwd(),thisFile)
                # newPath = '%s\\%s'%(os.getcwd(),pblFolder)
                # os.rename(currFilePath,os.path.join(newPath,thisRow[1]))