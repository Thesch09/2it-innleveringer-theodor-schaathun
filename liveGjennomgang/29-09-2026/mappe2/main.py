# Just like Daniel Failboat in the making of Cata-Bomb, I, Theodor Schaathun, use no AI
# Moduler
#import random
from random import randint
import math
from romskip import normalizeVector

planets = ["Mercurius","Venus","Terra", "Mars","Jupiter","Saturnus", "Uranus", "Neptunus"]
planetNumber =randint(0,7)
print(planetNumber)
print(planets[planetNumber])
#print(random.choice(planets))

xPos = 100
yPos = 100
dist = math.sqrt(xPos**2+yPos**2)
print(normalizeVector(xPos,yPos))
'''print(dist)
print(xPos/dist)
print(yPos/dist)'''