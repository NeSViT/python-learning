#!/usr/bin/env python

# Description: class example

class Car():
	# init function with some variables
	def __init__(self):
		self.color = ''
		print "Car started"
	# acceleration function	
	def accel(self,speed):
		print "Speeding up to %s mph" %(speed)
	# turn function
	def turn(self, direction):
		print "Turning " + direction
	# stop function
	def stop(self):
		print "Stop"

# how to use class 
car1 = Car()

# set variable color 
car1.color='red'

# call function "accel" from class
car1.accel(10)

# call function "turn"
car1.turn('right')

# call function "stop"
car1.stop()

# show all variables that used in variable car1 that equal to class Car()
print vars(car1)

# Class can inherit other class and use methods from this class
class RaceCar(Car):
	def __init__(self, color):
		self.color = color
		self.top_speed = 200
		print "%s race car started with a top speed of %s" %(self.color, self.top_speed)
	def accel(self,speed):
		print "Speeding up to %s mph very very fast" %(speed)

# define variable with new class 
car2 = RaceCar('blue')

# we can change variable inside as previous
car2.color = 'red'

# we can call function from class RaceCar()
car2.accel(10)

# we can call functions from class Car(), because RaceCar() inherit Car()
car2.turn('left')

# and other function from Car()
car2.stop()

# show variables that contain in car2
print vars(car2)