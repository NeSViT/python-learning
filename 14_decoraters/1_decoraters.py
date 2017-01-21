#!/usr/bin/env python

# Description: we have two functions. Second function calls first function.
# THIS EXAMPLE WILL BE EXTENDED WITH DECORATERS in file 2_decoraters.py

import time
import urllib2

def download_webpage():
	url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
	response = urllib2.urlopen(url, timeout = 60)

	# response.read() helps reading an object like a string
	print "response: %s" %(response.read())
	# then we return html code of this page
	return response.read()

def elapsed_time():
	
	# show current time before loading page
	t0 = time.time()
	print t0
	webpage = download_webpage()

	# show current time after loading page
	t1 = time.time()
	print t1
	
	# subtract time before from after for getting time page
	print "Elapsed time: %s\n" %(t1-t0)

elapsed_time()