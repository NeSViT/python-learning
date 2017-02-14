#!/usr/bin/env python

# Description:

# NOT A GENERATOR
# function 
def counter():
	i=0
	while True:
		i+=1
		return i

# a equal function counter
a = counter()
print a
print a
print a
print a
print a

# check type of this variable
print type(a)

# GENERATOR
def counter():
	i=0
	while True:
		i+=1
		yield i

a = counter()
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)

print type(a)