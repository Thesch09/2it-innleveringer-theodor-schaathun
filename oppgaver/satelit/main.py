# Null AI/KI
import time

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
        return delay

satlit = satellite("Mickey","Pluto", 5900000000-149600000)
satlit = satellite("The Flush Five", "Eris",10000000000-149600000)
satlit = satellite("Lil' Jimmy", "Sola", 149600000)
for satelliteThing in satellites:
    satelliteThing.sendMessage()
    print(f"{satelliteThing.sendSignal():.2f}")