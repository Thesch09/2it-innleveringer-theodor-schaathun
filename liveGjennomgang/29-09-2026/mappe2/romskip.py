# Just like Daniel Failboat in the making of Cata-Bomb, I, Theodor Schaathun, use no AI
from math import sqrt

def normalizeVector(x,y):
    dist = sqrt(x**2+y**2)
    return x/dist,y/dist