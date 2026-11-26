def calcDist(speed, hours):
    if hours < 0:
        raise ValueError("Hours cannot be less than 0")
    return abs(speed) * hours

def calcFuel(dist, hours): #spun off GFuel
    return dist * hours

def welcomeTravaleer(name):
    print(f"Well hello there Travaleer {name}. How do you do fellow space Travaleer?")
    return f"Well hello there Travaleer {name}. How do you do fellow space Travaleer?"