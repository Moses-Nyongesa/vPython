from vpython import *
from time import *
mRadius=.75
wallThickniss=.1
roomWidth=10
roomDepth=5
roomHeight=10
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickniss,roomDepth),color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickniss,roomDepth),color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickniss,roomHeight,roomDepth),color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickniss,roomHeight,roomDepth),color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickniss),color=color.white)
marble=sphere(pos=vector(0,0,0),color=color.red,radius=mRadius)
deltaX=.1
xPos=0
while True:
    rate(10)
    xPos=xPos+deltaX
    if (xPos>roomWidth/2 or xPos<-roomWidth/2):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)
