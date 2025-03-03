from vpython import *
import numpy as np
glassBulb=sphere(radius=1.25,color=color.white, opacity=.3)
glassCylinder=cylinder(radius=.55, length=6, color=color.white, opacity=.5)
mercSphere=sphere(radius=1, color=color.red, )
mercColumn=cylinder(radius=.45,length=6,color=color.red)
for tick in np.linspace(1,6,15):
    box(size=vector(.05,.5,.25),color=color.white,pos=vector(tick,0,.5))
while True:
    pass
    for myTemp in np.linspace(1,6,100):
        rate(25)
        mercColumn.length=myTemp
    for myTemp in np.linspace(6,1,100):
        rate(25)
        mercColumn.length=myTemp