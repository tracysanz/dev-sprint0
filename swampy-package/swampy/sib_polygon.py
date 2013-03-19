# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 	
import math	
world = TurtleWorld()			
bob = Turtle()				


def square():
	for i in range(4):
		fd(bob,100)
		lt(bob)


def squaregen(turtle,len):
	for i in range(4):
		fd(turtle,len)
		lt(turtle)	

def polygon(turtle,len,sides,theta):
	for i in range(sides):
		fd(turtle,len)
		lt(turtle,theta/sides)

def circle(turtle,r):
	circum = r * 2 * math.pi
	sides = 60
	theta = 360
	polygon(turtle,circum/sides,sides,theta)

def arc(turtle,r,theta):
	circum = r * 2 * math.pi
	sides = 60
	polygon(turtle,circum/sides,sides,theta)


arc(bob,30,150)

wait_for_user()					
