import os
import csv

# Create storage for all of the CSV data
csvExtract = []

# Padding lengths to ensure CSV structure is retained without data loss
fields_rev = 20
fields_title = 25

# Strings that I'm searching for in the field names
drgNum1 = '_DRGNO'
drgNum2 = '_DRG.NO'
drgNum3 = '99-999-9999-A'
revNum = 'REV'
titleName = '_TITLE'
titleList = []
for idx in range(0,fields_title):
    titleList.append("T%d" % idx)
    
# Standard format for a blank field
blankText = '~'

# Set up first row of CSV file with column headings
firstRow = ['File name','Parent Folder','Drawing Number']
for idx in range(0, fields_title+1):
    firstRow.append("TITLE%d" % idx)
for idx in range(0, fields_rev+1):
    firstRow.append("REV%d" % idx)
csvExtract.append(firstRow)

# Walk through the folder structure to find all of the CSV documents
for (dirPath, dirNames, fileNames) in os.walk(os.getcwd()):
    # Locate every CSV file
    for thisFile in fileNames:
        if thisFile.endswith('.csv')|thisFile.endswith('.CSV'):
            # Storage for the information extracted from the CSV
            titleFields = []
            revFields = []
            otherFields = []
            # counter for postion in CSV file
            rowNum = 0
            # markers for field positions
            index_drgNum = -1
            index_title = []
            index_revision = []
            
            #add the file name and folder location
            otherFields.append(thisFile)
            # otherFields.append(os.path.basename(dirPath))
            otherFields.append(dirPath)
            # print "A"
            # create CSV reader
            with open(os.path.join(dirPath,thisFile),'rb') as csvFile:
                csvReader = csv.reader(csvFile,'excel')
                for thisRow in csvReader:
                    # print thisRow
                    # read the first row
                    if rowNum ==0:
                        
                        #determine the location of the needed fields
                        for colNum in range(0,len(thisRow)):
                            # Search for drawing number
                            if drgNum1 in thisRow[colNum]:
                                index_drgNum = colNum
                            elif drgNum2 in thisRow[colNum]:
                                index_drgNum = colNum
                            elif drgNum3 in thisRow[colNum]:
                                index_drgNum = colNum
                            # Search for revision fields
                            elif thisRow[colNum].endswith(revNum):
                                index_revision.append(colNum)
                            # Search for title fields
                            elif titleName in thisRow[colNum]:
                                index_title.append(colNum)
                            else:
                                for thisPattern in titleList:
                                    if thisPattern in thisRow[colNum]:
                                        index_title.append(colNum)
                                        
                    #extract the fields from the other rows
                    else:
                        # extract drawing number
                        if rowNum == 1:
                            if index_drgNum == -1:
                                otherFields.append(blankText)
                                # print "1"
                            else:
                                otherFields.append(thisRow[index_drgNum])
                                # print "2"
                        # extract title fields
                        for idx in index_title:
                            if thisRow[idx] != "":
                                titleFields.append(thisRow[idx])
                                # print "3"
                        # extract revision numbers
                        for idx in index_revision:
                            if  thisRow[idx] != "":
                                revFields.append(thisRow[idx])
                                # print "4"
                            
                    rowNum += 1
                    
            # pad the title and revision datafields to guarantee structure
            for idx in range (0, fields_title - len(titleFields)):
                titleFields.append(blankText)
                
            for idx in range(0, fields_rev - len(revFields)):
                revFields.append(blankText)
                
            #save the extracted data to the overall records list
            csvExtract.append(otherFields+titleFields+revFields)
# print csvExtract

# Create a CSV file from the list
with open('drawing_records.csv','wb') as csvFile:
    csvFile.truncate()
    recordWriter = csv.writer(csvFile,'excel')
    for row in csvExtract:
        recordWriter.writerow(row)