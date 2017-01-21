#!/usr/bin/env python

# Description: decorators example
import time
import urllib2

def elapsed_time(function_to_time):
	def wrapper():
		t0 = time.time()
		function_to_time()
		t1 = time.time()
		print "Elapsed time: %s\n" %(t1-t0)
	return wrapper

# we execute function below like function inside decorator
@elapsed_time
def download_webpage():
	url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
	response = urllib2.urlopen(url, timeout = 60)
	return response.read()

webpage = download_webpage()

# there's we use another function
# using decorators provides an ability for using another function in function elapsed_time() without their changing
@elapsed_time
def another_function():
	print "Doing something else"
	for i in range (1,100):
		pass
another_function()