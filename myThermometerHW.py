from vpython import *
import numpy as np
scene.background = color.white
outerCylinder=cylinder(pos=vector(0,0,0), axis=vector(0,10,0), length=10, radius=.8, color=color.white, opacity=.5)
innerCylinder=cylinder(pos=vector(0,0,0), axis=vector(0,5,0), length=8, radius=.5, color=color.red, opacity=.5)
bulb=sphere(pos=vector(0,-0.5,0), radis=1, color=color.red)
while True:
    pass
    for myLength in np.linspace(1,8,1000):
        rate(150)
        innerCylinder.length=myLength
    for myLength in np.linspace(8,1,1000):
        rate(150)
        innerCylinder.length=myLength  