# Hello excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

world.clear()

bob = Turtle()

def turn(turtle):
  rt(turtle)
  rt(turtle)

def bigline(turtle):
  fd(turtle, 100)
  turn(turtle)   

def nextletter(turtle):
   pu(turtle)
   fd(turtle,30)
   pd(turtle)
   
pu(bob)
bk(bob,150)
pd(bob)
lt(bob)

bigline(bob)

fd(bob,50)
lt(bob)
fd(bob,40)
lt(bob)
fd(bob,50)
turn(bob)
fd(bob,100)
lt(bob)

nextletter(bob)

lt(bob)

bigline(bob)
lt(bob)
fd(bob,40)
turn(bob)
fd(bob,40)
lt(bob)
fd(bob,50)
lt(bob)
fd(bob,40)
turn(bob)
fd(bob,40)
lt(bob)
fd(bob,50)
lt(bob)
fd(bob,40)

pu(bob) 
lt(bob)

rt(bob)

nextletter(bob)
lt(bob)
bigline(bob)
bigline(bob)
rt(bob)
fd(bob,40)

nextletter(bob)
lt(bob)
bigline(bob)
bigline(bob)
rt(bob)
fd(bob,40)

nextletter(bob)
lt(bob)
bigline(bob)
lt(bob)
fd(bob,40)
rt(bob)
bigline(bob)
lt(bob)
fd(bob,40)





wait_for_user()					
