# Null AI/KI
import time
import math

satellites = []
class satellite:
    def __init__(self, name, planet, distEarth):
        self.name = name
        self.planet = planet
        self.distEarth = distEarth
        satellites.append(self)

    def sendMessage(self):
        lines = ""
        lengthName = len(f"Navn: {self.name}")
        lengthPlanet = len(f"Planet: {self.planet}")
        if lengthName > lengthPlanet:
            for i in range(lengthName):
                lines += "-"
        else:
            for i in range(lengthPlanet):
                lines += "-"
        print(lines)
        print(f"Navn: {self.name}")
        print(f"Planet: {self.planet}")
        print(lines)

    def sendSignal(self):
        print(f"{self.name} sender et signal")
        delay = self.distEarth/300000
        time.sleep(delay/1000)
        print()
        return delay

    def checkDelay(self,delay):
        print(f"Forsinkelsen er {delay:.2f} ({delay/1000:.2f}) sekunder") # Forsinkelsen er {forsinkelse} ({delt på 1000}) sekunder
        if delay < 3:
            return "Det er direkte kommunikasjon"
        elif delay < 30:
            return "Kommunikasjonen er forsiket"
        else:
            return "Det er stor signalforsinkelse"

meatyors = [] # The number 1 vegeterian meat alternative (it rocks)
class meteoriteMaker:
    def __init__(self, name, diameter, distEarth):
        self.name = name
        self.diameter = diameter
        self.distEarth = distEarth
        meatyors.append(self)

    def judgeMeteorite(self):
        print(f"{self.name} er en meteor med diameter på {self.diameter}m som er på det nærmeste {self.distEarth}km unna Jorden")
        danger = self.diameter*10-self.distEarth/max(1,1000-math.floor(self.distEarth/100))
        print(danger)
        if self.distEarth == 0:
            return "Den kolliderer med Jorden"
        elif danger < 5000:
            return "Det er lav risiko"
        elif danger < 50000:
            return "Det er middels risiko"
        else:
            return "Det er høy risiko"

print("Skriv NEI hvis du ikke vil se på satellitter")
if input().lower() != "nei":
    satlit = satellite("Mickey","Pluto", 5900000000-149600000) # Mikke Mus har en hund som heter Pluto
    satlit = satellite("The Flush Five", "Eris",10000000000-149600000) # I Balatro bruker man planet kortet Eris for å oppgradere hånden flush five
    satlit = satellite("Lil' Jimmy", "Sola", 149600000)
    for satelliteThing in satellites:
        satelliteThing.sendMessage()
        delay = satelliteThing.sendSignal()
        print(satelliteThing.checkDelay(delay))
        print()

meatyor = meteoriteMaker("The Phantom Thief", 1180, 40360) # Persona 5
meatyor = meteoriteMaker("Poopcanoizer", 5000, 0) # RTGame Cities Skylines
meatyor = meteoriteMaker("Planet Popstar", 12756000000, 10000000000000) # Kirby
meatyor = meteoriteMaker("Wing-a-Ding", 1000000, 100000) # Villager News add-on for Minecraft bedrock edition/Villager News: Breaking News og Gaste- Long ago, two races ruled over Earth: HUMANS and MONSTERS.
for meteorite in meatyors:
    print(meteorite.judgeMeteorite())
    print()