# Author: Andrew Lines
#         anlines@deloitte.com.au
#
# Revision History
# 0.2 - Now outputing full path for all elements instead of basename
# 0.1 - first draft, added all basic functionality

import os
import csv

# List used to store all directory contents
folderContents = []
#Set up the column labels to be imported into Excel
columnLabels = [['Name', 'Type', 'Parent Folder']]
folderContents.extend(columnLabels)

# Walk the directory structure and return all of the folder and file names
# Add all of the folder and file details to the list
for (dirPath, dirNames, fileNames) in os.walk(os.getcwd()):
    
    #Add all of the subfolders to the list
    for thisFolder in dirNames:
        #tempDetails = [[thisFolder, 'Folder',os.path.basename(dirPath)]]
        tempDetails = [[thisFolder, 'Folder',dirPath]]
        folderContents.extend(tempDetails)
    
    #Add all of the files to the list
    for thisFile in fileNames:
        #tempDetails = [[thisFile, 'File',os.path.basename(dirPath)]]
        tempDetails = [[thisFile, 'File',dirPath]]
        folderContents.extend(tempDetails)

# Create a CSV file from the list
with open('directory_list.csv','wb') as csvFile:
    csvFile.truncate()
    listWriter = csv.writer(csvFile,'excel')
    for row in folderContents:
        listWriter.writerow(row)