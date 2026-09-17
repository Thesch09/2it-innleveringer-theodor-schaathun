# Jeg, Theodor Schaathun, bruker IKKE KI/AI. Jeg har skrudd det helt av

planets = {"Mars":8, "The Cheesy Planet":343353, "Jordkloden":1}
def planetaryLook(planet, moom):
    print("------------------------")
    print(f"Planet: {planet}")
    print(f"Antall måner: {moom}")

def calcDist(fart,hours):
    dist = fart * hours
    return dist

def checkTemp(temp):
    if temp < -100:
        return "I see you used Snowgrave, huh?"
    elif temp < -20:
        return "Det begynner å bli ganske så kaldt kaldt"
    elif temp < 0:
        return "I love snow Charlie! I LOVE SNOW!!!"
    elif temp < 10:
        return "Nærmer seg snø :)"
    elif temp < 25:
        return "This is a Theo-approved temperature"
    elif temp < 35:
        return "Wooh, det begynner å bli varmt"
    else:
        return "MAMA MIA!!!"

for planet in planets:
    planetaryLook(planet, planets[planet])
print("------------------------")

result = calcDist(40,3.5)
print(f"Du kjørt {result}km")

while True:
    temperature = input("Gi meg en temperatur\n")
    try:
        temperature = float(temperature)
        break
    except ValueError:
        print("ikke et tall")

print(checkTemp(temperature))

# En funksjon som regner ut hvor mye drivstoff et romskip bruker
def fuelSpaceshipuation(hours, fuelEfficent): # fuel + spaceship + situation
    return hours * fuelEfficent

print(f"Du har brukt {fuelSpaceshipuation(2077,0.05):.2f}l på din tur")