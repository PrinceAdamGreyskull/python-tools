# Author: Andrew Lines
#         anlines@deloitte.com.au
#
# Revision History
# 0.1 - first draft, added all basic functionality

import os
import csv

# Create program variables and storage constructs
# Import TSC text file
thisFile = open('test1.txt', 'rb')
thisData = thisFile.read()
for thisLine in thisData:
    print thisLine
# Read each line
# Match double number pattern
# [maybe] detect USN or RAN and add to column 10
# Output each line to new entry in list
# Output list to CSV