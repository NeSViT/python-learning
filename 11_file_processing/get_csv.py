	
#!/usr/bin/env python

# Description: this script go throught the csv-file and calculate quantity of the same values in a dictionary 

import csv

file_path = 'servers.csv'
# open file to variable file_handle
file_handle = open(file_path)

#read file with method reader in module csv
reader = csv.reader(file_handle)

# create empty dictionary
os_counts = {}

# go throught the output placed in reader
for row in reader:

	# just print all row
	print row
	
	# just print third second column 
	print row[2]

	# 
	os_counts[row[2]] = os_counts.get(row[2],0)+1

# Show the dictionary
print os_counts

# Show user friendly output
for os, os_count in os_counts.items():
	print "In CSV-file %s script found %s numbers of %s" %(file_path,os_count,os)
