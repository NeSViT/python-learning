#!/usr/bin/env python

# Description: script demonstrates how we can handle exceptions duting work with file

try: 
    filename = '/var/log/notthere'
    for line in open(filename):
        print line
except IOError:
    print "File does not exist"
except: 
    print "Can't open file for other reason"
else:
    print "Done processing file"