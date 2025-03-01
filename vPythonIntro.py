from vpython import *
from time import *
floor=box(pos=vector(0,-5,0),size=vector(10,.1,10),color=color.white)
ceiling=box(pos=vector(0,5,0),size=vector(10,.1,10),color=color.white)
rightWall=box(pos=vector(5,0,0),size=vector(.1,10,10),color=color.white)
leftWall=box(pos=vector(-5,0,0),size=vector(.1,10,10),color=color.white)
backWall=box(pos=vector(0,0,-5),size=vector(10,10,.1),color=color.white)
marble=sphere(pos=vector(0,0,0),color=color.red,radius=.75)
deltaX=.1
xPos=0
while True:
    rate(10)
    xPos=xPos+deltaX
    if (xPos>5 or xPos<-5):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)
